"""Recompute distances and summaries from cached public-source coordinates."""
import json,math,statistics,csv
from pathlib import Path
ROOT=Path(__file__).resolve().parent
P=ROOT/"geography"
cfg=json.loads((ROOT/"geography-config.json").read_text())
fac=json.loads((P/"facility-inputs.json").read_text())
census={x["name"]:x for x in json.loads((P/"census-geocodes.json").read_text())}
osm={x["name"]:x for x in json.loads((P/"osm-fallback.json").read_text())}
extra={x["name"]:x for x in json.loads((P/"osm-business.json").read_text())} if (P/"osm-business.json").exists() else {}
manual=json.loads((P/"coordinate-review.json").read_text()) if (P/"coordinate-review.json").exists() else {}
citylist=json.loads((P/"city-points.json").read_text())
def point(key):
    name,state=key.split(",")
    matches=[x for x in citylist if x["name"]==name and x["state"]==state]
    assert len(matches)==1,(key,len(matches))
    return matches[0]
def miles(lat,lon,lat2,lon2):
    a,b,c,d=map(math.radians,(lat,lon,lat2,lon2))
    h=math.sin((c-a)/2)**2+math.cos(a)*math.cos(c)*math.sin((d-b)/2)**2
    return 3958.7613*2*math.asin(min(1,math.sqrt(h)))
rows=[]
for f in fac:
    name=f["name"]; original=name.startswith("Carvana ")
    key=cfg["original_cities" if original else "adesa_cities"][name.removeprefix("Carvana " if original else "ADESA ")]
    city=point(key)
    group="Original IRC" if original else ("Integrated ADESA" if "member of reconstructed" in f.get("retail_integration_status_at_q3","") else "Other ADESA")
    lat=lon=None; quality="unmatched"; source=""; matched=""
    cm=census[name]["matches"]
    if len(cm)==1:
        m=cm[0]; lat=m["coordinates"]["y"]; lon=m["coordinates"]["x"]; quality="Census address-range"; source=census[name]["url"]; matched=m["matchedAddress"]
    else:
        o=extra.get(name,osm.get(name,{})); matches=o.get("matches",[])
        if len(matches)==1:
            m=matches[0]; lat=float(m["lat"]); lon=float(m["lon"]); source=o["url"]; matched=m["display_name"]
            quality="OSM address/site" if m.get("address",{}).get("house_number") or m.get("category") in ("building","shop","industrial","office","amenity","landuse") else "OSM road approximation"
    if name in manual:
        m=manual[name]; lat=m["lat"]; lon=m["lon"]; quality=m["quality"]; source=m["source"]; matched=m["note"]
    distance=miles(lat,lon,city["lat"],city["lon"]) if lat is not None else None
    alternatives=[dict(city=k,miles=miles(lat,lon,point(k)["lat"],point(k)["lon"]) if lat is not None else None) for k in cfg["alternatives"].get(name,[])]
    rows.append(dict(name=name,address=f["address"],group=group,lat=lat,lon=lon,quality=quality,matched_address=matched,coordinate_source=source,city=key,city_lat=city["lat"],city_lon=city["lon"],geonames_id=city["id"],city_source="https://www.geonames.org/"+city["id"]+"/",miles=distance,alternatives=alternatives,city_assignment_ambiguous=name in cfg["alternatives"],excluded=name in cfg["exclude_from_primary_statistics"],status_note=f.get("retail_integration_status_at_q3","Original IRC")))
def summary(rs):
    vals=[r["miles"] for r in rs if r["miles"] is not None]
    return dict(roster_count=len(rs),located_count=len(vals),median=statistics.median(vals) if vals else None,mean=statistics.mean(vals) if vals else None,within10=sum(x<=10 for x in vals)/len(vals) if vals else None,within25=sum(x<=25 for x in vals)/len(vals) if vals else None,within50=sum(x<=50 for x in vals)/len(vals) if vals else None)
groups=["Original IRC","Integrated ADESA","Other ADESA","All ADESA"]
summaries={}
for title,eligible in [("located_including_road_proxies",lambda r:not r["excluded"]),("strict_address_matches",lambda r:not r["excluded"] and "approximation" not in r["quality"]),("exclude_ambiguous_cities",lambda r:not r["excluded"] and not r["city_assignment_ambiguous"]),("all_directory_records",lambda r:True)]:
    summaries[title]={g:summary([r for r in rows if eligible(r) and (r["group"]==g or g=="All ADESA" and r["group"]!="Original IRC")]) for g in groups}
pairs=[]
for city in sorted({r["city"] for r in rows}):
    originals=[r for r in rows if r["city"]==city and r["group"]=="Original IRC" and r["miles"] is not None]
    adesas=[r for r in rows if r["city"]==city and r["group"]!="Original IRC" and not r["excluded"] and r["miles"] is not None]
    if originals and adesas:
        old=min(originals,key=lambda r:r["miles"])
        for new in adesas:
            pairs.append(dict(city=city,original=old["name"],adesa=new["name"],group=new["group"],original_miles=old["miles"],adesa_miles=new["miles"],reduction_miles=old["miles"]-new["miles"],original_quality=old["quality"],adesa_quality=new["quality"]))
result=dict(as_of=cfg["as_of"],cutoff=cfg["classification_cutoff"],method=cfg["method"],rows=rows,summaries=summaries,same_city_pairs=pairs)
(P/"comparison.json").write_text(json.dumps(result,indent=2)+"\n")
with (P/"facility-distances.csv").open("w") as out:
    keys=[k for k in rows[0] if k!="alternatives"]
    writer=csv.DictWriter(out,keys);writer.writeheader();writer.writerows({k:r[k] for k in keys} for r in rows)
template=(ROOT/"geography-map-template.html").read_text()
geo=json.loads((P/"us-states.geojson").read_text())
(P/"map.html").write_text(template.replace("__DATA__",json.dumps(result)).replace("__GEO__",json.dumps(geo)))
print(json.dumps(summaries,indent=2)); print("PAIRS",json.dumps(pairs,indent=2)); print("UNMATCHED",[r["name"] for r in rows if r["miles"] is None])
