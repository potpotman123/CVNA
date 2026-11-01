# Remaining ADESA integration pipeline and full-buildout upside

November 1, 2026. User authorized assigning standard 13,000 capacity and nine-month linear ramps to the remaining property pool, plus a separate full-buildout upside case. All results are modeled production/capacity, not observed sales. No workbook created.

## Coverage and opening schedule

The geographic inventory has 57 ADESA directory entries; Queen City remains excluded because status is unresolved. The resulting working 56-site population includes the 21 Q3 candidate integrations and 35 other properties. This numerical reconciliation is not independent confirmation of the acquired estate. All 35 names/addresses receive 13,000 standard capacity and assumed major-buildout eligibility in the output JSON. Suitability is assumed, not independently established.

Orlando is one of those 35, not a 36th property. Its October 6, 2026 announcement is used as a first-production proxy (not an observed startup date). That leaves 34 unassigned future integration slots. Slots begin in 2027, evenly spaced at six, seven or eight annually. The base uses seven; the final partial year retains the normal cadence. No unsupported named-site opening order is invented. Property-level inclusion and cohort-level timing are distinct.

Six-to-eight annual starts extrapolates management's 2026 guidance; it is our assumption for later years, not continuing company guidance. No further unannounced Q4 2026 openings are inserted. Each slot ramps linearly from zero to 13,000 annual rate over nine months, then stays at 100% as the user specified. Existing 21 production comes from the prior cohort calculation and is not counted again in the future pool.

## Base results: seven starts per year from 2027

| Year | New integrations in remaining pool | Remaining-pool production | Increase over prior year | All 56 standard-integration production |
|---|---:|---:|---:|---:|
| 2026 | 1, Orlando proxy | 485 | 485 | 213,709 |
| 2027 | 7 | 30,547 | 30,062 | 299,653 |
| 2028 | 7 | 115,375 | 84,828 | 388,375 |
| 2029 | 7 | 206,375 | 91,000 | 479,375 |
| 2030 | 7 | 297,375 | 91,000 | 570,375 |
| 2031 | 6 | 388,331 | 90,956 | 661,331 |
| 2032 | 0 | 450,534 | 62,203 | 723,534 |
| 2033 onward | 0 | 455,000 | 4,466 in 2033; zero thereafter | 728,000 |

The remaining pool ultimately adds 35 × 13,000 = 455,000 annual capacity. The original 21 contribute 273,000 at maturity, so all standard integrations total 728,000. The last base-case start occurs in 2031, finishes ramping in 2032, and 2033 is the first complete calendar year at the mature total. In 2027, this future pool adds 30,062 over its modeled 2026 output; combined with the existing-21 increase of 55,882, all ADESA standard integrations add approximately 85,944 over 2026. These are not additions to a Q3-exit annualized baseline.

| Future opening pace | Remaining-pool 2027 output | 2028 output | Last opening year |
|---|---:|---:|---:|
| 6 annually | 27,688 | 100,750 | 2032 |
| 7 annually | 30,547 | 115,375 | 2031 |
| 8 annually | 33,398 | 130,000 | 2031 |

At $2–3m each, all 35 standard projects imply $70–105m project budgets. Seven starts represent $14–21m of project budgets per cohort year. This is not a cash-capex schedule: construction may precede first production, Orlando spend may already be incurred, and acquisition, operating expense, working capital, logistics and maintenance are excluded.

## Full-buildout upside: show the denominator conflict, do not hide it

Verified August 2026 presentation explicitly labels full buildouts as approximately **40,000 incremental annual capacity**, alongside $30–35m per site. Therefore do not silently relabel it 40,000 total to force reconciliation.

| Capacity scenario | ADESA annual capacity | Interpretation |
|---|---:|---|
| All 56 standard integrations | 728,000 | Approved 13,000/site extrapolation |
| Management estate-level reference | Approximately 2,000,000 | Existing and potential ADESA operations; broader company property network approximately/over 3m |
| Every one of 56 sites gets 13,000 plus a further 40,000 | 2,968,000 | Mechanical all-sites additive upside; **not a verified ceiling or company guidance** |

Mechanical all-site full buildouts add 2,240,000 beyond the standard layer and imply $1.68–1.96bn in full-buildout project budgets, excluding the standard integrations and property acquisition. No dates are assigned: this is long-term optionality, not a timed production forecast. The already announced construction projects would be part of these 56, not added on top.

The mechanical 2.968m ADESA case exceeds the company's approximately 2m ADESA reference by 968,000. We have not established that every property can host the representative 40,000 increment. Possible explanations include site heterogeneity, selective buildouts or differences in the capacity baseline/scope; these remain hypotheses, not resolved facts.

For a management-aligned planning boundary, use approximately 2m ADESA / 3m broader network separately from the mechanical upside. Relative to 728,000 standard ADESA capacity, the 2m reference leaves approximately **1.272m additional annual capacity**, not another 2m on top. Do not add 728,000 or original-IRC capacity to the 3m whole-network reference again. None is a demand forecast or a proven engineering hard cap.

## Reproduction and validation

Run `python3 research/volume/capacity/adesa-future-pipeline.py`. It reads the sourced geography roster and prior existing-21 cohort output, and writes `adesa-future-pipeline-2026-11-01.json` containing all 35 property tags, finite anonymous start slots, annual production, project budgets and ceiling cases. There is no paid/raw licensed source text.

Checks: exactly 35 eligible properties; Orlando once; 34 further slots in each scenario; eventual remaining production 455,000 and combined standard output 728,000; no growth after all ramps finish. Timeline extends to 2034 so even the slower opening case has a full mature calendar year. Validation is arithmetic only, not independent site-output confirmation.

Sources checked November 1, 2026:
- Management integration/buildout capacity, cost and 2026 pace, slide 6: https://investors.carvana.com/~/media/Files/C/Carvana-IR/reports-and-presentations/jp-morgan-auto-conf-aug-2026.pdf
- Orlando October 6 announcement: https://press.carvana.com/carvana-brings-inspection-and-reconditioning-center-capabilities-to-adesa-orlando/ (body identifies Orlando; boilerplate mistakenly mentions Syracuse; source typo preserved as a caution).
- Acquisition-era estate reference, February 24, 2022: https://press.carvana.com/carvana-to-accelerate-growth-through-acquiring-adesa-u-s-physical-auction-business-from-kar-global/ (approximately 2m ADESA addition, over 3m company total).
- Q3 2026 network capacity reference and three 2027 construction projects: `sources.md`, S2 and local shareholder letter. The large Q2 introductory presentation could not be reopened through web access this turn; do not count it as newly verified.
- Approved ramp evidence: `adesa-peer-ramp-evidence-2026-11-01.md`.

Next work: combine this scheduled standard-integration layer with original-IRC production estimates; assign actual construction projects to a timed major-buildout layer only once their site identity and incremental scope are verified. The full-buildout ceiling here must not be summed with a separate project layer without removing overlapping increments.
