"""Illustrative workload sensitivity; not measured capacity or a forecast."""
import json
from pathlib import Path
result = {"classification": "hypothetical sensitivity", "target_completed_vehicles_per_week": 1280,
          "paint_jobs_per_affected_vehicle_assumed": 1,
          "paint_incidence_cases": [{"incidence": p, "required_jobs_per_week": 1280*p} for p in (0.3,0.5,0.7)],
          "supported_output_gain_if_incidence_falls_70_to_50_percent": 0.7/0.5-1}
Path(__file__).with_name("headroom-pilot-calculations.json").write_text(json.dumps(result, indent=2)+"\n")
