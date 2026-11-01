# Labor-hours recovery: calculations and agreed next build

Status: workbook/model creation stopped at the user's request. This note preserves the data, arithmetic, corrections and intended framework. No new volume forecast has been completed.

## What is measured

The [OSHA staffing panel](staffing-panel-data.json) contains 14 matched original IRC establishments, 2022–2025. It includes source URLs, retrieval metadata, employee counts, hours and establishment addresses. [Existing methodology and limitations](staffing-test-results-2026-10-30.md) remain applicable, including address/scope changes and employer-reported data. Hours include establishment functions, not necessarily only direct recon work.

| Year | Annual average employees | Annual hours |
|---|---:|---:|
| 2022 | 7,212 | 13,020,405 |
| 2023 | 4,356 | 7,410,179 |
| 2024 | 5,048 | 7,244,948 |
| 2025 | 6,806 | 12,684,358 |

For each site, take **max(2022 hours, 2025 hours)**. This restores sites below their own historical hours without shrinking sites that have grown beyond them. Summed target: **14,812,246 hours**, an increase of **2,127,888 / 16.7757%** over 2025. This is not the change between aggregate 2022 and aggregate 2025 hours.

The [calculation output](labor-recovery-calculations-2026-11-01.json) preserves every site's inputs, gap and provisional classification. Reproduce with `python3 research/volume/capacity/labor-recovery-calculations.py` from the repository root. No raw downloads or licensed report text are needed for this calculation.

## Agreed simplifying assumption

User approved constant labor hours per completed vehicle: 10% more total hours supports 10% more acceptable production. This gives no credit for future productivity gains. It remains conditional on stable repair mix, sufficiently skilled labor, equipment and downstream capacity; extra paid/worked hours alone do not guarantee output.

The identity is production = employees × hours per employee ÷ hours per completed vehicle. Neither the historical hours-per-employee series nor management's discussion supports assuming each factor is constant as an empirical fact.

Historical evidence against a fixed headcount/output ratio:
- D.A. Davidson, November 16, 2025, Haines City tour: output growth exceeded labor growth due to operating improvements and leverage. No matched before/after counts supplied. Local licensed source: `work/sellside-expanded-2026-10-31/20.txt`, lines 29–38. Keep report text local.
- Q1 2026 earnings call: labor hours per unit worsened in Q4 2025, then recovered toward the prior Q2 2025 best. Local source: `work/earnings-calls/CVNA-Q1-2026.txt`, around lines 399–403. Recovery is not necessarily a new productivity record.

## Conditional arithmetic, not forecasts

- Closing the entire historical hours gap over two years implies **8.0628% annualized growth** for this sample; over three years, **5.3054%**. The historical endpoint is evidenced; completion and timing are assumed.
- Additional vehicles = **starting production of those same 14 sites × 16.7757%**. That starting production is unknown, so an actual vehicle increment remains uncalculated.
- Earlier headcount requirements for a hypothetical 20% production increase used an 18-original-IRC 2025 employee total of 7,977: 7,977 × (1.20 / (1 + productivity gain) − 1). At 0%, 5%, and 10% productivity improvement, the rounded additional annual-average employees are 1,595, 1,140, and 725. These were conditional arithmetic, not hiring forecasts, and also held hours per employee constant. They do not use the same 14-site population as the recovery calculation.
- **Correction to the conversation:** multiplying 596,641 companywide 2025 retail sales by 16.7757% produces about 100,091 vehicles, but mixes populations and production with sales. It is not a valid original-IRC output estimate. Do not add ADESA growth to that shortcut. The earlier ~148,400 cumulative two-year incremental-sales illustration shares this defect and is withdrawn as a forecast.

## Timing

2025 OSHA hours describe calendar 2025, although filed during 2026. OSHA collects annual data for the preceding calendar year; 2026 reporting is due in early 2027 under the annual March 2 schedule, with public availability potentially later. [OSHA data users guide](https://www.osha.gov/sites/default/files/ITA_data_users_guide.pdf).

User accepted a crude 2025 baseline. A two-year recovery from that baseline refers to **2026–2027**, not another two years beginning after Q3 2026. Some recovery may already have happened. Any later forecast must account for that rather than reuse the whole gap.

## Intended segmentation for future work

| Group | Proposed driver | Treatment now |
|---|---|---|
| Original IRCs below historical hours | Site-specific gap closure | Historical inputs and gap calculated |
| Original IRCs at/above historical hours | Supported shifts, staffing or expansion | No automatic further growth assumed |
| Other original IRCs without matched history | Separate site evidence | Do not silently apply the 14-site gap |
| ADESA integrations already operating at baseline | Ramp from estimated starting output | Requires explicitly labeled allocation/ramp assumptions |
| Later integrations and major buildouts | Opening dates, incremental capacity and ramp | Separate additions; avoid counting replacement/expanded capacity twice |

Calculate sites individually, then aggregate by group. Maturity guides near-term ramp; usable recon building area and equipment constrain eventual capacity. Do not translate total land, parking or auction building area directly into output. Square footage is a possible cross-check or explicitly assumed comparable-site scaling factor, not an observed production function.

Available inputs already in Git:
- [Facility register](facility-register.json): originals, candidate integrations, auction properties, addresses, provenance and unknown capacity fields. Not every record is a producing IRC.
- [Original IRC inputs](original-irc-inputs.json): 18 reconstructed original locations.
- [ADESA candidate roster](../adesa-21-site-candidate-roster.json): six 2024, ten 2025, five through Q3 2026 announcements/operating leads. Dates have different meanings; announcement is not necessarily startup. Orlando is a separate post-Q3 lead.
- [Operating timeline](operating-timeline.md), [sources](sources.md), [ramp evidence](ramp-evidence-2026-10-30.md), [headroom pilot](headroom-pilot-2026-10-31.md), [equipment follow-up](equipment-followup-2026-10-31.md).
- Elyria's June 2026 ~1,280 vehicles/week, four lines and two shifts is a tour observation, not a network-wide per-site assumption. Existing infrastructure examples include Greenfield paint equipment, Trenton booths/lifts and Dayton proposed building area; historical design and proposals are not current output.
- Prior scenario files contain hypothetical growth rates. They are not the newly agreed labor-gap approach and have not been changed or validated by this work.

## What is still needed before a segmented forecast

1. A clearly labeled allocation of starting production between originals and ADESA cohorts; actual site-level counts remain unavailable.
2. Ramp assumptions for ADESA sites, tied where possible to dates and equipment rather than arbitrary utilization percentages.
3. Distinguish gross capacity of a full buildout from incremental capacity replacing an existing integration.
4. Keep production separate from sales absorption and inventory changes. This exercise does not establish profitability of incremental sales.

No further data search or workbook construction is authorized by the stop instruction. Next action requires the user's direction; this handoff prevents repeated framework discussions and preserves the corrections.

## November 1 continuation — user authorized ADESA cohort calculation

The earlier stop on further calculation was superseded by the user's instruction to apply the accepted nine-month ramp and move to the next bin. [ADESA cohort bridge](adesa-cohort-build-2026-11-01.md) now supplies per-site proxy start dates and 2026–2028 output. The five Q3 ramping sites add approximately 49,407 modeled vehicles in 2027 over 2026; the 16 Q3 mature sites add 6,475 from calendar carryover. No new workbook has been created. Further mature-site expansion is kept separate from these standard integration ramps.

## Completed combined volume scenario

The user's subsequent instruction to finish the bins authorizes the [combined volume build](volume-bridge-2026-11-01.md). It now includes original-site residual output allocations, remaining standard integrations and assumed 2030+ major buildouts. Half-completed historical recovery and 5% later original-site hours growth are explicitly assumed, not observed. Production reaches roughly 1.49 million in 2030 and 2.21 million in 2035 under the specified schedule; sales absorption and profitability are still unproven. Costs are deferred, with project budgets and unknown remaining-spend fields retained for the next phase. This supersedes the earlier statement that no segmented calculation was authorized.

## Revised volume assumptions — latest user instruction

The combined volume build now removes the unsupported 5% annual labor growth completely, retaining only conditional historical labor recovery. It schedules three full-buildout starts annually in every year 2027–2035, including 2028–2029. Revised 2035 production is 2,350,632; eventual fully ramped output from these same projects is 2,500,632 with other bins unchanged. These supersede the earlier combined-scenario totals above. No additional sales absorption or profitability evidence is implied.
