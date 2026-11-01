# Preliminary valuation and modeling handoff

November 1, 2026. User authorized persisting the previously scratch-only calculations. This preserves the conversation's illustration, not a completed investment model or independently validated long recommendation.

## Current agreed volume scenario

Use [combined volume build](../volume/capacity/volume-bridge-2026-11-01.md) and its JSON. No recurring 5% labor growth. Retain conditional historical labor recovery. Standard integrations: seven starts annually until the remaining pool is exhausted, nine-month linear ramps. Full buildouts: three production starts each year 2027–2035, 40,000 incremental capacity per project, 18-month ramps. The alternative three-then-five schedule was rejected; the earlier omission of 2028–2029 buildouts is superseded.

2035 output is 2,350,632 vehicles: originals 692,632, existing standard ADESA 273,000, future standard ADESA 455,000, major-buildout additions 930,000. The 27 major projects eventually contribute 1.08 million at full ramp; total then reaches 2,500,632 with everything else flat. Neither equals management's 3-million goal.

## Scratch financial assumptions

Q3 2026 annualized reference: 869,540 retail units; $32,160m revenue; $24,576m retail revenue; $6,168m adjusted gross profit; $2,968m adjusted SG&A; $3,200m adjusted EBITDA. Source: [Q3 shareholder letter](https://investors.carvana.com/~/media/Files/C/Carvana-IR/documents/cvna-shareholder-letter-q3-2026.pdf), financial statements and adjusted reconciliations (local extracted source in work/loan-sale-economics/sources/). Annualization is not FY2026 guidance. Calendar 2027–2035 sales equal modeled production, an assumption.

- Retail revenue/unit $28,263; consolidated revenue per retail unit $36,985. Hold both constant. The latter includes wholesale and finance/other revenue and is not a sticker price. Independent growth of wholesale and financing is not modeled.
- Hold adjusted gross profit/unit $7,093 constant, including financing and wholesale economics. Recon and vehicle-acquisition costs are therefore embedded, not separately estimated.
- Assume 70% of adjusted SG&A scales with units and 30% grows 3% annually. This split is unverified. It raises adjusted EBITDA margin to 11.4% in 2035.
- Deduct stock compensation at $100m annualized baseline, scaling with units, as an economic expense; no additional recurring share dilution applied. Starting economic share count still needs a fully diluted reconciliation.
- Assume depreciation 0.8% of revenue; taxes 25% of EBITDA less stock compensation and depreciation.
- Recurring capex 1% of revenue, plus $97.5m/year for major projects starting the following year (2027–2034 cash years), plus $17.5m/year standard-integration spending through 2029 and $15m in 2030. These are coarse timing conventions. 2027-start projects are assumed funded before the valuation date; actual remaining payments are not reconciled. No explicit future projects after 2035, although the exit multiple assumes a continuing business.
- Assume $4,200 additional operating capital for each incremental unit of annual sales. This is a rough inventory/receivable funding allowance, not a measured marginal cash conversion ratio. Financing receivables and retained securitization interests need separate treatment later.
- Unlevered FCF = adjusted EBITDA − stock compensation − normalized taxes − capex − change in operating capital. No interest deduction; net debt is deducted from enterprise value.

## Market inputs and valuation convention

[October 30 market snapshot](https://stockanalysis.com/stocks/cvna/statistics/): $68.29 price, $76.20bn equity value and $78.29bn enterprise value. [Q3 release](https://investors.carvana.com/~/media/Files/C/Carvana-IR/documents/cvna-earnings-release-q3-2026.pdf): FY2026 adjusted EBITDA expected toward upper end of $2.7–3.0bn guidance. Use $3bn as the illustrative denominator, giving 26.0967x. This is a current-year adjusted multiple, not a generic trailing vendor EBITDA multiple.

Use nine end-year discount periods from year-end 2026, with no two-month stub adjustment. Terminal EV = 2035 adjusted EBITDA × exit multiple. Using the current-year 2026 guidance multiple on 2035 realized EBITDA is an approximation. Deduct $2.179bn net debt (short-term facilities + current and long-term debt − unrestricted cash) and $2.130bn TRA liability at face value. Use market-implied economic shares of 1.11583bn rather than Class A shares alone. This approximates inclusion of exchangeable ownership interests; a detailed Up-C/dilution reconciliation remains necessary. Operating leases remain operating costs, not separately deducted debt. The normalized tax model excludes tax-shield benefits while subtracting the TRA obligation, a conservative simplification requiring integrated treatment later.

## Results

| Year | Retail units, m | Retail revenue, bn | Total revenue, bn | Adjusted EBITDA, bn | Unlevered FCF, bn |
|---|---:|---:|---:|---:|---:|
| 2027 | 0.982 | 27.75 | 36.32 | 3.70 | 1.81 |
| 2028 | 1.172 | 33.12 | 43.34 | 4.57 | 2.07 |
| 2030 | 1.593 | 45.02 | 58.92 | 6.49 | 3.26 |
| 2033 | 2.111 | 59.65 | 78.06 | 8.83 | 5.20 |
| 2035 | 2.351 | 66.44 | 86.94 | 9.90 | 6.02 |

Indicative present equity value per share:

| Discount rate | 15x exit | 20x exit | 26.1x exit |
|---|---:|---:|---:|
| 10% | $70.83 | $89.64 | $112.57 |
| 12% | $60.71 | $76.70 | $96.20 |
| 14% | $52.18 | $65.82 | $82.44 |

At 12%/26.1x: $111.65bn EV, $107.34bn equity, 40.9% upside; 83.4% of EV comes from the terminal value. Removing fixed-cost leverage gives $83.44/share. Reducing adjusted gross profit by $500 per retail unit gives $83.42/share; both hold the other assumptions unchanged.

Slowing growth generally lowers the justified multiple, other things equal. Retaining 26.1x in 2035 presupposes substantial subsequent growth, strong cash conversion and/or lower risk. 15x and 20x are sensitivities, not researched peer valuations. Volume growth alone does not establish a long recommendation. Recent projects are not fully ramped in 2035; the exit multiple must value their future contribution without substituting fully ramped earnings for actual earnings and ignoring timing/costs.

## Volume gaps that matter before the full model

1. **Production versus profitable sales:** all produced units are assumed sold; no demand, price-concession or inventory-aging mechanism. Model sales absorption independently and curtail production when stock accumulates.
2. **Starting site output:** original production is a residual of Q3 annualized sales less modeled ADESA production, not measured same-site output. Q3 seasonality and marketplace cars could bias the reference. Use actual full-year/quarterly reconciliation where available.
3. **Labor recovery:** 2025 establishment hours are observed but their link to production is assumed. Half the historical gap is assumed closed by the anchor and the rest by 2028. No further 5% growth remains. Changing skill mix, repair intensity and reporting scope can alter the relationship.
4. **Future project pace:** three 2027 buildouts are disclosed; three every year thereafter and seven standard integrations annually are extrapolations. Hiring, managers, permitting, construction, logistics and demand must support both programs simultaneously.
5. **Ramp versus nameplate:** nine months for standard integrations and eighteen for full buildouts are analog-informed assumptions. Reaching and sustaining full nameplate across every site is not independently demonstrated; downtime/seasonality could lower annual production.
6. **Property eligibility and overlap:** the working 56-property population and 21-site roster are reconstructed. Remaining properties are assumed suitable. Full-buildout slots are not assigned verified sites; confirm their 40k increments do not overlap standard capacity or reallocated production.
7. **No within-category productivity upside:** deliberately omitted; this is potential upside, but omitting it does not make every other assumption conservative. More demanding vehicle mix could reduce throughput.

Ready to build: transparent conditional volume case and sensitivity framework. Not ready to assert: validated site utilization, marginal ROIC, profitability of all incremental sales or robust valuation upside. The full financial model should add revenue-stream separation, variable/fixed recon and logistics costs, hiring/ramp expenses, project cash schedules, working capital, loan-sale economics, ownership/dilution, taxes/TRA and a terminal-multiple sensitivity. No further broad data collection is necessary just to begin that model; unresolved inputs should remain visibly adjustable.

## Reproduction

Run `python3 research/valuation/preliminary-dcf-2026-11-01.py`. [JSON output](preliminary-dcf-2026-11-01.json) preserves annual cash flows and valuation sensitivities. Tests reconcile the nine-year horizon, 2035 volume and the previously discussed $96.20 result. These are arithmetic checks, not independent forecast validation. No licensed raw reports are committed.
