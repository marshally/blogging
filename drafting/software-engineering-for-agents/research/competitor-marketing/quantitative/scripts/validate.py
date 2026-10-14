#!/usr/bin/env python3
"""Validate schema 1.0 rows, identity/metric semantics and immutable evidence bytes.
Requires: jsonschema, beautifulsoup4, lxml; pypdf for PDF locators.
Usage: python scripts/validate.py [dataset-or-shard] [--context ROOT]
"""
import argparse,datetime as dt,hashlib,html,json,pathlib,re,sys,uuid
from collections import Counter
from jsonschema import Draft202012Validator,FormatChecker
Q=pathlib.Path(__file__).resolve().parents[1]
TABLES={'entities':'entity','relationships':'relationship','captures':'capture','content':'content','observations':'observation','coverage':'coverage','derived-metrics':'observation'}
KEYS={'entities':'entity_id','relationships':'relationship_id','captures':'capture_id','content':'content_id','observations':'observation_id','coverage':'coverage_id','derived-metrics':'observation_id'}
START='2026-07-16T00:00:00Z';END='2026-10-14T00:00:00Z'
def canonical(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False)
def load_json(path):return json.loads(path.read_text('utf-8'),parse_constant=lambda x:(_ for _ in ()).throw(ValueError('Non-finite JSON '+x)))
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def stamp(s):return dt.datetime.fromisoformat(s.replace('Z','+00:00'))
def date_value(t):
 if t is None:return
 v=t['value'];p=t['precision']
 if p=='second':stamp(v)
 elif p=='day':dt.date.fromisoformat(v)
 elif p=='month':dt.date.fromisoformat(v+'-01')
 elif p=='year':dt.date(int(v),1,1)
 if p=='second' and not v.endswith('Z'):raise ValueError('Non-UTC time')
def read_tables(root):
 out={}
 for table in TABLES:
  p=root/(table+'.jsonl')
  if not p.exists():
   if table=='derived-metrics' and root!=Q:out[table]=[];continue
   raise ValueError(f'Missing required {p}')
  b=p.read_bytes()
  if b.startswith(b'\xef\xbb\xbf') or (b and not b.endswith(b'\n')):raise ValueError(f'BOM or missing final LF: {p}')
  rows=[]
  for n,line in enumerate(b.decode('utf-8').splitlines(),1):
   if not line:raise ValueError(f'Blank JSONL line {p}:{n}')
   x=json.loads(line,parse_constant=lambda v:(_ for _ in ()).throw(ValueError(v)))
   if canonical(x)!=line:raise ValueError(f'Noncanonical JSONL serialization {p}:{n}')
   rows.append(x)
  out[table]=rows
 return out

def pointer(value,p):
 if p=='':return value
 if not p.startswith('/'):raise ValueError('JSON pointer must start /')
 for part in p[1:].split('/'):
  k=part.replace('~1','/').replace('~0','~');value=value[int(k)] if isinstance(value,list) else value[k]
 return value

def validate(roots,configuration=Q,strict_sort=False):
 schema=load_json(configuration/'data-contract.schema.json');registry=load_json(configuration/'metric-definitions.json');run=load_json(configuration/'run.json')
 Draft202012Validator.check_schema(schema)
 validators={name:Draft202012Validator({'$schema':schema['$schema'],'$defs':schema['$defs'],'$ref':'#/$defs/'+name},format_checker=FormatChecker()) for name in schema['$defs']}
 for file,key in [('run.json','run'),('metric-definitions.json','metric_registry')]:
  value=load_json(configuration/file);validators[key].validate(value)
  assert (configuration/file).read_text()==json.dumps(value,ensure_ascii=False,sort_keys=True,indent=2)+'\n',f'Configuration serialization {file}'
 assert run['schema_sha256']==digest(configuration/'data-contract.schema.json'),'Schema hash drift'
 assert run['metric_registry_sha256']==digest(configuration/'metric-definitions.json'),'Metric hash drift'
 assert (run['window_start'],run['window_end'],run['timezone'])==(START,END,'UTC'),'Baseline window changed'
 assert (stamp(END)-stamp(START)).days==90
 assert (run['status']=='planned')==(run['created_at'] is None),'Run creation/status mismatch'
 metrics={m['metric_id']:m for m in registry['metrics']};assert len(metrics)==len(registry['metrics']),'Duplicate metric ID'
 assert len(run['competitors'])==5 and sum(len(c['person_ids']) for c in run['competitors'])==7,'Competitor mapping'
 tables={t:{} for t in TABLES};locations={};warnings=set();total=Counter()
 for root in roots:
  for table,rows in read_tables(root).items():
   ids=[]
   for row in rows:
    validators[TABLES[table]].validate(row);id=row[KEYS[table]];ids.append(id)
    assert row['run_id']==run['run_id'],f'Run drift {id}'
    assert row['worker_id'] in run['worker_ids'],f'Unassigned worker {id}'
    if 'workers' in root.parts:assert row['worker_id']==root.name,f'Shard ownership {id}'
    if table not in ('entities','content'):assert uuid.UUID(id).version==4,f'Not UUIDv4 {id}'
    if id in tables[table]:assert canonical(tables[table][id])==canonical(row),f'Conflicting duplicate {id}'
    else:tables[table][id]=row;locations[id]=root
   assert len(ids)==len(set(ids)),f'Duplicate row ID within {root}/{table}'
   if strict_sort and root==configuration:assert ids==sorted(ids),f'Unsorted root table {table}'
 entities=tables['entities'];content=tables['content'];captures=tables['captures'];coverage=tables['coverage'];relations=tables['relationships'];observations=dict(tables['observations']);observations.update(tables['derived-metrics']);subjects={**entities,**content}
 assert not (set(entities)&set(content)),'Entity/content ID collision'
 assert not (set(tables['observations'])&set(tables['derived-metrics'])),'Observation/derived ID collision'
 def fk(id,collection=subjects):assert id in collection,f'Unresolved foreign key {id}'
 for c in run['competitors']:
  for p in c['person_ids']:fk(p,entities);assert entities[p]['entity_type']=='person' and c['competitor_id'] in entities[p]['competitor_ids']
 artifacts={};artifact_bytes={}
 for cap in captures.values():
  if cap['source_owner_id']:fk(cap['source_owner_id'],entities)
  assert cap['status']!='complete' or cap['failure_reason'] is None,f'Complete capture with failure {cap["capture_id"]}'
  for a in cap['artifacts']:
   rel=pathlib.PurePosixPath(a['path']);assert not rel.is_absolute() and '..' not in rel.parts,'Unsafe archive path'
   assert a['path']==f'archive/sha256/{a["sha256"][:2]}/{a["sha256"]}','Hash path mismatch'
   path=locations[cap['capture_id']]/rel;b=path.read_bytes()
   assert len(b)==a['byte_length'] and hashlib.sha256(b).hexdigest()==a['sha256'],f'Archive corruption {path}'
   if a['text_encoding']:b.decode(a['text_encoding'])
   artifacts[(cap['capture_id'],a['sha256'])]=a;artifact_bytes[a['sha256']]=b
  for a in cap['artifacts']:
   if a['derived_from_sha256']:assert any(x['sha256']==a['derived_from_sha256'] for x in cap['artifacts']) or a['derived_from_sha256'] in artifact_bytes,'Unresolved derived artifact'
 def evcheck(e):
  fk(e['capture_id'],captures);key=(e['capture_id'],e['artifact_sha256']);assert key in artifacts,'Evidence object not in capture'
  a=artifacts[key];b=artifact_bytes[e['artifact_sha256']];typ=e['locator_type'];loc=e['locator'];text=b.decode(a['text_encoding'] or 'utf-8',errors='replace');target=text
  if typ=='json_pointer':target=pointer(json.loads(text),loc);target=canonical(target) if not isinstance(target,str) else target
  elif typ in ('css_selector','xpath'):
   if typ=='css_selector':
    from bs4 import BeautifulSoup
    selected=BeautifulSoup(text,'html.parser').select(loc);assert selected,f'CSS locator missing: {loc}';target=' '.join(str(x)+' '+x.get_text(' ',strip=True) for x in selected)
   else:
    from lxml import etree
    selected=etree.HTML(text).xpath(loc);assert selected,f'XPath missing {loc}';target=' '.join(str(x) if isinstance(x,str) else etree.tostring(x,encoding='unicode') for x in selected)
  elif typ=='line_range':
   m=re.fullmatch(r'(\d+)(?:[-:](\d+))?',loc);assert m,f'Invalid line range {loc}';lo=int(m[1]);hi=int(m[2] or lo);lines=text.splitlines();assert 1<=lo<=hi<=len(lines);target='\n'.join(lines[lo-1:hi])
  elif typ=='pdf_page':
   import io
   from pypdf import PdfReader
   pages=PdfReader(io.BytesIO(b)).pages;m=re.fullmatch(r'(?:page\s*)?(\d+)',loc);assert m and 1<=int(m[1])<=len(pages),'PDF page locator';target=pages[int(m[1])-1].extract_text()
  elif typ not in ('full_document',):warnings.add(f'Manual locator review: {e["capture_id"]} {typ} {loc}')
  if e['excerpt']:
   norm=lambda s:' '.join(html.unescape(str(s)).split())
   excerpt=norm(e['excerpt']);candidates=[norm(target)]
   if 'html' in a['media_type']:
    from bs4 import BeautifulSoup
    candidates.append(norm(BeautifulSoup(target,'html.parser').get_text(' ',strip=True)))
   assert any(excerpt in t for t in candidates),f'Excerpt missing at {e["capture_id"]} {typ} {loc}: {excerpt[:100]}'
  elif typ=='full_document':warnings.add(f'Manual full-document evidence review: {e["capture_id"]}')
  return a
 for table in tables.values():
  for row in table.values():
   for k in ('effective_at','published_at','reported_as_of','observed_start','observed_end'):date_value(row.get(k))
   for e in row.get('evidence',[]):evcheck(e)
 for ent in entities.values():
  if ent['entity_type']=='account':assert ent['platform'] is not None,'Account platform missing'
 for c in content.values():
  if c['account_id']:fk(c['account_id'],entities);assert entities[c['account_id']]['entity_type']=='account'
  for id in c['owner_ids']:fk(id,entities)
  assert c['content_id']=='content:'+c['platform']+':'+hashlib.sha256(c['url'].encode()).hexdigest(),'Content canonical hash mismatch'
 seen_urls={}
 for c in content.values():
  key=(c['platform'],c['url']);assert key not in seen_urls or seen_urls[key]==c['content_id'],'Identity collision';seen_urls[key]=c['content_id']
 for r in relations.values():
  fk(r['from_id']);fk(r['to_id'])
  if r['predicate']=='owns_account':assert r['to_id'] in entities and entities[r['to_id']]['entity_type']=='account'
  if r['predicate'] in ('derived_from','repost_of','reply_to'):fk(r['from_id'],content);fk(r['to_id'],content)
  if r['predicate'] in ('edition_of','translation_of'):assert entities[r['from_id']]['entity_type']==entities[r['to_id']]['entity_type']=='book'
 for c in coverage.values():
  fk(c['subject_id'])
  for m in c['metric_ids']:assert m in metrics,f'Unknown coverage metric {m}'
  for id in c['capture_ids']:fk(id,captures)
  for s in c['search_log']:
   for id in s['capture_ids']:fk(id,captures)
  for a,b in [('requested_start','requested_end')]:
   assert (c[a] is None)==(c[b] is None),'Half window'
   if c[a]:assert c[a]==START and c[b]==END,'Coverage baseline drift'
  if c['status']=='complete_public_window':
   assert c['sampling_method']=='census' and c['pagination_exhausted'] is True and not c['known_gaps'] and c['capture_ids'],'Unsupported complete census'
   assert (c['requested_start'],c['requested_end'])==(START,END),'Complete census window'
   assert c['sampling_detail'],'Census boundary explanation missing'
 for table in ('observations','derived-metrics'):
  for o in tables[table].values():
   fk(o['subject_id']);assert o['metric_id'] in metrics,'Unknown metric';m=metrics[o['metric_id']];typ=subjects[o['subject_id']].get('entity_type','content')
   assert typ in m['allowed_subject_types'] and o['unit']==m['unit'],'Metric subject/unit mismatch'
   v=o['value'];q=o['qualifier'];lo=o['lower_bound'];hi=o['upper_bound'];sc=o['scope']
   if v is not None:assert ((m['value_type']=='number' and isinstance(v,(int,float)) and not isinstance(v,bool)) or (m['value_type']=='string' and isinstance(v,str)) or (m['value_type']=='boolean' and isinstance(v,bool))),'Metric value type'
   if q=='unknown':assert v is None and lo is None and hi is None and o['missing_reason'] and o['evidence_class']=='unavailable','Unknown qualifier invariant'
   else:
    assert o['missing_reason'] is None and o['evidence_class']!='unavailable','Known missingness invariant'
    if q in ('exact','rounded','approximate'):assert v is not None and lo is None and hi is None,'Value invariant'
    elif q=='lower_bound':assert v is not None and v==lo and hi is None,'Lower bound invariant'
    elif q=='upper_bound':assert v is not None and v==hi and lo is None,'Upper bound invariant'
    elif q=='range':assert v is None and lo is not None and hi is not None and lo<=hi,'Range invariant'
   for b in (v,lo,hi):
    if isinstance(b,(int,float)) and not isinstance(b,bool):
     if o['unit']=='fraction':assert 0<=b<=1,'Fraction out of bounds'
     if o['unit']=='percent' and o['metric_id']!='followers_growth_percent':assert 0<=b<=100,'Percent out of bounds'
     if not any(x in o['metric_id'] for x in ('change','growth','reuse_lag')):assert b>=0,'Negative count'
     if q=='exact' and o['unit'] in ('people','copies','ratings','reviews','items','comments','views','reposts','seats','subscriptions','interactions','downloads','rank') and m['formula_id'] is None:assert int(b)==b,'Fractional exact counter'
   for id in sc['book_ids']:fk(id,entities);assert entities[id]['entity_type']=='book'
   if o['metric_id'].startswith('book_'):
    assert sc['book_scope'] is not None and sc['book_format'] is not None,'Book scope missing'
    assert sc['notes'],'Book missing-scope explanation required'
   if o['metric_id']=='offer_price':assert sc['currency'] and sc['notes'],'Price terms missing'
   if o['metric_id']=='book_average_rating':assert sc['rating_scale_max'] is not None and sc['rating_scale_max']>0,'Rating scale missing'
   if o['metric_id']=='book_sales_rank':assert sc['marketplace'] and sc['notes'] and (sc['category'] or 'unknown' in sc['notes'].lower()),'Rank scope missing'
   if o['metric_id'] in ('book_publication_date','author_first_publication_date') and v is not None:
    assert re.fullmatch(r'\d{4}(?:-\d{2}(?:-\d{2})?)?',v),'Date shape';date_value({'value':v,'precision':{4:'year',7:'month',10:'day'}[len(v)]})
   if o['metric_id']=='book_publication_status' and v is not None:assert v in ('planned','early_access','published','retired','unknown')
   if o['metric_id']=='event_status' and v is not None:assert v in ('announced','scheduled','delivered','cancelled','unknown')
   if o['period_type']=='window':assert (o['period_start'],o['period_end'])==(START,END),'Observation baseline window'
   else:assert (o['period_start'] is None)==(o['period_end'] is None),'Half observation period'
   if o['coverage_id']:fk(o['coverage_id'],coverage)
   if table=='derived-metrics':
    assert o['worker_id']=='coordinator' and o['evidence_class']=='derived' and o['lineage'] and m['formula_id'],'Derived invariants'
    lin=o['lineage'];assert lin['formula_id']==m['formula_id'] and lin['script_sha256']==digest(configuration/lin['script_path']),'Derived formula/script drift'
    for key,col in [('observation_ids',observations),('content_ids',content),('relationship_ids',relations),('coverage_ids',coverage),('capture_ids',captures)]:
     for id in lin[key]:fk(id,col)
    assert o['observation_id'] not in lin['observation_ids'],'Self-referential lineage'
    if m['formula_id'] in ('original_posts_per_week','active_week_fraction','issues_per_week','kind_per_week'):assert lin['coverage_ids'] and all(coverage[x]['status']=='complete_public_window' for x in lin['coverage_ids']),'Rate without complete coverage'
    if o['metric_id']=='uploads_per_week':assert sc['content_kind']=='video_upload'
   else:assert o['lineage'] is None and o['evidence_class']!='derived','Collected lineage invariant'
   if o['evidence_class'] in ('direct_observation','first_party_report','third_party_report'):
    assert o['evidence'],'Accepted observation without evidence'
    supporting=[e for e in o['evidence'] if artifacts[(e['capture_id'],e['artifact_sha256'])]['representation']=='original_response' and captures[e['capture_id']]['status'] in ('complete','partial')]
    assert supporting,'Accepted observation without supporting archived original'
    for e in supporting:
     if e['locator_type']=='json_pointer':
      a=artifacts[(e['capture_id'],e['artifact_sha256'])];val=pointer(json.loads(artifact_bytes[a['sha256']]),e['locator'])
      if isinstance(val,(int,float)) and isinstance(v,(int,float)):assert val==v,'JSON counter/value mismatch'
    total['archive_backed_observations']+=1
   if o['evidence_class']=='unavailable':total['unavailable_observations']+=1
 total.update({k:len(v) for k,v in tables.items()});total['archive_objects']=len(artifact_bytes);total['manual_locator_warnings']=len(warnings)
 return tables,locations,dict(total),sorted(warnings)

def main():
 p=argparse.ArgumentParser();p.add_argument('path',nargs='?',type=pathlib.Path,default=Q);p.add_argument('--context',type=pathlib.Path);a=p.parse_args();roots=[a.path]
 if a.context and a.context!=a.path:roots.insert(0,a.context)
 try:
  _,_,stats,warnings=validate(roots,strict_sort=a.path==Q);print(json.dumps(stats,sort_keys=True))
  for w in warnings:print('REVIEW: '+w)
 except Exception as e:print(f'VALIDATION FAILED: {type(e).__name__}: {e}',file=sys.stderr);return 1
 return 0
if __name__=='__main__':sys.exit(main())
