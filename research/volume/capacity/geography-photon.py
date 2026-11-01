import json,urllib.request,urllib.parse,time
from pathlib import Path
P=Path(__file__).resolve().parent/"geography"
rows=json.loads((P/"census-geocodes.json").read_text())
out=[]
for r in rows:
    if r["matches"] and r["name"]!="ADESA New Jersey":continue
    url="https://photon.komoot.io/api/?"+urllib.parse.urlencode(dict(q=r["query"],limit=3))
    try: data=json.loads(urllib.request.urlopen(url,timeout=15).read()); error=None
    except Exception as e:data={};error=str(e)
    out.append(dict(name=r["name"],query=r["query"],url=url,data=data,error=error))
    print(r["name"],[(v["properties"].get("name"),v["properties"].get("housenumber"),v["properties"].get("street"),v["geometry"]["coordinates"]) for v in data.get("features",[])],flush=True)
    (P/"photon-review.json").write_text(json.dumps(out,indent=2)+"\n")
    time.sleep(.5)
