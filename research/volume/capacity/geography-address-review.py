import json,urllib.request,urllib.parse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
P=Path(__file__).resolve().parent/"geography"
queries=[("Carvana West Memphis","1100 Family Dollar Pkwy, West Memphis, AR 72301"),("Carvana Indianapolis","6508 W F W Marks Dr, Greenfield, IN 46140"),("Carvana Indianapolis","6369 W 300 N, Greenfield, IN 46140"),("ADESA St. Louis","7858 US Highway 61, Barnhart, MO 63012")]
def run(pair):
    name,address=pair
    url="https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?"+urllib.parse.urlencode(dict(address=address,benchmark="Public_AR_Current",format="json"))
    try: data=json.loads(urllib.request.urlopen(url,timeout=40).read());error=None
    except Exception as e:data={};error=str(e)
    return dict(name=name,query=address,url=url,data=data,error=error)
with ThreadPoolExecutor(max_workers=4) as p: out=list(p.map(run,queries))
(P/"address-variants.json").write_text(json.dumps(out,indent=2)+"\n")
for r in out: print(r["name"],r["data"].get("result",{}).get("addressMatches",[]))
