"""Reproduce the historical recovery calculation; not a production forecast."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
source = json.loads((ROOT / "staffing-panel-data.json").read_text())
sites = []
for site in source["matched_panel"]:
    obs = {int(x["source_year"]): x for x in site["observations"]}
    hours = {str(y): int(obs[y]["total_hours_worked"]) for y in (2022, 2023, 2024, 2025)}
    employees = {str(y): int(obs[y]["annual_average_employees"]) for y in (2022, 2023, 2024, 2025)}
    target = max(hours["2022"], hours["2025"])
    sites.append({
        "site": site["site"], "establishment_id": site["establishment_id"],
        "annual_hours": hours, "annual_average_employees": employees,
        "historical_hours_target": target,
        "additional_hours": target - hours["2025"],
        "hours_growth_to_target": target / hours["2025"] - 1,
        "provisional_bin": "Original IRC below 2022 hours" if target > hours["2025"] else "Original IRC at or above 2022 hours",
    })
history = {str(y): {
    "hours": sum(s["annual_hours"][str(y)] for s in sites),
    "annual_average_employees": sum(s["annual_average_employees"][str(y)] for s in sites),
} for y in (2022, 2023, 2024, 2025)}
base = history["2025"]["hours"]
target = sum(s["historical_hours_target"] for s in sites)
growth = target / base - 1
assert len(sites) == 14 and len({s["establishment_id"] for s in sites}) == 14
assert target - base == sum(s["additional_hours"] for s in sites)
result = {
    "as_of": "2026-11-01",
    "source": "staffing-panel-data.json; original OSHA URLs and retrieval metadata in that file",
    "status": "Historical calculations and conditional arithmetic only; user stopped workbook/model creation.",
    "sites": sites, "matched_history": history,
    "recovery": {"baseline_2025_hours": base, "target_hours": target,
        "additional_hours": target-base, "growth": growth,
        "two_year_cagr_if_recovery_completed": (1+growth)**0.5-1,
        "three_year_cagr_if_recovery_completed": (1+growth)**(1/3)-1},
    "output_translation": {
        "formula": "additional production = starting production of these same 14 sites * recovery growth",
        "starting_production_for_14_sites": None,
        "additional_vehicles": None,
        "assumption": "Constant labor hours per acceptable completed vehicle; equipment, mix and downstream capacity permit proportional output.",
    },
    "rejected_companywide_shortcut": {
        "companywide_2025_retail_sales": 596641,
        "mechanical_increment": 596641*growth,
        "reason": "Wrong population and metric: 14-site hours growth applied to all-company retail sales. Not a forecast; do not add ADESA contributions to this number.",
    },
    "limitations": [
        "2025 annual hours are not current 2026 staffing or an exit run rate.",
        "Recovery may already have occurred in 2026; no additional two-year horizon from today is established.",
        "2022 hours are a historical benchmark, not an efficient staffing requirement or physical ceiling.",
        "Employer-reported establishment scope/address changes and support functions limit comparability.",
        "Timing of recovery is assumed, not measured; no future productivity improvement credited.",
    ],
}
(ROOT / "labor-recovery-calculations-2026-11-01.json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps({"sites": len(sites), "history": history, "recovery": result["recovery"]}, indent=2))
