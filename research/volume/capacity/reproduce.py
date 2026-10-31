"""Reproduce bounded capacity research tables. Standard library only; no network.
Run: python3 research/volume/capacity/reproduce.py
Inputs are explicitly reported facts or hypothetical assumptions, not fitted estimates.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def dump(name, obj):
    (ROOT / name).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")

def make_register():
    cards = json.loads((ROOT / "adesa-site-cards.json").read_text())
    roster = json.loads((ROOT.parent / "adesa-21-site-candidate-roster.json").read_text())
    candidates = {r["site"]: r for r in roster["sites"]}
    candidates["ADESA Brasher's"] = candidates.pop("ADESA Brasher’s / Sacramento")
    overlaps = {
        "ADESA Houston": "First local IRC candidate; San Antonio and Blue Mound existed elsewhere in Texas. Houston was already a sales/delivery market.",
        "ADESA Chicago": "University Park original IRC south of Chicago; Hoffman Estates adds northwest-side production, not first Chicago coverage.",
        "ADESA Atlanta": "Winder original IRC northeast of Atlanta; Fairburn adds southwest-side capacity.",
        "ADESA Indianapolis": "Original IRC in Greenfield east of Indianapolis; Plainfield adds west-side capacity.",
        "ADESA Phoenix": "Tolleson original IRC west of Phoenix; Chandler adds southeast-side capacity.",
        "ADESA Dallas": "Blue Mound original IRC near Fort Worth; Hutchins adds southeast Dallas capacity.",
        "ADESA Charlotte": "Original Concord NC IRC northeast of Charlotte; ADESA Charlotte adds southwest-side capacity.",
        "ADESA Brasher's": "Rocklin original IRC already serves Sacramento area; Rio Linda adds capacity/another side of metro.",
        "ADESA New Jersey": "Delanco original IRC in southern NJ/Philadelphia catchment; Manville is farther north. State-level overlap does not establish same local coverage.",
        "ADESA Seattle": "First local IRC candidate; previously served market. Portland integration is regional rather than Seattle-local.",
        "ADESA Kansas City": "First local IRC candidate in reconstructed original network; same-day service announcement after integration provides delivery mechanism evidence.",
        "ADESA Sarasota": "Haines City original IRC in central Florida; Bradenton adds Gulf-coast proximity, with overlap depending on catchment.",
        "ADESA Orlando": "Original Haines City IRC in central Florida; Sanford adds northeastern metro capacity; post-Q3 announcement.",
        "ADESA Jacksonville": "Haines City was already a regional IRC; Jacksonville new-build project is not confirmed producing.",
        "ADESA San Antonio": "Separate original San Antonio IRC at Old Corpus Christi Highway; auction repair services alone do not establish retail integration.",
        "ADESA Birmingham": "Original Bessemer IRC already in greater Birmingham; ADESA property is in Moody.",
        "ADESA Memphis": "Original West Memphis IRC across state line in Arkansas.",
        "ADESA Salt Lake": "Original Tooele IRC southwest of Salt Lake City.",
        "ADESA Cincinnati/Dayton": "Original Trenton IRC in same broader Cincinnati-Dayton corridor.",
        "ADESA Cleveland": "Original Elyria/Lorain IRC west of Cleveland.",
        "ADESA Sacramento": "Distinct from ADESA Brasher's and original Rocklin IRC; do not merge these three sites.",
    }
    rows = []
    for card in cards:
        text = card["observed"]
        address = re.search(r"330 text ([^\n]+)", text)
        locality = re.search(r"331 text ([^\n]+)", text)
        url = re.search(r"333 link Description: More Info, Value: ([^\n]+)", text)
        assert address and locality and url, card["name"]
        town = locality.group(1).replace("\u00a0", " ").strip()
        # Preserve the observed address; do not silently correct map inconsistencies.
        row = {
            "name": card["name"], "address": address.group(1).strip() + ", " + town,
            "address_source": "https://www.adesa.com/map/#", "directory_detail_url": "https://" + url.group(1),
            "observed_date": "2026-10-29", "retail_integration_status_at_q3": "not confirmed in candidate roster; not proof of auction-only use",
            "facility_type": "ADESA auction property; retail status unconfirmed",
            "ownership_or_lease": None, "acquisition_date": None,
            "acquisition_note": "ADESA US acquired May 2022 as a portfolio; per-property title history not verified.",
            "announcement_date": None, "construction_start": None, "first_production_date": None, "ramp_completion": None,
            "infrastructure": "Auction property listed in ADESA directory; retail equipment/line configuration not independently established.",
            "capacity": {"theoretical": None, "installed": None, "staffed": None, "demonstrated": None},
            "expansion_potential": "Unquantified; building suitability, utilities, permits and local labor need site-specific verification.",
            "nearby_original_irc": overlaps.get(card["name"], "Not assessed beyond national original-IRC register; do not infer no nearby site."),
            "sources": ["https://www.adesa.com/map/#"],
            "quality": "Primary directory address; directory presence is not an operating census or retail-production confirmation.",
            "ambiguities": []
        }
        if card["name"] in candidates:
            c = candidates[card["name"]]
            row.update(facility_type="Integrated ADESA retail IRC candidate plus auction", retail_integration_status_at_q3="member of reconstructed 21-site candidate roster", announcement_date=c["evidence_date"], date_meaning=c["date_meaning"], infrastructure="Existing ADESA buildings adapted for retail reconditioning; exact site lines/equipment not disclosed in register.")
            row["sources"].append(c["source"])
            row["quality"] = "Company announcement plus primary address; named roster reconstructed, not company-certified."
            row["ambiguities"].append("Announcement date does not establish production start or full staffing. Generic 13,000 capacity/site must not be assigned as measured site capacity.")
            if card["name"] == "ADESA Buffalo":
                row["announcement_date"] = None
                row["first_production_date"] = "2024-04 (month only)"
        if card["name"] == "ADESA Portland":
            row["ambiguities"].append("Map says Portland; facility described as Wood Village. Preserve source address pending jurisdiction verification.")
        if card["name"] in ["ADESA New Jersey", "ADESA Concord"]:
            row["ambiguities"].append("Map omits leading zero in ZIP; raw value preserved.")
        if card["name"] == "ADESA Queen City":
            row["ambiguities"].append("Extra map entry contributes to 57 directory names versus 56 acquisition locations; current operating status unverified.")
        if card["name"] == "ADESA Orlando":
            row["announcement_date"] = "2026-10-06"
            row["date_meaning"] = "Post-Q3 retail integration announcement; operating start unknown."
            row["sources"].append("https://press.carvana.com/carvana-brings-inspection-and-reconditioning-center-capabilities-to-adesa-orlando/")
            row["facility_type"] = "ADESA retail integration announced after Q3; auction"
        if card["name"] == "ADESA Jacksonville":
            row.update(facility_type="ADESA auction plus retail IRC construction project", ownership_or_lease="Carvana identified as owner/developer in local plans reporting; title/lease audit not performed", infrastructure="89.32-acre property; existing wholesale buildings retained. January plan: 77,000 sf IRC and 6.9 acres staging. October permit: 74,400 sf metal building; total site improvement cost reported $32m.", construction_start="Unknown; site-work permit 2026-09-04; building permit 2026-10-21", expansion_potential="New IRC structure on existing property; local reported approval cost is not an audited all-in project budget.")
            row["sources"].append("https://www.jaxdailyrecord.com/news/2026/oct/21/carvanas-dinsmore-megasite-lands-more-approvals/")
            row["ambiguities"].append("Not confirmed as one of three Q3 company full buildouts; no verified output or start date. 77,000 vs 74,400 sf reflects different project descriptions.")
        rows.append(row)
    originals = json.loads((ROOT / "original-irc-inputs.json").read_text())
    for o in originals:
        rows.append({
            **o, "facility_type": "Original/non-ADESA IRC candidate", "observed_date": "2026-10-29",
            "ownership_or_lease": None, "acquisition_date": None, "announcement_date": o.get("announcement_date"),
            "construction_start": None, "first_production_date": o.get("first_production_date"), "ramp_completion": None,
            "infrastructure": o.get("infrastructure", "IRC function documented or corroborated; current line count, equipment and acreage unverified."),
            "capacity": {"theoretical": None, "installed": None, "staffed": None, "demonstrated": None},
            "expansion_potential": "Network staffing/shift expansion is a disclosed route; per-site headroom unquantified.",
            "nearby_original_irc": "See paired ADESA entries for overlap; no GIS distance estimate.",
            "ambiguities": ["Original/non-ADESA does not establish that the facility opened before the May 2022 acquisition. Current address corroboration is not a historical production record."]
        })
    result = {"as_of":"2026-10-29", "scope":"75 records: 57 directory entries and 18 reconstructed original IRCs; NOT 75 confirmed producing facilities", "limitations":["No company-certified named census", "57 map entries do not reconcile with 56 acquisition properties", "Individual capacity and title records largely unavailable", "No acreage-to-output conversion"], "facilities":rows}
    dump("facility-register.json", result)
    md = ["# Facility register", "", result["scope"], "", "Dates below are announcements/evidence dates, not starts unless stated. Null fields and full provenance are in [JSON](facility-register.json). Primary ADESA map observed 2026-10-29. Original addresses use official location pages, regulatory records or specifically labeled corroboration. Delivery hubs and vending machines are excluded from production counts.", ""]
    for title, group in [("Original / non-ADESA IRC candidates", rows[57:]), ("ADESA properties with Q3 retail-integration evidence", [r for r in rows[:57] if r["name"] in candidates]), ("Other ADESA directory entries", [r for r in rows[:57] if r["name"] not in candidates])]:
        md += ["## " + title,"","| Site | Physical address | Timeline / status |","|---|---|---|"]
        for r in group:
            status = r.get("first_production_date") or r.get("announcement_date") or "Not established"
            if r["name"] == "ADESA Jacksonville": status = "Construction approvals Sep–Oct 2026; production unverified"
            if r["name"] == "ADESA Queen City": status = "Directory/census discrepancy; current status unverified"
            md.append(f"| [{r['name']}]({r['sources'][0]}) | {r.get('address') or 'Not verified'} | {status} |")
        md += [""]
    md += ["## Infrastructure and geographic interpretation", "", "No site-level demonstrated, staffed or installed capacity was verified. Generic investment guidelines are retained at network level in the report, not imputed to each row. The JSON separately records paired original IRCs, source quality, construction evidence and unresolved dates.", "", "Jacksonville is the independently documented substantial build: existing auction buildings remain, with a new reconditioning structure. Other auction properties may already offer wholesale repair, logistics or last-mile services; those functions do not establish Carvana retail integration. Carvana's 2025 property table combines IRCs with hubs, vending machines, dealerships and auctions, so its acreage and square footage cannot be allocated to IRC capacity."]
    (ROOT / "facility-register.md").write_text("\n".join(md) + "\n")
    assert len(rows) == 75 and len(candidates) == 21

def scenarios():
    assumptions = json.loads((ROOT / "scenario-inputs.json").read_text())
    b = assumptions["annualized_normalization_units"]
    out = []
    for spec in assumptions["cases"]:
        existing = b
        for i, year in enumerate([2027, 2028, 2029]):
            existing *= 1 + spec["existing_resource_growth"][i]
            mix_adjusted = existing / spec["repair_hours_multiplier"][i]
            additions = 120000 * spec["three_buildouts_realization"][i] + 78000 * spec["six_integrations_realization"][i]
            p = mix_adjusted + additions
            sales = p * spec["demand_absorption"][i]
            wc = sales * assumptions["inventory_days"] / 365 * assumptions["inventory_cost_per_unit"]
            base_wc = b * assumptions["inventory_days"] / 365 * assumptions["inventory_cost_per_unit"]
            out.append({"case":spec["name"],"year":year,"existing_site_output":round(mix_adjusted),"new_project_output":round(additions),"potential_production":round(p),"hypothetical_absorbable_sales":round(sales),"unabsorbed_if_not_curtailed":round(p-sales),"incremental_steady_state_inventory_dollars":round(wc-base_wc)})
    checks = {
        "annual_sales_2025_growth":596641/416348-1,
        "q3_2026_sales_growth":217385/155941-1,
        "integration_capex_per_annual_capacity_unit_range":[2000000/13000,3000000/13000],
        "buildout_capex_per_annual_capacity_unit_range":[30000000/40000,35000000/40000],
        "three_buildouts_capacity":3*40000,"three_buildouts_capex_range":[90000000,105000000],
        "six_integrations_capacity":6*13000,"six_integrations_capex_range":[12000000,18000000],
        "inventory_per_100k_incremental_sales_45_days_22k":100000*45/365*22000,
        "inventory_per_100k_incremental_sales_60_days_22k":100000*60/365*22000,
        "extra_15_days_inventory_at_1m_sales_22k":1000000*15/365*22000,
        "q3_2026_operating_income_per_unit":714000000/217385,
        "q3_2025_operating_income_per_unit":552000000/155941,
        "q3_2026_operating_income_growth":714/552-1,
        "q3_2026_advertising_per_unit":152000000/217385,
        "q3_2025_advertising_per_unit":102000000/155941,
        "9m_2026_ocf_less_ppe":900000000-166000000,
        "9m_2025_ocf_less_ppe":606000000-96000000,
        "inventory_balance_change":3456000000-2408000000,
        "hypothetical_10pct_more_repair_hours_throughput_loss":1-1/1.1,
        "hypothetical_20pct_more_repair_hours_throughput_loss":1-1/1.2,
    }
    dump("scenario-results.json", {"warning":"Hypothetical operating conditions, not forecasts or estimates of actual utilization; baseline 800k is deliberately a normalization below disclosed Q3 annualized output.","scenarios":out,"arithmetic_checks":checks})
    lines=["# Conditional operating scenarios", "", "All assumptions are explicit in [scenario-inputs.json](scenario-inputs.json); calculations in [reproduce.py](reproduce.py). These are sensitivities, not forecasts. Production starts at a normalized 800,000 annual units; Q3 reported output was more than 200,000, so 800,000 is not the measured annual run rate. No probability is assigned.","","| Case | Year | Existing output | New-project output | Potential output | Absorbable sales assumption | Incremental steady-state inventory ($m) |","|---|---:|---:|---:|---:|---:|---:|"]
    for r in out:
        lines.append(f"| {r['case']} | {r['year']} | {r['existing_site_output']:,} | {r['new_project_output']:,} | {r['potential_production']:,} | {r['hypothetical_absorbable_sales']:,} | {r['incremental_steady_state_inventory_dollars']/1e6:,.0f} |")
    lines += ["","Inventory assumes $22,000 carried cost and 45 days at the assumed sales rate. It excludes receivables, parts, payables, construction and liquidity buffers; it is not incremental cash borrowing. Do not add this steady-state stock requirement mechanically to unsold accumulation: they are alternative stock assumptions. In the demand case management would need to curtail production; potential output is not an expectation that all vehicles are produced.","","The three buildouts are the Q3 announced cohort, modeled at 40,000 incremental annual capacity each. Six further integrations in 2027 are an analyst assumption, not company guidance. No additional 2028–29 projects are assumed. Ramp realization combines in-year availability and productive utilization; it is not measured utilization. No generic project contribution is counted inside the existing-site growth assumption."]
    (ROOT / "scenarios.md").write_text("\n".join(lines)+"\n")

if __name__ == "__main__":
    make_register()
    scenarios()
    print("Rebuilt facility register and scenario outputs; 75 records, 21 candidate Q3 integrations.")
