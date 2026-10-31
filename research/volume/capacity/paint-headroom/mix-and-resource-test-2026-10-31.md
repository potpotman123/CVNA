# Vehicle mix versus executable resource expansion

As of October 31, 2026. Extends the [paint study](README.md), without recalibrating its hypothetical plant.

## Finding and model decision

The direction of the newer/lower-mileage workload advantage has independent peer support. Its magnitude, especially for paint rather than mechanical repairs, remains unknown. Carvana reports both execution recovery and deliberate selection of easier vehicles. Neither a pure software explanation nor a pure vehicle-mix explanation is identified by the evidence.

**New contribution:** a competitor cross-check, closer inspection of the measurement/skill-allocation problem, and a reproducible test of how large a mix change must be to explain output. The previously documented recovery and mix chronology is context, not newly discovered evidence. No current CVNA age distribution, paint-hours ratio, or staffing elasticity is estimated.

## Chronology and attribution

| Period | Reported observation | Interpretation and limits |
|---|---|---|
| Q4 2025 | Managers with less tenure and single-line sites were associated with higher recon costs. | Both management execution and small-site overhead can matter. A cost difference does not equal a paint-hour difference. |
| April 2026 | Network labor efficiency reportedly near its historical best; staffing/paint-flow tools under development and rollout. | Recovery is not proof of a new productivity frontier. No absolute hours or mix adjustment. |
| Q2 2026 | Management describes cost recovery, then renewed growth using newer vehicles, followed by planned mix broadening. Prime-focused rate reductions also affected purchases. | Workload selection and demand incentives jointly change mix. Sequence suggests multiple mechanisms but does not isolate them statistically. |
| June 2026 tour | Initial cost recovery attributed to execution; additional technology benefits prospective. | Do not attribute the entire recovery to new software. |
| Q3 2026 | Later-model/prime emphasis continued; cost efficiency and output improved, with production above 200,000 and slightly above sales. | Broadening back to the old mix was not demonstrated as complete. Management discussed leader development but supplied no training-cohort count. |

Provenance: supplied CapIQ files `work/earnings-calls/CVNA-Q4-2025.txt` lines 132–143, `CVNA-Q1-2026.txt` lines 86–92, `CVNA-Q2-2026.txt` lines 128–130, 164–170, 340–368 and 388–390; transcript manifest in the same directory. [Public Q2 transcript](https://www.roic.ai/quote/CVNA/transcripts/2026-year/2-quarter), Garcia replies to Haigian, Lick and Fong. [Public Q3 transcript](https://stockanalysis.com/stocks/cvna/transcripts/718716-q3-2026/), Jenkins replies to Fong/Zackfia and Garcia to Lick. These are company statements, not independent measurements. Q3 exact production remains unknown.

## Heat check: does newer mean easier?

**CarMax is a useful independent operator comparison.** On April 14, 2026, Tom Folliard said older, higher-mileage vehicles cost more and take longer to recondition at the same quality standard. He put ValueMAX at approximately 50% of inventory versus 15–20% ten to fifteen years earlier. These are inventory shares and a long-run comparison, not Carvana data or a recent causal experiment. No paint-specific hours or cost difference is disclosed. [CarMax FY2026 Q4 call](https://www.roic.ai/quote/KMX/transcripts/2026-year/4-quarter); supplied `KMX-Q4-FY2026.txt` lines 334–348.

This supports **age/mileage/condition → overall repair workload**, not **price itself → lower paint-hours**. An expensive vehicle can still have substantial panel damage. Need separate controls for age, mileage, initial condition, damage/panel count, model/finish, sourcing, quality standard and repair routing. A younger mix might mainly avoid mechanical work, leaving the paint constraint almost unchanged.

**Technical denominator check:** Mitchell's estimating guidance distinguishes refinishing new undamaged panels from repaired/used panels. Preparation operations can be excluded from quoted refinish times, and color blending can extend work onto adjacent panels. Therefore neither a panel count nor an estimating-guide time directly equals the actual hours needed to release a Carvana vehicle. This supports repair-category measurement; it provides no CVNA age coefficient. [Mitchell refinish procedure](https://static.mymitchell.com/static/webhelp/ppages/ceg/1033/Content/ceg022801.htm), repaired/used panels and blending sections.

Stephens' August follow-up generalizes toward higher-priced vehicles; UBS's July 30 note instead emphasizes a potential older-car GPU advantage. These are not inherently contradictory: lower processing burden and higher contribution per vehicle are different objectives. Local reports `work/sellside-expanded-2026-10-31/07.txt` PDF p2 and `30.txt` PDF p1; original metadata/hashes remain in that directory's manifest. No analyst estimate is promoted to observed economics.

## Staffing, workflow and parallelization

JPMorgan's June 5 Elyria report says task-assignment visibility was being added beyond mechanic clock-ins, with a skill matrix planned and overtime directed at constrained work centers. This is more specific than hiring counts: total attendance can coexist with a shortage at one qualified role. It is reported management testimony, not access to the underlying logs. `work/sellside-expanded-2026-10-31/29.txt`, PDF pp4–5, lines 205–217 and 270–283. Source text remains local.

| Route | Potential effect | Decisive observation | Cost/limit |
|---|---|---|---|
| Reallocate or cross-train current staff | More productive bottleneck hours from existing paid hours | Qualified staffing, idle reasons and accepted output at comparable repair mix | Training/supervision; withdrawing labor can create another constraint |
| Improve preparation/first-pass quality | Less resource time for the same repair | Category-level hours and repeat-work hours before/after | Quality cannot be relaxed to manufacture apparent productivity |
| Add painters or shifts | More available labor and potentially staffed booth-hours | Operational equipment available during proposed hours; matched shift output | Wages, overtime, managers, maintenance windows and recruitment |
| Add preparation stations/booths | More physical processing capacity | Station-specific queues and occupancy; completed installation | Capital/commissioning; serial paint-line topology matters |
| Select easier vehicles or change repair route | Lower workload on one stage | Incidence, severity and method mix | Acquisition prices, selection breadth; PDR itself requires qualified labor |

At a single binding resource, `Q = H / h`: productive hours H divided by workload per acceptable vehicle h. Model paint labor and booth occupancy separately. Adding staff only raises whole-site output if it increases H at a binding stage and downstream stages can absorb it. Workload must include repeat work and effort spent on vehicles subsequently removed from retail production.

## Conditional mix test

**All inputs below are assumptions, not estimates of Carvana.** Let easier vehicles require one normalized resource-hour and harder vehicles require r hours. Average workload is `h=f+(1-f)*r`, where f is the easier share. Assume the share rises from 50% to 60%, quality and category-specific execution stay constant, and other stages do not bind.

| Assumed harder/easier workload ratio | Output gain from that mix shift alone | Extra productive hours still needed for 20% output growth | Easier share needed for 20% growth from mix alone |
|---|---:|---:|---:|
| 1.5× | 4.2% | 15.2% | 91.7% |
| 2× | 7.1% | 12.0% | 75.0% |
| 3× | 11.1% | 8.0% | 66.7% |

Thus a modest mix change cannot explain an arbitrarily large increase in output. Conversely, material mix effects are possible if repair requirements differ substantially. Neither f nor r is disclosed sufficiently to select a row. **Higher sale prices do not identify either parameter.**

At r=2, returning from 60% to 50% easier vehicles needs 7.1% more productive hours merely to hold output constant; with fixed hours, output falls 6.7%. That is a conditional reversal test, not a prediction. Stage-specific ratios may differ; a mechanical-work saving cannot be transferred to booth-hours.

Reproduce with `python3 research/volume/capacity/paint-headroom/mix-and-resource-test.py`; results are in [JSON](mix-and-resource-results.json). Checks cover mix endpoints, equal-work invariance, target workload and combined growth identities. Arithmetic validation only; no fitted parameters or empirical validation.

## Economics and next decision

When paint is binding, compare incremental contribution **per constrained resource-hour**, not just GPU per vehicle. Contribution must include acquisition, repairs, delivery, selling costs and financing economics on a consistent basis. A harder vehicle is preferable in that simplified model only if its contribution advantage exceeds its relative use of the constrained resource; demand and other stages can overturn that ranking. Companywide GPU is not the contribution of a specific repair category.

The cleanest future test is whether reported labor efficiency persists while age/mileage mix broadens, with no offsetting rework, outsourcing or aging. A weaker test uses overall costs but must adjust for wages, parts, outsourcing, fuel and production-to-sale accounting lag. More expensive inventory can require more cash per unit even with fewer days in process. No working-capital saving is assumed.

Priorities: (1) mix shares and category-specific paint labor/occupancy; (2) qualified productive hours by stage/shift; (3) accepted releases and repeat-work rates; (4) contribution and acquisition funding by cohort. Existing public sources establish direction and mechanisms, not these inputs. No paid collection, outreach or bulk scraping was performed. Bounded peer, auction and technical-source discovery found no usable joint microdataset; a historical Manheim report link returned 404, and job/marketing cost claims were excluded. Raw licensed files remain local. Do not reopen generic searches without a concrete additional operating disclosure.
