# Carvana model versus supplied consensus

Our existing capacity-based retail forecast is below the Bloomberg consensus supplied on November 1, 2026. The comparison does not establish a bullish near-term earnings variant: adjusted EBITDA is also lower, and adjusted SG&A per retail unit is higher. All model outputs remain conditional on the volume and cost assumptions in the linked models.

## Retail volume comparison

| Year | Consensus retail units | Our retail units | Difference | Difference % |
|---|---:|---:|---:|---:|
| 2027 | 1,040,187 | 981,992 | −58,195 | −5.6% |
| 2028 | 1,228,260 | 1,171,840 | −56,420 | −4.6% |
| 2029 | 1,461,650 | 1,382,007 | −79,643 | −5.4% |

The screenshots show 820,413 consensus FY2026 retail units. Our 869,540 starting anchor is Q3 units multiplied by four, **not** an FY2026 forecast; a direct comparison would be invalid. We have no supplied consensus beyond 2029, so cannot assert that our longer-term volume case is above consensus.

For a genuine positive volume variant, the research must support additional production or better conversion of capacity into sales beyond our current assumptions. Candidates include original-site productivity beyond historical staffing recovery, faster ADESA ramps, and more or larger projects. They are hypotheses to test, not adjustments to insert merely to beat consensus.

## Earnings and investment comparison

| Measure | 2027 consensus / ours | 2028 consensus / ours | 2029 consensus / ours |
|---|---:|---:|---:|
| Adjusted EBITDA, $bn | 3.885 / 3.672 | 4.826 / 4.479 | 5.792 / 5.372 |
| Adjusted SG&A per retail unit, $ | 2,927 / 3,336 | 2,903 / 3,227 | 2,988 / 3,140 |
| Capital spending, $m | 260 / 290 | 280 / 314 | 350 / 341 |

Our mechanically revised EBITDA is 5.5%, 7.2% and 7.2% below the displayed consensus. Cost-model calibration is still provisional; this is a comparison of current assumptions, not a conclusion that consensus expenses are wrong. Our capex exceeds consensus in 2027–2028 partly because of the assumed nonproject capex envelope. That input is not independently verified maintenance investment.

Use adjusted-to-adjusted comparisons here. The screenshot's total gross profit per unit is on the historical GAAP basis, whereas the cost model starts from adjusted gross profit. A direct comparison of those two GPU lines would overstate our economic margin advantage.

## The business split

The previous volume bridge forecast **retail used vehicles only**. Its aggregate gross-profit baseline included wholesale and financing/ancillary profit, implicitly scaling those businesses with retail. It did not separately forecast wholesale units or ADESA auction transactions.

The companion calculation now uses supplied consensus owned-wholesale units for 2027–2029, replacing the previous constant-ratio placeholder. It removes the old implied owned-wholesale revenue/profit before adding the revised amounts, avoiding double counting. Retail forecasts are unchanged. No wholesale forecast is invented beyond 2029; the combined business schedule stops there until additional estimates or an independent view are available. The original cost-layer output is preserved as a prior scenario.

The model separates four lines:

| Business | Unit and revenue driver | Current implementation |
|---|---|---|
| Retail used vehicles | Consumer retail sales × retail selling price | Existing capacity-driven retail forecast; Q3 realized revenue per unit held flat |
| Carvana-owned wholesale vehicles | Cars Carvana owns and sells wholesale × wholesale selling price | Supplied consensus units; existing Q3 wholesale ASP and profit per owned unit held flat pending further work |
| Wholesale marketplace | Auction transactions × fee/service revenue per transaction | Transaction count unknown; revenue and profit remain proportional to retail as an explicit placeholder |
| Other | Finance originations/sales, ancillary-product attachment and economics | Prior per-retail-unit baseline preserved; sustainability still under investigation |

The [Q3 2026 filing](https://www.sec.gov/Archives/edgar/data/1690820/000169082026000067/cvna-20260930.htm) reports 217,385 retail units and 111,119 owned wholesale units: a 51.1% ratio. Wholesale vehicles are principally sourced from customer purchases and trade-ins. A proper independent forecast should therefore use acquisition volumes, trade-in attachment and the share of acquired cars routed wholesale. It should not treat wholesale vehicles as additional retail reconditioning capacity.

| Year | Consensus owned wholesale units | Current model | Difference % |
|---|---:|---:|---:|
| 2027 | 504,780 | 504,780 | 0.0% |
| 2028 | 599,196 | 599,196 | 0.0% |
| 2029 | 689,835 | 689,835 | 0.0% |

The earlier 51.1% wholesale/retail extrapolation has been removed. Consensus units are a neutral modeling input, not our independently validated forecast. Wholesale price and unit margin remain separate existing assumptions; switching volume alone does not adopt consensus wholesale profits. The gross-profit change passes through mechanically to EBITDA, with SG&A and capex unchanged until wholesale-specific costs can be calibrated.

## Wholesale materiality and research priorities

The supplied FY2025 actual columns show 297,643 wholesale vehicles and 596,641 retail vehicles. Wholesale is **33.3% of owned vehicles sold**, but total wholesale revenue including marketplace is $4.052bn / $20.322bn = **19.9% of company revenue**, and wholesale gross profit is $481m / $4.192bn = **11.5% of company gross profit**. Within that profit, owned vehicle sales contribute $302m (7.2% of total company GP) and marketplace contributes $179m (4.3%). The unit count excludes marketplace transactions, while these wholesale financial totals include marketplace; those are deliberately different populations, not a single per-unit margin calculation.

Wholesale deserves an independent view, but its unit share overstates its direct gross-profit weight. It also supports retail sourcing: being able to monetize cars that do not fit retail standards helps Carvana buy from consumers and accept trade-ins. Gross profit is not segment EBITDA; shared expenses prevent inferring its exact earnings contribution from this table.

The focused diligence questions are:

1. How many cars are acquired through standalone consumer purchases and retail trade-ins, and what proportion are routed to wholesale? This establishes a volume bridge independent of retail recon capacity.
2. What determines owned-wholesale purchase/sale spreads, transport and auction costs, depreciation and holding periods? These establish sustainable profit per wholesale vehicle.
3. What drives third-party auction transactions, fees and services per transaction, and marketplace costs? This requires a separate ADESA forecast, excluding double-counted Carvana-owned throughput.
4. How much additional staff, transport, working capital and capex does wholesale growth require, and does adding retail recon activity constrain auction capacity?

A 20% change in FY2025 wholesale gross profit would change consolidated gross profit by about $96m, or 2.3%, before operating-cost responses and retail-sourcing spillovers. This is a scale sensitivity, not a forecast. Until this work is done, hold consensus units and do not claim a wholesale variant.

The filing's wholesale selling price and owned-wholesale profit-per-unit exclude marketplace activity. We use those rounded metrics to estimate owned-wholesale revenue/profit, then subtract from reported total wholesale revenue/profit to obtain approximate marketplace residuals. Those residuals are derived, not separately reported exact balances. Marketplace growth tied to retail is an inherited shortcut; an alternative flat-marketplace-GP sensitivity is included in JSON. Auction transactions may include Carvana-owned cars, so adding them to retail-plus-owned-wholesale units would risk double counting.

**Denominator trap:** Bloomberg's wholesale gross profit under “Gross Profit per Retail Unit” is wholesale gross profit divided by retail units. It is not profit per wholesale car. The companion model keeps those denominators separate.

## Source quality and reproducibility

The dated company-specific screenshots supply the unit forecasts and operating KPIs; the headline screenshot supplies the more precise capital-spending estimates. The duplicate business-breakdown screenshots are not independent sources. Contributor counts vary: retail-unit estimates have 16, 14 and 8 contributors in 2027–2029. These snapshots are not represented as a live consensus refresh.

Do not force independently averaged Bloomberg rows to reconcile. Their contributor populations differ. There are also larger data/mapping anomalies in the business-breakdown panel: 2025 used gross margin is displayed as 43.40%, whereas $1,978m/$14,537m implies 13.61%; 2028 used cost of revenue is displayed above revenue despite positive gross profit. Those particular cost and margin rows are excluded pending a mapping check. The numeric model records the displayed unit and KPI values without using anomalous cost rows.

Run `python3 research/valuation/consensus-comparison-2026-11-01.py` to regenerate the companion JSON. It contains the transcribed consensus, source filenames, Q3 anchors, annual business splits, differences, and limitations. Assertions confirm that owned-wholesale units equal consensus and that changes in business revenue and gross profit equal exactly the replacement of the old wholesale-volume assumption. No source screenshots or licensed full reports are committed.

See [cost model](cost-layer-2026-11-01.md) and [volume bridge](../volume/capacity/volume-bridge-2026-11-01.md). The revised split replaces wholesale earnings embedded in the previous total; it does not add them twice or overwrite the preliminary valuation.
