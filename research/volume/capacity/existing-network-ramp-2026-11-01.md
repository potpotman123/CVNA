# Existing IRC staffing expansion: replace the historical-hours flatline

November 1, 2026. Working scenario, not a validated base forecast. The prior volume bridge and financial model remain unchanged. Reproduce with `python3 research/volume/capacity/existing-network-ramp-2026-11-01.py`; assumptions, monthly method, comparisons and provenance are in the adjacent JSON.

## Finding

The old bridge restores lagging sites to their 2022 hours, then freezes all original IRC output around 693k. Historical hours are a reference, not physical capacity. The comparator is the pandemic-era 2022 expansion, not pre-pandemic staffing. Keeping the plateau as the sole central forecast excludes a mechanism management explicitly intends to use: continued staffing of existing facilities.

Company presentation slide 16 assigns **over 1m potential annual units to the 18 original IRCs**, plus 2m from ADESA at full buildout. Use 1m as a conservative modeling boundary, not a measured engineering ceiling or guaranteed output. The August presentation separately identifies staffing existing sites, standard integrations and major buildouts. Its no-capex staffing description does not eliminate working capital, training, logistics or customer-care costs.

Sources: [July introduction, slide 16](https://investors.carvana.com/~/media/Files/C/Carvana-IR/documents/IR_Intro-to-Carvana_Q2_2026.pdf); [August operating plan, slide 6](https://investors.carvana.com/~/media/Files/C/Carvana-IR/reports-and-presentations/jp-morgan-auto-conf-aug-2026.pdf).

## What the tours establish

- **Haines City, November 2025:** D.A. Davidson describes adding a fifth physical line versus four in March, and ramping a second shift. That supports expansion through both equipment and staffing. It does not establish a measured doubling of whole-site completed production. Exclude the report's implausible 12,800/week capacity figure. MS's 40% figure measures parking occupancy, not production utilization.
- **Elyria, June 2026:** Citizens reports approximately 1,280 completed vehicles/week across four physical lines working two shifts. That is 64–67k annualized at 50–52 weeks, not an observed full-year total. JPM's roughly 1,300/week capacity description comes from the same tour. Do not count eight physical lines and then multiply by two shifts again.
- Both observations precede our Q3 anchor. Their achieved increases cannot be added afresh. They demonstrate an operating route, not its remaining nationwide magnitude. Tour selection favors showcase sites.

Local licensed-source locators are recorded in the JSON; full reports are not redistributed. See [prior headroom review](headroom-pilot-2026-10-31.md) for equipment, bottleneck and permit-access limitations.

## Model specification

At facility level, supported output depends on the least-capable production stage: inspection, mechanical work, body/paint, parts availability and final release. Staffed hours divided by hours per completed vehicle approximates output only while equipment and other stages can support it. Extra shifts and headcount contribute to the same effective-hours driver; they are not separate multipliers.

We lack consistent site-level shift, skill, equipment and completed-output observations. A portfolio model is therefore more honest than inventing 18 detailed ramps:

`Original output rate(t) = min(cap, Q3 original output proxy × (1 + effective-hours growth)^t × (1 + productivity growth)^t)`

Effective hours are available productive labor after training, absence and skill constraints. They can grow through hiring, retention and additional staffed shifts. Hiring must lead productive output. No numerical training lag is estimated in this pass.

Starting original output is the existing model's residual **648,714 annualized units**: company Q3 sales annualized less modeled ADESA output. It is not disclosed original-site production. Take Q3's midpoint as the time anchor; annual outputs average monthly midpoint rates, so calendar production is not an exit run rate. No seasonality is modeled.

**Working case:** 10% annual effective-hours growth, zero productivity growth, capped at 1m originals. The 10% is an explicit analyst scenario, not management guidance, an estimate derived from the tours or a rate fitted to consensus. Test 5% and 15%, plus 2% productivity and a lower 900k effective operating cap. The new path replaces historical recovery; do not add the old recovery increment on top. All ADESA cohorts and project schedules remain unchanged.

## Results: retail units, thousands

| Calendar year | Old bridge | 5% hours | 10% hours | 15% hours | Supplied consensus | 10% case vs consensus |
|---|---:|---:|---:|---:|---:|---:|
| 2027 | 982 | 988 | 1,017 | 1,045 | 1,040 | -2.3% |
| 2028 | 1,172 | 1,190 | 1,255 | 1,323 | 1,228 | +2.2% |
| 2029 | 1,382 | 1,436 | 1,543 | 1,654 | 1,462 | +5.6% |
| 2030 | 1,593 | 1,684 | 1,839 | 1,900 | — | — |
| 2035 | 2,351 | 2,652 | 2,658 | 2,658 | — | — |

The central original-site path is 705k / 776k / 854k / 939k in 2027–2030, approximately 999k in 2031. It assumes about 54% eventual growth from the Q3 original-site proxy, not a doubling. A 900k effective cap lowers 2030 total volume to 1.800m and 2035 to 2.558m. The 2% productivity sensitivity raises 2029 volume to 1.593m. These are execution scenarios conditional on profitable demand absorption.

Owned-wholesale units remain the user's consensus assumptions: 504,780 / 599,196 / 689,835 for 2027–2029. No extrapolated wholesale forecast is added after 2029. Remaining staffing upside at mature ADESA integrations is not quantified: the old 13k standard integration limit is retained. The new model is not a complete reconciliation of the company's roughly 1.5m currently built-out capacity.

## Labor and costs

At unchanged productivity, 10% hours growth requires about 10% more effective staffing hours until capped. At unchanged hours per person, that implies roughly 10% net productive workforce growth; gross hiring must also cover attrition and training. Original-site modeled establishment hours rise from a 15.72m anchor proxy to 20.68m in 2029. At 2,000 hours per employee-year, that is roughly 2,481 additional FTE equivalents. These include establishment roles, not just technicians, and neither the Q3 hour proxy nor the 2,000-hour conversion is measured contemporaneous headcount.

Cost illustration versus the old bridge, using the existing cost model's provisional assumptions:

| 2029 incremental requirement | Amount | Treatment |
|---|---:|---|
| Retail units | 160,901 | Conditional production-to-sales translation |
| Adjusted SG&A | $409m | Existing companywide variable cost driver; segment split still needed |
| Normal direct reconditioning labor | $64m | Memo component already inside GPU; do not subtract twice |
| Nonproject capex | $16m | Existing volume-scaled placeholder; equipment needs unverified |
| Net working capital balance | $676m | $4,200 per added annual unit placeholder; balance difference, not annual expense |

Normal reconditioning labor belongs in inventory/cost of sales, whereas support, administration and relevant logistics costs feed SG&A under the company's classification. OSHA establishment hours and the cost model's eight direct hours/vehicle are different populations and must not be treated as interchangeable staffing estimates. This pass does not calculate a new earnings or valuation target. New-cohort training inefficiency, overtime, wage pressure and extra equipment need calibration before promoting the scenario into the full financial model. The SG&A proxy scales total-company costs with retail even while wholesale is held fixed, another remaining refinement.

## Decision and next check

Use the old bridge as a restricted-recovery comparator, and use this scenario grid to test continued expansion. The evidence supports removing the arbitrary plateau; it does not identify a uniquely correct 10% ramp or prove demand at today's margins. The 2027 central case remains below consensus: the objective is a defensible mechanism, not forcing every forecast above the Street.

Next useful observation is matched output and productive staffing at the same sites across two dates, ideally with shift counts, repair mix and training attrition. Quarterly production/inventory growth and unit preparation costs can then test whether effective staffing is translating into sellable inventory. Avoid spending more time on parking counts or raw job postings as substitutes. Demand, sourcing, inventory aging and financing concessions must separately justify sales absorption and return on the incremental costs.
