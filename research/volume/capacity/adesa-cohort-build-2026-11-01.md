# ADESA cohort calculation and mature-bin treatment

November 1, 2026. User-approved assumptions: 13,000 annual capacity per standard integration; straight-line ramp to 100% over nine months. Calculations only; no workbook. Output is modeled production, not reported site results or a sales forecast.

## Scope, timing and provenance

Fixed Q3 2026 snapshot: 21 candidates from `../adesa-21-site-candidate-roster.json`, split into 16 modeled mature sites and five ramping sites. Later Orlando and future integrations are excluded for a separate new-opening bin. The old named roster remains a candidate reconstruction, not a company-certified census.

Use announcement dates as first-production proxies where actual dates are absent. Buffalo's disclosed April 2024 operating month uses April 15. The original `first_production_date` fields remain null: no dates were relabeled as observed. Reopened all five 2026 company releases on November 1: each announces plans/integration and hiring, not a precise first-production date. Thus timing uncertainty remains separate from the agreed ramp. Source URLs and date meaning are retained per site in the JSON.

The calculation uses calendar months as equal time units, with day-of-month fractions. Full calendar years at mature output always equal 13,000, including leap years. A nine-calendar-month anniversary is shown as an approximate completion date; differing month lengths can cause sub-day differences from the fractional-month calculation. Q3 exit is measured at October 1. Bin membership stays fixed for the bridge, even as the five sites subsequently mature.

## Ramping bin: five 2026 integrations

| Site | Proxy start | Approx. full-rate date | 2026 vehicles | 2027 vehicles | Increase |
|---|---|---|---:|---:|---:|
| Syracuse | Apr 28, 2026 | Jan 28, 2027 | 3,949 | 12,951 | 9,003 |
| Chicago | May 6, 2026 | Feb 6, 2027 | 3,698 | 12,919 | 9,221 |
| Sarasota | Jun 24, 2026 | Mar 24, 2027 | 2,338 | 12,539 | 10,201 |
| Brasher’s / Sacramento | Sep 1, 2026 | Jun 1, 2027 | 963 | 11,495 | 10,532 |
| Charlotte | Sep 15, 2026 | Jun 15, 2027 | 751 | 11,201 | 10,450 |
| **Total, rounded from unrounded sums** | | | **11,700** | **61,106** | **49,407** |

All five yield 65,000 in 2028, adding another 3,894 over 2027. This is not another 65,000 increment. Differences in rounded rows may not sum exactly.

The modeled Q3-exit annualized production rate for this cohort is 21,241. Relative to that rate, 2027's additional production is 39,865, versus 49,407 when comparing full-year 2027 to full-year 2026. Use the correct bridge for the baseline: **do not add the full-year increase to a Q3-annualized company forecast**.

Start-date sensitivity, keeping nine-month ramp and 100% endpoint fixed:

| Proxy shift for these same five sites | 2026 production | 2027 production | 2027 increase |
|---|---:|---:|---:|
| Three months earlier | 24,663 | 64,393 | 39,730 |
| Announcement proxy | 11,700 | 61,106 | 49,407 |
| Three months later | 3,681 | 52,875 | 49,194 |

These are scenarios, not date confidence intervals. Later starts can leave year-on-year growth similar while lowering both years' output. No attempt to fit site outputs to company retail sales was made.

## Next bin: 16 modeled mature ADESA integrations

Members: Buffalo, Portland, Kansas City, Houston, Las Vegas, Boston, Atlanta, Indianapolis, New Jersey, Phoenix, Colorado Springs, Nashville, Seattle, Dallas, Golden Gate and Long Island.

| Quantity | Modeled vehicles |
|---|---:|
| 2026 production | 201,525 |
| 2027 production | 208,000 |
| 2028 production, unchanged standard configuration | 208,000 |
| 2027 increase over 2026 | 6,475 |
| Further increase above Q3-exit annualized rate | 0 |

The 6,475 is calendar-year carryover: some sites were still ramping early in 2026, although all 16 are modeled mature by Q3. Flat standard capacity is an accounting consequence of the agreed nine-month/13,000 assumptions, **not evidence that these properties lack headroom**. Calling these sites 50% utilized again would contradict the adopted initial-ramp calculation unless we explicitly introduce a higher capacity definition.

### How to add further growth without double-counting

1. **More output within the current configuration:** requires an explicit increase in the 13,000 benchmark, supported by productivity or configuration evidence. Mechanical sensitivities for this 16-site bin are +20,800 annual vehicles for +10% and +41,600 for +20%. Neither is an evidence-backed forecast; no automatic credit is included.
2. **Additional standard-equivalent lines/capability:** if a project is genuinely additive and comparable, one 13,000-unit increment adds 13,000 at maturity. The original integration's $2–3m cost is not automatically the cost of a second line. Check equipment, construction and labor separately.
3. **Full buildouts:** management describes ~40,000 incremental annual capacity for $30–35m/site. If an already-counted 13,000 integration receives a project genuinely adding 40,000, resulting total is 53,000; if a project-specific disclosure instead describes 40,000 total, increment is 27,000. Respect the source's denominator. Do not assign all three announced 2027 builds to this mature bin without confirming sites and scopes.

| Verified additive full-buildout projects at mature sites (scenario count) | Extra annual capacity | Project budget |
|---:|---:|---:|
| 1 | 40,000 | $30–35m |
| 2 | 80,000 | $60–70m |
| 3 | 120,000 | $90–105m |

This quantifies the next lever but is not an approved project allocation or year-one production estimate. Larger buildouts need a separate ramp: Aramis Nemours's roughly 18-month plan is more comparable than applying the nine-month light-integration assumption automatically. Construction spend may already be partly incurred; wages, working capital and demand absorption remain separate.

## Combined existing ADESA bridge

| Cohort fixed at Q3 | 2026 | 2027 | 2028 | 2027 vs 2026 |
|---|---:|---:|---:|---:|
| Mature 16 | 201,525 | 208,000 | 208,000 | 6,475 |
| Ramping five | 11,700 | 61,106 | 65,000 | 49,407 |
| **All 21** | **213,224** | **269,106** | **273,000** | **55,882** |

Rounding can create one-unit discrepancies. These are modeled contributions from the existing Q3 integrations, excluding original IRCs, future integrations, major buildouts and changes in ready inventory or marketplace sales. “Mature” is a model classification, not observed utilization. No companywide forecast or incremental profitability conclusion follows from this table alone.

## Reproduction and checks

Run `python3 research/volume/capacity/adesa-cohort-build.py`. Full source dates, start classifications, site outputs, growth and sensitivity are saved in `adesa-cohort-build-2026-11-01.json`. Assertions check 21 sites, 16/5 bin split, 8,125 first rolling year for a nine-month ramp, 273,000 final annual output and no site exceeding the standard ceiling. Counts and sums reconcile; none of these arithmetic checks independently validates ramp timing.

Relevant sources: `adesa-peer-ramp-evidence-2026-11-01.md` for the approved peer-based ramp and links; `sources.md` S5 for management's integration/buildout capacity and costs; source links per site in the input roster and output JSON.

Next actionable bin work: identify the named 2027 full-buildout projects and whether each adds to a mature integration, recent integration or auction-only location, before allocating the 40,000 increments. Keep land-only optionality outside scheduled production.
