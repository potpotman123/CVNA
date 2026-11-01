"""One sequential Nominatim lookup per unmatched Census address; cache responses."""
import json,time,urllib.request,urllib.parse
from pathlib import Path
P=Path(__file__).resolve().parent/"geography"
prior=json.loads((P/"census-geocodes.json").read_text())
dest=P/"osm-fallback.json"
results=json.loads(dest.read_text()) if dest.exists() else []
done={x["name"] for x in results}
for x in prior:
    if x["matches"] or x["name"] in done: continue
    url="https://nominatim.openstreetmap.org/search?"+urllib.parse.urlencode(dict(q=x["query"],format="jsonv2",addressdetails=1,limit=3,countrycodes="us"))
    try:
        req=urllib.request.Request(url,headers={"User-Agent":"CVNA-Public-Research/1.0 (75-facility one-time location study)","Accept-Language":"en"})
        matches=json.loads(urllib.request.urlopen(req,timeout=30).read()); error=None
    except Exception as e: matches=[]; error=str(e)
    results.append(dict(name=x["name"],query=x["query"],url=url,matches=matches,error=error))
    dest.write_text(json.dumps(results,indent=2)+"\n")
    print(x["name"],len(matches),error,flush=True)
    time.sleep(1.1)
