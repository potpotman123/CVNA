# Carvana growth cost model

The cost extension attaches to the agreed November 1 volume bridge without changing its volumes. It replaces the preliminary aggregate SG&A and capex shortcuts with category and project schedules in a separate, reproducible scenario. It does not overwrite the preliminary DCF or establish a new fair value.

**Model-ready:** disclosed project budget ranges; expense classification; Q3 SG&A baseline; the arithmetic linking each project to spending and output. **Still assumptions:** construction payment timing, cost behavior, staffing intensity, wage rates, ramp inefficiency, and nonproject investment. These can enter sensitivity analysis, not yet a high-confidence base case.

Run `python3 research/valuation/cost-layer-2026-11-01.py`. The companion JSON includes annual financial results, every project's annual spending, inputs, provenance and sensitivities. No licensed source downloads are required.

## Capital spending by project

Management's [August presentation, slide 6](https://investors.carvana.com/~/media/Files/C/Carvana-IR/reports-and-presentations/jp-morgan-auto-conf-aug-2026.pdf) specifies $2–3m per standard integration and approximately 13,000 incremental annual capacity, versus $30–35m and approximately 40,000 for a full buildout. The model uses midpoints of $2.5m and $32.5m. Increasing staffing at existing facilities requires no facility expansion capex under that framework; it still requires operating expense and potentially supporting logistics investment.

The agreed schedule contains Orlando plus 34 subsequent standard integrations, and 27 major buildouts starting over 2027–2035. Their midpoint budgets total $965m, including modeled spending before 2027. Site compatibility and the additivity of capacities remain assumptions inherited from the volume bridge.

Cash spending is assumed linear over six months before standard openings and twelve before major openings. Production ramps remain nine and eighteen months respectively. These are distinct clocks. $55.5m of the project budgets is allocated through 2026 under this convention; that is not a claim about actual spending already incurred. Nominal project budgets remain flat, with no construction inflation or overruns included.

| Year | Retail units, millions | Standard capex, $m | Major capex, $m | Other capex, $m | Total capex, $m | Adjusted SG&A, $m |
|---|---:|---:|---:|---:|---:|---:|
| 2027 | 0.982 | 17.5 | 97.5 | 175.5 | 290.5 | 3,276 |
| 2028 | 1.172 | 17.5 | 97.5 | 199.3 | 314.3 | 3,782 |
| 2029 | 1.382 | 17.5 | 97.5 | 226.4 | 341.4 | 4,340 |
| 2030 | 1.593 | 17.5 | 97.5 | 255.0 | 370.0 | 4,901 |
| 2031 | 1.804 | 10.7 | 97.5 | 285.1 | 393.4 | 5,462 |
| 2032 | 1.986 | 0 | 97.5 | 313.7 | 411.2 | 5,952 |
| 2033 | 2.111 | 0 | 97.5 | 337.2 | 434.7 | 6,295 |
| 2034 | 2.231 | 0 | 97.5 | 361.3 | 458.8 | 6,628 |
| 2035 | 2.351 | 0 | 48.8 | 386.6 | 435.3 | 6,961 |

All forecast amounts are scenario outputs. The 2035 decline is a horizon artifact: no 2036 construction cohort is scheduled. Do not use it as normalized terminal capex if expansion continues.

Other capex covers fleet, software, equipment replacement and supporting facilities outside the modeled project budgets. Its $160m starting run rate is **assumed**, with half scaling with volume and the full amount inflating 3% annually. $100m and $250m starting anchors are separate sensitivities. Disclosed aggregate property/equipment purchases do not isolate these categories, so $160m is not observed maintenance capex. It replaces, rather than supplements, the preliminary 1%-of-revenue allowance. Leased fleet/facilities would instead require an appropriate operating lease and cash-flow schedule; acquisition spending is excluded.

## Costs and accounting treatment

The [Q3 2026 10-Q, SG&A discussion and reconciliation](https://www.sec.gov/Archives/edgar/data/1690820/000169082026000067/cvna-20260930.htm) provides the accounting classifications and baseline below.

| Cost | Economic driver | Where it belongs | Implementation |
|---|---|---|---|
| Vehicle purchases, parts, external repair | Units, vehicle mix, repair severity, sourcing | Inventory then cost of sales | Embedded in baseline gross profit; separate $100/car adverse nonlabor sensitivity |
| Reconditioning technicians and related benefits | Paid hours/car × loaded hourly wage | Vehicle preparation cost of sales, generally through inventory | Memorandum staffing schedule; only incremental inflation/ramp cost deducted from baseline GPU |
| Inbound transportation | Purchased units, distance, load factor | Cost of sales | Embedded baseline; included in nonlabor cost stress |
| Recon-site occupancy and equipment | Site count, shifts, utilization | Cost of sales; asset purchases capitalized | Baseline embedded; site-specific incremental fixed costs not disclosed or separately calibrated |
| Delivery and customer-service payroll | Deliveries, contacts, hours per transaction | SG&A compensation | Category forecast; do not also add to logistics payroll |
| Outbound fleet fuel, repairs, third-party transport | Miles, density, load factor, deliveries | SG&A logistics; owned fleet purchases capex | Category forecast plus separate nonproject capex envelope |
| Marketing | Incremental customers, acquisition cost, brand spend | SG&A advertising | Category forecast; no assumed improvement in variable cost per unit |
| Hubs and vending-machine occupancy | Open locations and footprint | SG&A market occupancy | Partly volume-linked, partly fixed with inflation |
| Title/registration processing, limited warranty, IT, insurance, corporate services | Transactions, claims, headcount, complexity | SG&A other; certain software payroll capitalized | Category forecast; no separate duplicate charge |
| Hiring, training, preopening and ramp inefficiency | Staffing before output; excess paid hours | Depends on function and capitalization eligibility | Explicit direct-labor overlay; not an audited prediction of quarterly GAAP recognition |
| Stock compensation and depreciation | Compensation policy and asset base | Allocated COGS/SG&A under GAAP | Excluded from adjusted operating output here; must be restored appropriately in valuation |
| Inventory and receivables funding | Holding days, purchase cost, origination/sale timing | Working capital; financing interest separately | Prior $4,200 net working capital per incremental annual unit retained as unvalidated placeholder |

Cash paid for inventory can precede COGS recognition. Unsold inventory and abnormal idle/training costs require separate treatment; the model assumes produced units are sold and is an annual economic approximation. Floorplan borrowing does not eliminate the investment in inventory. Do not subtract both gross inventory funding and the existing net-working-capital placeholder.

## SG&A calibration and labor assumptions

Q3 GAAP SG&A was $805m: compensation $255m, advertising $152m, occupancy $18m, logistics $68m and other $312m. Removing $24m stock compensation and $39m depreciation/amortization reconciles to $742m adjusted SG&A. The $39m includes amortization; PPE depreciation alone is not the complete adjustment.

The model removes SBC from compensation and provisionally allocates D&A proportionally across occupancy, logistics and other. That category allocation is assumed, while the total reconciliation is observed. Starting variable shares are respectively 80%, 90%, 40%, 90% and 60%. For each category:

`Annual cost = Q3 adjusted cost × 4 × [variable share × unit growth factor × variable-cost inflation + fixed share × fixed-cost inflation]`.

Fixed costs inflate 3%; variable unit costs are flat in the working case. This is a smooth approximation to stepwise expansion, not proof that customer care or corporate functions can scale indefinitely without new infrastructure. A no-fixed-leverage case and 3% variable-cost inflation case test that risk. Retail units are a scaling proxy for shared retail/wholesale operations; a subsequent full model should give auction activity its own driver.

Direct production labor uses **illustrative**, unverified assumptions: eight paid hours/vehicle, $35/hour wages, 30% benefits/payroll burden, 2,000 paid hours per FTE annually, and 3% wage inflation. It adds 50% excess hours on production within new projects' ramp windows and two months of preopening staffing at 25% of mature staffing. OSHA establishment hours are not treated as measured technician hours.

Normal labor is already embedded in baseline GPU and is shown only as a memorandum item. The earnings bridge subtracts inflation above that baseline and the explicit ramp/preopening overlay. Existing Q3 ramp costs cannot be isolated, so this overlay is conservative rather than a fully normalized incremental cost estimate. FTE equivalents represent annual labor requirements, not actual headcount or gross hires; attrition and job mix are unknown. Original-site recovery is captured in total units without an additional site-specific training penalty.

## What changes the investment conclusion

At 2030 modeled volume of 1.593m units:

- Each additional $100/car of nonlabor COGS reduces annual profit by $159m.
- The working labor inflation/ramp overlay reduces adjusted operating profit by $102m versus constant GPU before that overlay.
- Assuming 3% annual inflation in variable SG&A costs reduces profit by a further $508m versus the working case.
- Eliminating the assumed fixed-cost leverage reduces profit by $536m versus the working case, as a separate sensitivity.
- Varying the nonproject capex starting anchor from $100m to $250m changes 2030 total capex from $274m to $513m.

These sensitivities overlap and should not be added indiscriminately. The model holds financing and ancillary economics in the original gross-profit baseline; it does not validate their sustainability. Taxes, stock compensation, asset depreciation, leases and capital structure still require reconciliation before producing a revised valuation.

Next evidence priorities are actual project spending-to-complete, direct production labor hours and loaded pay, paid versus productive hours during ramp, delivery cost per vehicle, and the split of fleet/software/maintenance capex. This pass establishes the accounting and executable schedule without treating missing unit economics as observed facts.

Validation: the model retains all nine volume forecasts exactly; reconciles the $742m adjusted SG&A anchor; allocates each project's full low/mid/high budget exactly once across calendar years; checks the earnings identity; and confirms that removing labor inflation and ramp penalties produces no extra labor deduction. The old DCF remains a preserved preliminary comparison, not the current cost schedule.

Consensus and business split: [November 1 comparison](consensus-comparison-2026-11-01.md) compares the supplied estimates and explicitly separates retail, owned wholesale, marketplace, and other economics and now supersedes this scenario’s implied wholesale volume with supplied consensus for 2027–2029. See that comparison for the mechanical revenue and earnings adjustment; this original cost scenario is preserved for reproducibility.
