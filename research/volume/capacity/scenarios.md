# Conditional operating scenarios

All assumptions are explicit in [scenario-inputs.json](scenario-inputs.json); calculations in [reproduce.py](reproduce.py). These are sensitivities, not forecasts. Production starts at a normalized 800,000 annual units; Q3 reported output was more than 200,000, so 800,000 is not the measured annual run rate. No probability is assigned.

| Case | Year | Existing output | New-project output | Potential output | Absorbable sales assumption | Incremental steady-state inventory ($m) |
|---|---:|---:|---:|---:|---:|---:|
| Existing-footprint ramp | 2027 | 920,000 | 0 | 920,000 | 920,000 | 325 |
| Existing-footprint ramp | 2028 | 1,030,400 | 0 | 1,030,400 | 1,030,400 | 625 |
| Existing-footprint ramp | 2029 | 1,133,440 | 0 | 1,133,440 | 1,133,440 | 904 |
| Expansion-supported | 2027 | 920,000 | 59,400 | 979,400 | 979,400 | 487 |
| Expansion-supported | 2028 | 1,030,400 | 168,300 | 1,198,700 | 1,198,700 | 1,081 |
| Expansion-supported | 2029 | 1,133,440 | 188,100 | 1,321,540 | 1,321,540 | 1,415 |
| Operational downside | 2027 | 785,455 | 12,000 | 797,455 | 797,455 | -7 |
| Operational downside | 2028 | 824,727 | 60,000 | 884,727 | 884,727 | 230 |
| Operational downside | 2029 | 865,964 | 84,000 | 949,964 | 949,964 | 407 |
| Demand/economic downside | 2027 | 920,000 | 59,400 | 979,400 | 930,430 | 354 |
| Demand/economic downside | 2028 | 1,030,400 | 168,300 | 1,198,700 | 1,078,830 | 756 |
| Demand/economic downside | 2029 | 1,133,440 | 188,100 | 1,321,540 | 1,123,309 | 877 |

Inventory assumes $22,000 carried cost and 45 days at the assumed sales rate. It excludes receivables, parts, payables, construction and liquidity buffers; it is not incremental cash borrowing. Do not add this steady-state stock requirement mechanically to unsold accumulation: they are alternative stock assumptions. In the demand case management would need to curtail production; potential output is not an expectation that all vehicles are produced.

The three buildouts are the Q3 announced cohort, modeled at 40,000 incremental annual capacity each. Six further integrations in 2027 are an analyst assumption, not company guidance. No additional 2028–29 projects are assumed. Ramp realization combines in-year availability and productive utilization; it is not measured utilization. No generic project contribution is counted inside the existing-site growth assumption.
