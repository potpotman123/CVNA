"""Conditional work-mix arithmetic, not calibrated Carvana paint headroom.
Run with Python 3; writes only the adjacent results file.
All numeric inputs are hypothetical. Units are normalized productive resource-hours.
Apply separately to painter labor, preparation labor, and booth occupancy, not their sum.
"""
import json
from pathlib import Path

def workload(easy_share, harder_to_easy_ratio):
    return easy_share + (1 - easy_share) * harder_to_easy_ratio

def calculate():
    initial_share, shifted_share, target = 0.5, 0.6, 1.2
    rows = []
    for ratio in (1.5, 2.0, 3.0):
        before = workload(initial_share, ratio)
        after = workload(shifted_share, ratio)
        needed_share = (ratio - before / target) / (ratio - 1)
        rows.append({
            "assumed_harder_to_easy_work_ratio": ratio,
            "initial_workload": before,
            "shifted_workload": after,
            "mix_only_output_growth_pct": 100 * (before / after - 1),
            "additional_productive_hours_for_20pct_growth_pct": 100 * (target * after / before - 1),
            "easy_share_required_for_20pct_mix_only_growth": needed_share,
            "required_share_change_percentage_points": 100 * (needed_share - initial_share),
            "hours_growth_to_restore_initial_mix_at_unchanged_output_pct": 100 * (before / after - 1),
            "output_decline_on_restoring_initial_mix_at_fixed_hours_pct": 100 * (1 - after / before),
        })
        assert abs(workload(needed_share, ratio) - before / target) < 1e-12
        assert abs(target * after / before * before / after - target) < 1e-12
    assert workload(0, 2) == 2 and workload(1, 2) == 1
    assert workload(0.5, 1) == workload(0.6, 1)
    return {
        "classification": "hypothetical conditional sensitivity; no empirical calibration",
        "assumptions": {
            "initial_easy_share": initial_share,
            "shifted_easy_share": shifted_share,
            "easy_workload_normalized": 1,
            "target_output_growth_pct": 20,
            "other_constraints": "assumed nonbinding; fixed quality and within-category workload",
            "paint_specific_warning": "neither shares nor ratios are measured at CVNA; use a separate ratio for each resource",
        },
        "rows": rows,
        "formula": "Q1/Q0 = (H1/H0) * h0/h1; h=f+(1-f)*r",
        "validation": "arithmetic identities and boundary checks only; no independent validation",
    }

if __name__ == "__main__":
    result = calculate()
    Path(__file__).with_name("mix-and-resource-results.json").write_text(json.dumps(result, indent=2) + "\n")
    for row in result["rows"]:
        print(f'r={row["assumed_harder_to_easy_work_ratio"]:g}: mix output +{row["mix_only_output_growth_pct"]:.1f}%; additional hours +{row["additional_productive_hours_for_20pct_growth_pct"]:.1f}%')
