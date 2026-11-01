"""Bounded public-data retrieval for the 75-record geographic comparison."""
import csv, io, json, re, urllib.request, urllib.parse, zipfile
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
ROOT = Path(__file__).resolve().parent
OUT = ROOT / "geography"
OUT.mkdir(exist_ok=True)
def get(url, timeout=60):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent":"CVNA-research-geography/1.0"}), timeout=timeout).read()
rows = json.loads((ROOT / "facility-register.json").read_text())["facilities"]
for x in rows:
    if x["name"] == "Carvana Delanco": x["address"] = "600 Creek Road, Delanco, NJ 08075"
    if x["name"] == "ADESA Concord": x["address"] = x["address"].replace("MA 1720", "MA 01720")
    if x["name"] == "ADESA New Jersey": x["address"] = x["address"].replace("NJ 8835", "NJ 08835")
if not (OUT / "city-points.json").exists():
    raw = get("https://download.geonames.org/export/dump/cities15000.zip")
    z = zipfile.ZipFile(io.BytesIO(raw))
    points=[]
    for line in z.read("cities15000.txt").decode().splitlines():
        f=line.split("\t")
        if f[8]=="US": points.append(dict(id=f[0],name=f[1],ascii=f[2],lat=float(f[4]),lon=float(f[5]),state=f[10],population=int(f[14]),modified=f[18]))
    (OUT / "city-points.json").write_text(json.dumps(points,indent=2)+"\n")
    print("City points retrieved",len(points),flush=True)
if not (OUT / "census-geocodes.json").exists():
    def geocode(x):
        url="https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?"+urllib.parse.urlencode(dict(address=x["address"],benchmark="Public_AR_Current",format="json"))
        try: matches=json.loads(get(url,45))["result"]["addressMatches"]; error=None
        except Exception as e: matches=[]; error=str(e)
        print(x["name"],len(matches),flush=True)
        return dict(name=x["name"],query=x["address"],url=url,matches=matches,error=error)
    with ThreadPoolExecutor(max_workers=4) as pool: results=list(pool.map(geocode,rows))
    (OUT / "census-geocodes.json").write_text(json.dumps(results,indent=2)+"\n")
    print("Address matches",sum(bool(r["matches"]) for r in results),"/",len(rows),flush=True)
(OUT / "facility-inputs.json").write_text(json.dumps(rows,indent=2)+"\n")
