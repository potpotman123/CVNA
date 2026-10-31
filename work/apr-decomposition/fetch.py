import urllib.request,gzip,hashlib,json,time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
p=Path('work/apr-decomposition')
items=[('2025-p2','000177037325000026','crvna25p2'),('2026-p2','000177037326000023','crvna26p2')]
def fetch(item):
 name,acc,stem=item; out=[]
 for ext in ['103','102']:
  url=f'https://www.sec.gov/Archives/edgar/data/1770373/{acc}/{stem}ex{ext}.xml';dest=p/(name+'-ex'+ext+'.xml.gz');h=hashlib.sha256();n=0
  try:
   req=urllib.request.Request(url,headers={'User-Agent':'Analyst Research analyst@example.com'})
   with urllib.request.urlopen(req,timeout=60) as src,gzip.open(dest,'wb') as target:
    while True:
     b=src.read(1024*1024)
     if not b:break
     n+=len(b)
     if n>170000000:raise RuntimeError('file size cap')
     h.update(b);target.write(b)
   row={'file':str(dest),'url':url,'bytes':n,'sha256':h.hexdigest()}
  except Exception as e:row={'url':url,'error':str(e)}
  out.append(row);print(json.dumps(row),flush=True)
 return out
with ThreadPoolExecutor(max_workers=2) as ex: rows=list(ex.map(fetch,items))
(p/'manifest.json').write_text(json.dumps(rows,indent=2))
