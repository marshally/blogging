#!/usr/bin/env python3
"""Validate shards with shared foreign-key context, then merge without fact changes."""
import argparse,json,pathlib,shutil,sys
from validate import Q,TABLES,KEYS,canonical,validate

def main():
 p=argparse.ArgumentParser();p.add_argument('--check-only',action='store_true');a=p.parse_args()
 shards=sorted(x for x in (Q/'workers').iterdir() if x.is_dir()) if (Q/'workers').exists() else []
 # All shards are checked before the first root mutation. The combined context
 # permits explicit shared persons/publishers without duplicating their records.
 tables,locations,stats,warnings=validate([Q]+shards)
 if a.check_only:print(json.dumps(stats,sort_keys=True));return
 for cap in tables['captures'].values():
  for art in cap['artifacts']:
   src=locations[cap['capture_id']]/art['path'];dest=Q/art['path']
   if dest.exists():
    assert src.read_bytes()==dest.read_bytes(),'Hash collision or corrupt canonical object'
   else:dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dest)
 for name,rows in tables.items():
  path=Q/(name+'.jsonl');temporary=path.with_suffix('.tmp')
  temporary.write_text(''.join(canonical(rows[k])+'\n' for k in sorted(rows)),encoding='utf-8');temporary.replace(path)
 _,_,stats,warnings=validate([Q],strict_sort=True);print(json.dumps(stats,sort_keys=True))
 for w in warnings:print('REVIEW: '+w)
if __name__=='__main__':
 try:main()
 except Exception as e:print(f'MERGE FAILED: {type(e).__name__}: {e}',file=sys.stderr);sys.exit(1)
