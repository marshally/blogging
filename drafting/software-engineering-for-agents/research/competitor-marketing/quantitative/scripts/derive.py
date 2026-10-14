#!/usr/bin/env python3
"""Recompute registered metrics from canonical records; never fetch sources.
Output is deterministic for unchanged input and script, including retained UUIDv4
identities/timestamps. New results get UUIDv4 and calculation UTC timestamp.
No rates are emitted for incomplete coverage. Missing inputs remain separately
recorded unavailable observations, not invented derived zeros.
"""
import datetime as dt,hashlib,json,math,pathlib,statistics,sys,uuid
from collections import defaultdict
sys.dont_write_bytecode = True
from validate import Q,START,END,canonical,digest,read_tables,stamp,validate
KINDS={'original_posts_per_week':'original_post','uploads_per_week':'video_upload','podcast_episodes_per_week':'podcast_episode','articles_per_week':'article','reposts_per_week':'repost','replies_per_week':'reply','quote_posts_per_week':'quote_post','newsletter_issues_per_week':'newsletter_issue'}

def count_content(items):return len({x['content_id'] for x in items})
def original_posts_per_week(items,days):return count_content(items)/(days/7)
def active_week_fraction(items,start,end):
 bins=int((end-start).total_seconds()//604800)
 active={int((pub(x)-start).total_seconds()//604800) for x in items if pub(x) is not None and start<=pub(x)<start+dt.timedelta(weeks=bins)}
 return len(active)/bins if bins else None
def followers_change(earlier,later):return later-earlier
def followers_growth_percent(earlier,later):return 100*(later-earlier)/earlier if earlier else None
def median_metric(values):return statistics.median(values) if values else None
def p75_metric(values):
 if not values:return None
 s=sorted(values);i=(len(s)-1)*.75;lo=math.floor(i);hi=math.ceil(i);return s[lo]+(s[hi]-s[lo])*(i-lo)
def format_fraction(items,format):return sum(x['format']==format for x in items)/len(items) if items else None
def counter_change(earlier,later):return later-earlier
def issues_per_week(items,days):return count_content(items)/(days/7)
def kind_per_week(items,days):return count_content(items)/(days/7)
def derivative_count(relations):return len({r['from_id'] for r in relations})
def reuse_lag_days(original,derivative):
 a,b=original['published_at'],derivative['published_at']
 if not a or not b or a['precision'] not in ('day','second') or b['precision']!=a['precision']:return None
 return (pub(derivative)-pub(original)).total_seconds()/86400

def pub(c):
 t=c['published_at']
 if not t or t['precision'] not in ('day','second'):return None
 return stamp(t['value']+'T00:00:00Z' if t['precision']=='day' else t['value'])
def scope(**kw):
 d=dict(book_scope=None,book_ids=[],book_format=None,geography=None,marketplace=None,category=None,language=None,audience_type=None,content_kind=None,content_format=None,rating_scale_max=None,currency=None,notes=None);d.update(kw);return d

def derive():
 tables=read_tables(Q);entities={r['entity_id']:r for r in tables['entities']};contents={r['content_id']:r for r in tables['content']};observations=tables['observations'];coverage=tables['coverage'];relations=tables['relationships'];captures={r['capture_id']:r for r in tables['captures']};metrics={r['metric_id']:r for r in json.loads((Q/'metric-definitions.json').read_text())['metrics']}
 script_hash=digest(pathlib.Path(__file__));start,end=stamp(START),stamp(END);days=(end-start).total_seconds()/86400
 old={}
 def key(r):
  v=dict(r);v.pop('observation_id',None);v.pop('observed_at',None);return canonical(v)
 for r in tables['derived-metrics']:old[key(r)]=r
 result=[];created=dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
 def emit(subject,metric,value,cov=[],items=[],obs=[],rels=[],qualifier='exact',sc=None,note=None,period='window',dates=None):
  if value is None:return
  capids=set()
  for r in items+obs+rels:
   capids.update(e['capture_id'] for e in r['evidence'])
  for r in cov:capids.update(r['capture_ids'])
  ev=[];seen=set()
  for r in obs+rels:
   for e in r['evidence']:
    k=canonical(e)
    if k not in seen:ev.append(e);seen.add(k)
  r=dict(schema_version='1.0',run_id='quant-2026-10-14',worker_id='coordinator',observation_id=str(uuid.uuid4()),subject_id=subject,metric_id=metric,platform_metric_name=None,value=value,unit=metrics[metric]['unit'],qualifier=qualifier,lower_bound=value if qualifier=='lower_bound' else None,upper_bound=None,raw_value=None,observed_at=created,reported_as_of=None,period_type=period,period_start=START if period=='window' else (dates[0] if dates else None),period_end=END if period=='window' else (dates[1] if dates else None),scope=sc or scope(),evidence_class='derived',evidence=ev,coverage_id=cov[0]['coverage_id'] if len(cov)==1 else None,missing_reason=None,lineage=dict(formula_id=metrics[metric]['formula_id'],script_path='scripts/derive.py',script_sha256=script_hash,observation_ids=sorted(r['observation_id'] for r in obs),content_ids=sorted({r['content_id'] for r in items}),relationship_ids=sorted(r['relationship_id'] for r in rels),coverage_ids=sorted(r['coverage_id'] for r in cov),capture_ids=sorted(capids)),notes=note)
  result.append(old.get(key(r),r))
 # One source-family coverage record is a declared population, with deduplicated
 # canonical content. Qualifying content must actually cite its census captures.
 for cov in sorted(coverage,key=lambda x:x['coverage_id']):
  subject=cov['subject_id']
  if subject not in entities or entities[subject]['entity_type']!='account' or cov['requested_start']!=START:continue
  if not cov['content_kinds']:continue
  capset=set(cov['capture_ids'])
  items=[c for c in contents.values() if c['account_id']==subject and c['content_kind'] in cov['content_kinds'] and (not cov['content_formats'] or c['format'] in cov['content_formats']) and pub(c) is not None and start<=pub(c)<end and any(e['capture_id'] in capset for e in c['evidence'])]
  complete=cov['status']=='complete_public_window';qual='exact' if complete else 'lower_bound'
  for kind in cov['content_kinds']:
   selected=sorted([c for c in items if c['content_kind']==kind],key=lambda x:x['content_id'])
   # A blocked feed with no collected items does not supply an informative zero.
   if selected or complete:emit(subject,'observed_content_count',count_content(selected),cov=[cov],items=selected,qualifier=qual,sc=scope(content_kind=kind),note=f'Distinct observed {kind} records in declared coverage. '+('Complete available public window.' if complete else 'Coverage-qualified lower bound; missing history is unknown.'))
   if complete:
    for metric,target in KINDS.items():
     if target==kind:
      emit(subject,metric,kind_per_week(selected,days),cov=[cov],items=selected,sc=scope(content_kind=kind),note=f'{len(selected)} distinct {kind} records / ({days:g} days / 7); UTC baseline.')
    if kind=='original_post':emit(subject,'active_week_fraction',active_week_fraction(selected,start,end),cov=[cov],items=selected,sc=scope(content_kind=kind),note='Original posts in 12 complete seven-day bins anchored July 16 UTC; final six days excluded.')
   if selected:
    for fmt in sorted({c['format'] for c in selected}):emit(subject,'content_format_fraction',format_fraction(selected,fmt),cov=[cov],items=selected,sc=scope(content_kind=kind,content_format=fmt),note=f'Format fraction of collected {kind} population n={len(selected)}; coverage={cov["status"]}.')
    for fmt in sorted({c['format'] for c in selected}):
     group=[c for c in selected if c['format']==fmt];ids={c['content_id'] for c in group}
     for source,target in [('content_views','median_content_views'),('content_reactions','median_content_reactions'),('content_comments','median_content_comments'),('content_reposts','median_content_reposts')]:
      # Latest available snapshot per post, not multiple observations of same post.
      by={}
      for o in sorted(observations,key=lambda x:(x['observed_at'],x['observation_id'])):
       if o['subject_id'] in ids and o['metric_id']==source and o['qualifier']=='exact' and isinstance(o['value'],(int,float)):by[o['subject_id']]=o
      inputs=list(by.values())
      if not inputs:continue
      values=[o['value'] for o in inputs];ages=[(stamp(o['observed_at'])-pub(contents[o['subject_id']])).total_seconds()/86400 for o in inputs]
      note=f'Available {source}, n={len(inputs)} of {len(group)} collected {kind}/{fmt} items; coverage={cov["status"]}; post ages {min(ages):.2f}-{max(ages):.2f} days at retrieval. Current cumulative counters, not fixed-age performance; author comments included unless separately measured.'
      emit(subject,target,median_metric(values),cov=[cov],items=[contents[o['subject_id']] for o in inputs],obs=inputs,sc=scope(content_kind=kind,content_format=fmt),note=note)
      if source=='content_views' and len(inputs)>=4:emit(subject,'p75_content_views',p75_metric(values),cov=[cov],items=[contents[o['subject_id']] for o in inputs],obs=inputs,sc=scope(content_kind=kind,content_format=fmt),note=note+' Linear interpolation at (n-1)*0.75; minimum n=4 reporting rule.')
 # Comparable exact counter snapshots. Historical first-party reports require
 # reported_as_of; direct observations use actual read time. Under one day is
 # excluded to prevent incidental collection jitter masquerading as growth.
 groups=defaultdict(list)
 for o in observations:
  if o['metric_id'] in ('account_followers','book_rating_count','book_written_review_count') and o['qualifier']=='exact' and isinstance(o['value'],(int,float)):
   groups[(o['subject_id'],o['metric_id'],canonical(o['scope']),o['platform_metric_name'],o['evidence_class'])].append(o)
 for (subject,metric,_,_,cls),rows in sorted(groups.items(),key=lambda p:str(p[0])):
  def when(o):
   if cls=='direct_observation':return o['observed_at']
   t=o['reported_as_of'];return t['value'] if t and t['precision']=='second' else None
  rows=[o for o in rows if when(o)];rows.sort(key=when)
  if len(rows)<2:continue
  a,b=rows[0],rows[-1];elapsed=(stamp(when(b))-stamp(when(a))).total_seconds()/86400
  if elapsed<1:continue
  sc=dict(a['scope']);sc['notes']=(sc['notes'] or '')+f' Comparable snapshots separated by {elapsed:.6f} days.'
  targets=['followers_change','followers_growth_percent'] if metric=='account_followers' else [('book_rating_count_change' if metric=='book_rating_count' else 'book_written_review_count_change')]
  for target in targets:
   value=followers_growth_percent(a['value'],b['value']) if target=='followers_growth_percent' else counter_change(a['value'],b['value'])
   emit(subject,target,value,obs=[a,b],sc=sc,note=f'Later minus earlier comparable snapshots over {elapsed:.6f} days; no causal attribution.',period='unspecified',dates=[when(a),when(b)])
 grouped=defaultdict(list)
 for r in relations:
  if r['predicate']=='derived_from':grouped[r['to_id']].append(r)
 for original,rels in sorted(grouped.items()):
  emit(original,'verified_derivative_count',derivative_count(rels),rels=rels,items=[contents[original]]+[contents[r['from_id']] for r in rels],qualifier='lower_bound',note='Distinct explicitly linked observed derivatives; discovery may be incomplete.',period='unspecified')
  for r in rels:
   a,b=contents[original],contents[r['from_id']];lag=reuse_lag_days(a,b)
   if lag is not None:emit(b['content_id'],'reuse_lag_days',lag,items=[a,b],rels=[r],note='Publication difference using matching '+a['published_at']['precision']+' precision. Day-only sources produce calendar-day difference, not invented hours.',period='unspecified')
 out=Q/'derived-metrics.jsonl';out.write_text(''.join(canonical(r)+'\n' for r in sorted(result,key=lambda x:x['observation_id'])),encoding='utf-8')
 print(f'Wrote {len(result)} derived observations; script SHA256 {script_hash}')
if __name__=='__main__':derive()
