# Working ramp for standard ADESA integrations

November 1, 2026. Supersedes the ungrounded 50%/80%/90% annual schedule proposed in chat. This is a benchmark-informed assumption, not a measured ADESA cohort fit. No workbook created.

## Evidence and adaptation

- Carvana's August 2026 presentation, slide 6: standard integrations add approximately 13,000 annual capacity for $2–3m; full buildouts add approximately 40,000 for $30–35m. Use 13,000 for light integrations only. https://investors.carvana.com/~/media/Files/C/Carvana-IR/reports-and-presentations/jp-morgan-auto-conf-aug-2026.pdf
- August 23, 2023 practitioner interview, published August 28: former Blue Mound director estimates 120 days as an aggressive realistic hiring interval for one line on one shift, explicitly clarifying the unit after confusion. First-line leadership recruiting and second-shift staffing are harder. Interviewer suggests roughly three years for a multi-line facility; respondent regards that as still aggressive. This is retrospective practitioner judgment, not a dated output panel or an ADESA observation. https://inpractise.com/articles/carvana-evolution-of-the-inspection-and-reconditioning-process
- Morgan Stanley June 10, 2026 report, local source `work/sellside-expanded-2026-10-31/31.txt`, PDF p4: larger IRC illustrative model assumes 35% year-one and 85% mature utilization. This is an analyst assumption for a different facility type, not historical validation. Keep licensed text local.
- Buffalo Business First March 30, 2026 accessible preview says Akron business 18 months earlier was one-tenth of current business. Undefined metric/no absolute units: directional multi-period ramp evidence only. https://www.bizjournals.com/buffalo/news/2026/03/30/carvana-ramps-up-hiring-in-akron.html

## Proposed working schedule

Hold mature annual output at 90% of the 13,000 guideline (11,700). The 90% allowance is analyst judgment for interruptions and uneven workload, not management guidance; the separate MS 85% mature assumption is a reasonableness reference only.

From first retail production, increase output linearly from zero to the mature rate over 12 months in the base case. Use 6 and 18 months as fast and slow cases. Twelve months allows more time than the aggressive four-month line-shift hiring benchmark for hiring, training and workflow stabilization. It is not a claim that an integration has three lines or takes exactly three staffing cycles. No measured ramp duration or optimal curve shape was recovered. The smaller standard integration need not follow a multi-line greenfield's roughly three-year staffing illustration.

These are first/second rolling 12-month periods after first production, not calendar years. Start dates must reflect operation where available; announcement dates are proxies when necessary. Prior recruiting may make the fast case appropriate. Do not add a second blanket utilization haircut after the 90% endpoint.

| Case | Months to mature rate | First 12 months | Second 12 months | Mature annual output |
|---|---:|---:|---:|---:|
| Fast | 6 | 8,775 | 11,700 | 11,700 |
| Base | 12 | 5,850 | 11,700 | 11,700 |
| Slow | 18 | 3,900 | 10,725 | 11,700 |

For five sites on the same age clock: base first-year production 29,250 and mature annual production 58,500; increase 29,250. Actual cohort calendar totals require individual dates. For existing integrations, subtract modeled baseline production rather than treating mature production as wholly incremental.

Reproduction: `python3 research/volume/capacity/adesa-ramp-benchmark-calculate.py`. Output is exact integration of the assumed linear rate, not independent validation. Sensitivity here isolates timing; separately changing the ultimate capacity or utilization would test a different uncertainty.

Decision: use this as a provisional ramp assumption in the discrete-bin build. Evidence grounds the operational time scale; judgment supplies the 6/12/18-month adaptation, linear shape and 90% endpoint. Replace with actual site-period output when available.
