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
| Adjusted EBITDA, $bn | 3.885 / 3.669 | 4.826 / 4.479 | 5.792 / 5.388 |
| Adjusted SG&A per retail unit, $ | 2,927 / 3,336 | 2,903 / 3,227 | 2,988 / 3,140 |
| Capital spending, $m | 260 / 290 | 280 / 314 | 350 / 341 |

Our EBITDA is 5.6%, 7.2% and 7.0% below the displayed consensus. Cost-model calibration is still provisional; this is a comparison of current assumptions, not a conclusion that consensus expenses are wrong. Our capex exceeds consensus in 2027–2028 partly because of the assumed nonproject capex envelope. That input is not independently verified maintenance investment.

Use adjusted-to-adjusted comparisons here. The screenshot's total gross profit per unit is on the historical GAAP basis, whereas the cost model starts from adjusted gross profit. A direct comparison of those two GPU lines would overstate our economic margin advantage.

## The business split

The previous volume bridge forecast **retail used vehicles only**. Its aggregate gross-profit baseline included wholesale and financing/ancillary profit, implicitly scaling those businesses with retail. It did not separately forecast wholesale units or ADESA auction transactions.

The new companion calculation explicitly separates four lines while reconciling exactly to the existing model:

| Business | Unit and revenue driver | Current implementation |
|---|---|---|
| Retail used vehicles | Consumer retail sales × retail selling price | Existing capacity-driven retail forecast; Q3 realized revenue per unit held flat |
| Carvana-owned wholesale vehicles | Cars Carvana owns and sells wholesale × wholesale selling price | Q3 owned-wholesale/retail ratio held flat; wholesale ASP and profit per owned unit held flat |
| Wholesale marketplace | Auction transactions × fee/service revenue per transaction | Transaction count unknown; revenue and profit remain proportional to retail as an explicit placeholder |
| Other | Finance originations/sales, ancillary-product attachment and economics | Prior per-retail-unit baseline preserved; sustainability still under investigation |

The [Q3 2026 filing](https://www.sec.gov/Archives/edgar/data/1690820/000169082026000067/cvna-20260930.htm) reports 217,385 retail units and 111,119 owned wholesale units: a 51.1% ratio. Wholesale vehicles are principally sourced from customer purchases and trade-ins. A proper independent forecast should therefore use acquisition volumes, trade-in attachment and the share of acquired cars routed wholesale. It should not treat wholesale vehicles as additional retail reconditioning capacity.

| Year | Consensus owned wholesale units | Our constant-ratio placeholder | Difference % |
|---|---:|---:|---:|
| 2027 | 504,780 | 501,957 | −0.6% |
| 2028 | 599,196 | 599,000 | approximately 0.0% |
| 2029 | 689,835 | 706,430 | +2.4% |

Consensus implies wholesale/retail ratios of approximately 48.5%, 48.8% and 47.2%. Our higher ratio offsets much of our lower retail volume. This is not independent evidence that wholesale will outperform.

The filing's wholesale selling price and owned-wholesale profit-per-unit exclude marketplace activity. We use those rounded metrics to estimate owned-wholesale revenue/profit, then subtract from reported total wholesale revenue/profit to obtain approximate marketplace residuals. Those residuals are derived, not separately reported exact balances. Marketplace growth tied to retail is an inherited shortcut; an alternative flat-marketplace-GP sensitivity is included in JSON. Auction transactions may include Carvana-owned cars, so adding them to retail-plus-owned-wholesale units would risk double counting.

**Denominator trap:** Bloomberg's wholesale gross profit under “Gross Profit per Retail Unit” is wholesale gross profit divided by retail units. It is not profit per wholesale car. The companion model keeps those denominators separate.

## Source quality and reproducibility

The dated company-specific screenshots supply the unit forecasts and operating KPIs; the headline screenshot supplies the more precise capital-spending estimates. The duplicate business-breakdown screenshots are not independent sources. Contributor counts vary: retail-unit estimates have 16, 14 and 8 contributors in 2027–2029. These snapshots are not represented as a live consensus refresh.

Do not force independently averaged Bloomberg rows to reconcile. Their contributor populations differ. There are also larger data/mapping anomalies in the business-breakdown panel: 2025 used gross margin is displayed as 43.40%, whereas $1,978m/$14,537m implies 13.61%; 2028 used cost of revenue is displayed above revenue despite positive gross profit. Those particular cost and margin rows are excluded pending a mapping check. The numeric model records the displayed unit and KPI values without using anomalous cost rows.

Run `python3 research/valuation/consensus-comparison-2026-11-01.py` to regenerate the companion JSON. It contains the transcribed consensus, source filenames, Q3 anchors, annual business splits, differences, and limitations. Assertions confirm that business revenue and the gross-profit reconciliation exactly reproduce the current aggregate model. No source screenshots or licensed full reports are committed.

See [cost model](cost-layer-2026-11-01.md) and [volume bridge](../volume/capacity/volume-bridge-2026-11-01.md). The new split makes existing assumptions visible; it does not silently add wholesale earnings on top of the previous total or overwrite the preliminary valuation.
