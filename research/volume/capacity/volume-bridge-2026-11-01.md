# Combined volume build: all facility bins

November 1, 2026. Volume-only scenario, authorized by the user. These are conditional production estimates, not reported site output or company guidance. Costs and profitability remain unfinished. No workbook created.

## Result

The revised build removes all 5% annual labor growth beyond historical recovery and assumes three full-buildout production starts every year from 2027 through 2035. It reaches **2.351 million annual vehicles in 2035, not 3 million**. The 27 projects eventually support 1.08 million additional annual capacity, but contribute 930,000 vehicles in calendar 2035 because the final projects are still ramping. Holding everything else flat, fully ramped total output would be approximately **2.501 million**. These remain conditional scenarios, not independently validated production forecasts.

Annual vehicles, rounded to nearest thousand:

| Year | Original: 10 recovery sites | Original: other 8 | Mature ADESA 16 | Ramping ADESA 5 | Future standard integrations | Major buildout additions | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2027 | 445,000 | 226,000 | 208,000 | 61,000 | 31,000 | 12,000 | 982,000 |
| 2028 | 467,000 | 226,000 | 208,000 | 65,000 | 115,000 | 91,000 | 1,172,000 |
| 2029 | 467,000 | 226,000 | 208,000 | 65,000 | 206,000 | 210,000 | 1,382,000 |
| 2030 | 467,000 | 226,000 | 208,000 | 65,000 | 297,000 | 330,000 | 1,593,000 |
| 2031 | 467,000 | 226,000 | 208,000 | 65,000 | 388,000 | 450,000 | 1,804,000 |
| 2032 | 467,000 | 226,000 | 208,000 | 65,000 | 451,000 | 570,000 | 1,986,000 |
| 2033 | 467,000 | 226,000 | 208,000 | 65,000 | 455,000 | 690,000 | 2,111,000 |
| 2034 | 467,000 | 226,000 | 208,000 | 65,000 | 455,000 | 810,000 | 2,231,000 |
| 2035 | 467,000 | 226,000 | 208,000 | 65,000 | 455,000 | 930,000 | 2,351,000 |

## Starting point and original IRCs

The [Q3 2026 letter](https://investors.carvana.com/~/media/Files/C/Carvana-IR/documents/cvna-shareholder-letter-q3-2026.pdf) reports 217,385 retail units. Four times that is **869,540**, a normalized reference, **not FY2026 production or sales**. We temporarily assume production equals sales. Inventory movements and marketplace transactions can break that identity.

The existing ADESA ramp model produces 220,826 annualized vehicles for the same Q3 period. Subtracting this leaves **648,714** for the original 18 IRCs. This residual is an allocation assumption, not measured original-IRC output; a wrong ADESA estimate flows directly into it.

The 18 originals report 14,651,510 hours in 2025. Fourteen have matched historical records; ten have a combined 2,127,888-hour gap below their 2022 levels. The other eight comprise four already at/above historical hours and four without comparable historical observations. Missing history does not mean no headroom. See [historical calculations](labor-recovery-calculations-2026-11-01.json) and [OSHA records and provenance](staffing-panel-data.json).

To avoid applying the entire 2025 gap again after Q3 2026, the base **assumes half has already closed**. Allocate the residual output using each site's 2025 hours plus half its gap. The ten recovery sites reach 75% gap closure in annual-average 2027 and 100% in 2028. Output scales linearly with hours; no productivity gain is added.

The other eight remain flat. The ten recovery sites also remain flat after completing historical recovery in 2028. No further labor growth or productivity gains are credited. The half-gap starting assumption remains unverified; recovery timing is also assumed. The 1-million original-network planning limit does not bind.

## Standard integrations and major buildouts

- Existing 21: retain the [cohort calculation](adesa-cohort-build-2026-11-01.md), with 13,000 annual capacity each and nine-month linear ramps. Their dates are mostly announcement proxies. Do not add calendar-year increases to the Q3 reference; the bridge uses each year's absolute output.
- Remaining 35: Orlando's October 2026 proxy start plus 34 future slots, seven per year from 2027 and six in the final 2031 cohort. All standard integrations produce 728,000 annually once mature. See [property coverage and pipeline](adesa-future-pipeline-2026-11-01.md). Seven annually extrapolates management's 2026 guidance; it is not future guidance.
- Major buildouts: three company-reported projects expected to start production in 2027, with April/July/October starts assumed. Add three more starts annually in 2028–2035, as requested by the user. All starts after the disclosed 2027 cohort are assumptions, not management guidance.
- Each major project adds 40,000 annual capacity and ramps linearly over 18 months. This uses the larger Aramis facility plan as a rough timing reference; it is not a measured CVNA ramp. The nine-month standard ramp draws on Aramis's smaller-hub benchmark. See [peer evidence and limitations](adesa-peer-ramp-evidence-2026-11-01.md).
- Major-project slots represent distinct eligible properties and additional output above the standard integration allowance. Actual site identities, engineering compatibility and incremental versus overlapping scope must be confirmed before using named project cash flows. There are enough modeled mature standard sites to host these slots, but suitability is unverified.

Management's project increments and illustrative budgets come from [August 2026 presentation, slide 6](https://investors.carvana.com/~/media/Files/C/Carvana-IR/reports-and-presentations/jp-morgan-auto-conf-aug-2026.pdf). We retain an approximate 2-million ADESA / 3-million combined planning boundary. This is not a certified engineering ceiling. Multiplying every property by every possible project increment would exceed those boundaries and is not used here.

## How much depends on the original-IRC assumptions?

Holding ADESA assumptions unchanged:

| Original-network alternative | 2027 total | 2030 total |
|---|---:|---:|
| Base | 981,992 | 1,593,007 |
| all historical recovery already done | 960,033 | 1,549,089 |
| none historical recovery done | 1,007,141 | 1,643,303 |
| production 5pct above sales anchor | 1,026,941 | 1,639,427 |

These isolate assumptions; they are not probability ranges. ADESA capacity, project execution and sales absorption could create much larger errors.

## Sales, costs and next work

The base sales column equals production **only if customers absorb it**. A separate 95% absorption calculation illustrates inventory accumulation, not a sustainable multi-year operating plan. At sustained weak absorption, production would need to slow. No profitability conclusion follows from this volume build.

Preserved for the cost phase: standard integrations have $2–3 million illustrative budgets; major projects $30–35 million. The project register retains 27 major project slots through 2035 and their timing. Already-incurred spend, remaining spend and construction-year cash schedules are unknown and left blank. A production-start year is not the year all capex is paid. The three 2027 projects are already underway, so their full budgets must not automatically be charged to future years. Standard integration and major-buildout scopes also require an overlap check before adding budgets.

Next: schedule remaining capital spending before production starts, estimate hiring/training and incremental operating costs, then connect production to sales, inventory funding and cash returns. Preserve the current volume scenario so cost assumptions do not silently change it.

## Reproduction and checks

Run `python3 research/volume/capacity/volume-bridge.py` from the repository root. [Machine-readable results](volume-bridge-2026-11-01.json) contain annual bins, site allocations, sensitivities, source classifications and project budgets. Inputs are existing committed research files; licensed source text remains local.

Checks reconcile 18 original sites, the historical hours gap, Q3 reference allocation, unique project IDs and annual component sums. Those are arithmetic checks. Matching the Q3 reference by residual allocation is calibration, **not independent validation** of any site's production or spare capacity.
