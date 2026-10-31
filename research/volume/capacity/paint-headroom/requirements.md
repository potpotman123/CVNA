# Reproducible results — all scenarios illustrative

No Carvana site utilization or forecast is estimated. Run `python3 model.py` to reproduce.

## Growth requirements

| Target output growth | Required workload reduction at fixed hours | Current availability must be at most, if achievable target is 85% | Elyria 1,280/week reference target |
|---|---:|---:|---:|
| 10% | 9.1% | 77.3% | 1,408 |
| 20% | 16.7% | 70.8% | 1,536 |
| 30% | 23.1% | 65.4% | 1,664 |

The 85% target is assumed. Elyria targets are arithmetic requirements, not expected output.

## Constructed plant: resource bottlenecks

| Case | Supported units/week | Change | Binding resource | Added weekly labor cost* |
|---|---:|---:|---|---:|
| reference | 400.0 | +0.0% | booth_occupancy | $0 |
| A_allocation_quality | 460.0 | +15.0% | other_release | $0 |
| B_shift_extension | 460.0 | +15.0% | other_release | $6,651 |
| C_older_mix | 303.2 | -24.2% | booth_occupancy | $0 |
| D_equipment_only | 440.0 | +10.0% | paint_labor | $0 |
| E_coordinated_expansion | 520.0 | +30.0% | booth_occupancy | $7,981 |

*Labor-only at assumed wages and 80% productive share of paid incremental hours; excludes materials, training, capex, facilities and nonpaint costs. Zero does not mean zero implementation cost.

## Rework requirements

| Additional rework hours / first-pass work: before → after | Stage output gain |
|---|---:|
| 10% → 0% | 10.0% |
| 10% → 5% | 4.8% |
| 25% → 10% | 13.6% |
| 40% → 10% | 27.3% |

## Capital screen

| Net incremental contribution / sold vehicle | Annual incremental contribution | Extra inventory | Maximum equipment + training capital* |
|---|---:|---:|---:|
| $100 | $500,000 | $3,013,699 | $-513,699 |
| $250 | $1,250,000 | $3,013,699 | $3,236,301 |
| $500 | $2,500,000 | $3,013,699 | $9,486,301 |

*100 additional weekly sales × 50 operating weeks, 10 calendar inventory days, $22k carrying value, 20% pretax cash return hurdle, all assumed. Not a project cost estimate or DCF; deduct other incremental capital and account separately for taxes, depreciation, maintenance and ramp losses.
