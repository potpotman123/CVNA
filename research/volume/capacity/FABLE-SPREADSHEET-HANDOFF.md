# Fable handoff: Carvana capacity-to-retail-volume side build

Prepared November 1, 2026. Deliverable requested here is an implementation brief, not a new workbook. Build a concise, editable Excel module that feeds annual retail units into the team's existing revenue model. Preserve unrelated workbook content. Do not rebuild the DCF or select valuation assumptions.

## 1. What to build, and the order of authority

Explain this chain with visible calculations:

**Existing-site labor recovery + ADESA integration ramps + incremental major buildouts → conditional production → inventory / marketplace bridge → retail units → retail revenue.**

First reproduce the accepted volume scenario exactly. Then expose its assumptions and the production-to-sales reconciliation. Do not replace the agreed scenario with new research, unsupported productivity growth, or assumptions chosen to exceed consensus. This scenario does not establish profitable demand.

Order of authority:
1. Current instructions in this document and the user's subsequent directions.
2. Latest `volume-bridge-2026-11-01.json` and its Python calculation for production.
3. Latest cohort/pipeline source files for detailed dates and site membership.
4. `consensus-comparison-2026-11-01.*` for the updated wholesale/business split, and `cost-layer-2026-11-01.*` for the separate cost schedule.
5. Older handoffs for provenance only. Some retain superseded 12-month ramps, 5% labor growth, earlier opening schedules and different totals. Do not reuse those versions.

The final production endpoint is **2,350,632 in calendar 2035**, not 3 million. The same projects at full ramp support approximately **2,500,632 annually**, holding other groups flat. Neither is verified demand or a measured engineering ceiling.

## 2. Design references inspected

Reference workbooks are local design examples, not CVNA evidence. Do not copy their financial assumptions, formulas, company names or licensed source data into this project or Git.

| Reference | Specific inspected area | What to adopt |
|---|---|---|
| `/Users/kwu/cprt/raw/reference/TeamBDCModel.xlsx` | ` (READ ME) UF6 Conversion Build`, B2:J33 and supporting formulas; `(READ ME) Refrigerants Build`; `RPM` | Output-first schedules, visible cohort contributions, aligned annual columns, navy section headers, white space, short explanatory notes to the right. UF6 labels use a wide column B (~53 Excel units), numeric columns ~13, and frozen labels/header. |
| `/Users/kwu/Downloads/2L Capital - Daniel Bao.xlsx` | `OpModel`, especially C85:O111; `IS`; `SUM` | Small readable steps from quantity drivers to revenue; indentation distinguishes inputs, intermediate calculations and totals; restrained navy `#002060`, Arial 10, gridlines off, comments in a separate right-hand column. |

TeamBDC predominantly uses Garamond 11 with navy `#0E2841` / blue `#215E99`. The 2L model predominantly uses Arial 10. These observations come from workbook cell styles, structure and formulas, not a completed native Excel visual review. Fable must inspect the rendered target workbook before final delivery.

For the current CVNA workbook, preserve its existing purple headers and serif font if integrating directly. Use the references for hierarchy and clarity rather than importing a conflicting color theme. If delivering standalone, use Garamond 11 and navy `#0E2841`. Never mix multiple fonts/palettes merely because both examples use them.

Do not reproduce separator-only tabs, blank graph sheets, formatting extending to row 1000, or unrelated scratch sheets. Adopt useful structure, not every artifact in the examples.

## 3. Workbook architecture: five tabs, no decorative cover

Order: **Volume Summary → Original IRCs → ADESA Rollout → Capacity Costs → Inputs & Sources**.

Every tab opens with its answer/annual totals, followed by supporting calculations. Keep common years aligned. Inputs live once in Inputs & Sources; build tabs link to and visibly display only the drivers needed to understand that calculation. Summary links directly to build outputs. Do not route finished outputs back through assumptions.

### Shared layout and presentation rules

- Annual main view: B = description (width 46–54), C = units (width 10), D = 2024A, E = 2025A, F = 2026E, G:O = 2027E–2035E. Adjust slightly to the host workbook rather than forcing these addresses.
- Row 2 title; row 3 purpose/units and model date; row 5 historical/forecast grouping; row 6 annual headings. Freeze at G7 so descriptions and context remain visible. Do not put the Q3 annualized reference in F as though it were full-year 2026.
- One blank column after the annual schedule; short Notes column ~35–45 wide. Put long sources in Inputs & Sources, with a short source ID in Notes.
- White background, gridlines off, dark header bars with white text, bold subtotal labels, thin top borders on key totals. Avoid boxes around every cell. Indent supporting rows one level.
- Numeric data right aligned; labels left aligned. Units are vehicles (whole units), hours (whole hours), dollars/car, and $m for financial outputs. Do not mix millions of vehicles with whole vehicle calculations without explicit conversion.
- Actual/input hardcodes blue; formulas black; within-workbook cross-tab formulas green if consistent with host conventions. Pale yellow only for editable assumptions, not every number. Explain the legend once. Use text classifications as well as color.
- Historical, forecast and reference periods must be explicitly labeled. Missing observations display “Not disclosed” in data/status fields, not invented zero observations. An intentional zero assumption is permitted but must say “Assumed zero.”
- Main summary approximately 40 rows; each build's top section about 30–45 rows. Detailed site/project records may continue below, grouped/collapsible. Monthly support belongs to the right of annual support with a narrow separator and one clear heading; don't shrink 120 months onto the main printed page.
- Summary landscape, one page wide and readable at normal zoom. Detail can span multiple pages vertically. Restrict print areas; never force the entire facility register onto one page.
- Keep one optional case selector, not multiple editable copies. Start with the approved Base only; add sensitivities once Base reconciles. Do not clone the entire forecast for each case.

## 4. Data manifest and source priority

All paths below are repository-relative and exist at preparation. Local reports/workbooks are not required for reproducing the saved volume arithmetic.

| File | What Fable reads |
|---|---|
| `research/volume/capacity/volume-bridge-2026-11-01.json` | `anchor`, `assumptions`, `original_sites`, `annual`, `project_register`, `sensitivities`, `provenance` |
| `research/volume/capacity/volume-bridge.py` | Authoritative current formula logic, including quarter-average baseline, hours recovery and planning bounds |
| `research/volume/capacity/labor-recovery-calculations-2026-11-01.json` | Matched 2022–2025 establishment hours and site-specific historical gaps |
| `research/volume/capacity/staffing-panel-data.json` | OSHA observations, establishment IDs, addresses, period definitions and source provenance |
| `research/volume/capacity/adesa-cohort-build-2026-11-01.json` | `rows`: 21 candidates, proxy dates, fixed cohort labels, capacities and output; `summaries` |
| `research/volume/capacity/adesa-cohort-build.py` | Exact calendar-month linear-ramp implementation |
| `research/volume/capacity/adesa-future-pipeline-2026-11-01.json` | 35 property records, scenario `slots`, standard integration production, planning references |
| `research/volume/capacity/adesa-future-pipeline.py` | Anonymous start cadence and partial final cohort |
| `research/volume/adesa-21-site-candidate-roster.json` | Original evidence dates and source URLs; not a company-certified census |
| `research/volume/capacity/facility-register.json`, `original-irc-inputs.json` | Facility context and unresolved engineering fields; do not convert acreage into production |
| `research/volume/capacity/adesa-peer-ramp-evidence-2026-11-01.md` | Aramis analogue supporting assumed 9/18-month timing; not a measured CVNA ramp |
| `research/valuation/cost-layer-2026-11-01.json` and `.py` | Cost assumptions, annual costs, project cash schedules and sensitivities |
| `research/valuation/consensus-comparison-2026-11-01.json` and `.md` | Latest separate wholesale forecast and consensus comparisons; takes priority over earlier proportional wholesale shortcut |

Primary public source anchors:
- Q3 2026 retail units: https://investors.carvana.com/~/media/Files/C/Carvana-IR/documents/cvna-shareholder-letter-q3-2026.pdf
- Integration/buildout benchmarks and illustrative budgets, slide 6: https://investors.carvana.com/~/media/Files/C/Carvana-IR/reports-and-presentations/jp-morgan-auto-conf-aug-2026.pdf
- Q3 expense classifications: https://www.sec.gov/Archives/edgar/data/1690820/000169082026000067/cvna-20260930.htm
- Site-specific sources remain attached to records in the JSON files. Preserve them; do not replace them with a generic homepage.

Inputs & Sources should hold source ID, metric, value, unit, relevant period, facility/population, classification (reported/derived/proxy/assumed/unknown), file or URL, page/section where known, and short limitation. Preserve raw inputs separately from calculated targets. Do not imply independent sources when multiple reports describe the same tour.

## 5. Original IRCs: reconstruct the accepted labor calculation

Top annual output: recovery cohort; other originals; total original production; annual hours; additional modeled output versus baseline. Supporting site table: 18 rows, stable IDs, name, 2022 hours if available, 2025 hours, positive gap, assumed closure, baseline allocation and annual output.

Baseline:
- Q3 2026 retail sales = **217,385**, ×4 = **869,540**. This is a quarter-average annualized reference, NOT FY2026 sales/production and NOT Q3 exit production.
- Existing ADESA modeled Q3 production ×4 = approximately **220,826**; derive from the same July–September interval, not October 1 exit rate.
- Original-network residual = approximately **648,714**. This is an assumed allocation, not observed original-IRC production.
- 18 original sites: **14,651,510 hours in 2025**. Fourteen matched historical sites; ten have positive gaps totaling **2,127,888 hours**. Other eight = four at/above historical hours plus four missing matched history.

Per site i:
1. Matched-site gap `G_i = MAX(H2022_i - H2025_i, 0)`.
2. For unmatched sites, preserve missing historical data; the credited model gap is zero by explicit conservative assumption, not a finding of zero headroom.
3. Baseline adjusted hours `W_i = H2025_i + 50% * G_i`.
4. Allocated annualized production `P_i0 = OriginalResidual * W_i / SUM(W_i)`.
5. Average-year closure = **75% in 2027, 100% from 2028 onward**.
6. Production `P_iy = P_i0 * (H2025_i + closure_y * G_i) / W_i`.

The 50% starting closure and recovery dates are assumptions. Output scales linearly with establishment hours, with constant repair mix/productivity implicitly assumed. OSHA hours are not direct technician hours. No 5% annual growth after recovery. Other eight remain flat; this is not proof they cannot expand. Preserve the source code's 1m original-network planning limit and show unconstrained output and any bound adjustment separately; no adjustment binds in Base.

## 6. ADESA Rollout: cohorts and exact ramps

Top annual rows: 16 existing mature standard integrations; five existing ramping integrations; future standard integrations; major incremental buildouts. Below: the 21 candidate site rows, future start slots, major project register. Show annual capacity separately from annual realized production.

**Fixed cohort labels:** for reconciliation use maturity as of Q3 2026 throughout all forecast columns. The five ramping sites stay in the “2026 ramp cohort” contribution row even after they mature. Optionally show a separate current-status field. Never count the same site again in a mature contribution row.

Existing standard integrations: **13,000 annual units/site**, zero-to-100% linear ramp over **nine months**. Dates are generally announcement proxies. Five 2026 starts:

| Site | Proxy start | 2027 modeled units | 2028 units |
|---|---|---:|---:|
| Syracuse | 2026-04-28 | 12,951 | 13,000 |
| Chicago | 2026-05-06 | 12,919 | 13,000 |
| Sarasota | 2026-06-24 | 12,539 | 13,000 |
| Brasher’s / Sacramento | 2026-09-01 | 11,495 | 13,000 |
| Charlotte | 2026-09-15 | 11,201 | 13,000 |

Use unrounded source results. The mature 16 contribute 208,000 from 2027 onward; all existing 21 contribute 273,000 once mature.

Remaining estate: **35 properties**, including Orlando (October 6, 2026 proxy) and **34 anonymous future slots**. Seven starts/year 2027–2030, six in 2031. Maintain the seven-per-year spacing even in that last partial year. Working estate: 56, with Queen City excluded pending status; do not call this an independently confirmed acquired-property count. All properties' suitability remains assumed.

For year Y and slot j starting at zero, the future standard start index is `12*Y + (j+0.5)*12/7`. These are evenly spaced fractional calendar months, not January 1 cohorts. Use numeric indices directly; rounding them to dates can change results.

Major buildouts: **three production starts/year, 2027–2035**, April 1 / July 1 / October 1. Total **27** slots. Only the initial three-project 2027 cohort is company-reported; its within-year dates and every later cohort are assumptions. Each adds **40,000 incremental annual units**, with an **18-month linear ramp**. Site identities/compatibility are unresolved. Do not invent names. Treat slots as distinct eligible properties within the estate, not new properties outside it.

If 40,000 is genuinely incremental to an existing 13,000 integration, mature combined capacity is 53,000. If later engineering evidence reports a total rather than an increment, change scope explicitly, not silently. Preserve the ~2m ADESA planning boundary in the code (major additions capped at 2m less 728k standard capacity); Base does not bind it. It is a planning reference, not proven physical capacity. Do not add the mechanical all-56-buildout upside to scheduled projects.

### Exact ramp equations for Excel

Use simple helper columns, not a single opaque nested formula. For a real date d:

`MonthIndex(d) = 12*YEAR(d) + MONTH(d)-1 + (DAY(d)-1)/DAY(EOMONTH(d,0))`

For annual capacity C, ramp months R, age a in equal calendar months:

```
Age = MAX(0, PeriodBoundaryIndex - StartIndex)
RampAge = MIN(Age, RampMonths)
CumulativeUnits = AnnualCapacity/12 * (RampAge^2/(2*RampMonths) + MAX(0, Age-RampMonths))
PeriodProduction = CumulativeUnitsAtEnd - CumulativeUnitsAtStart
```

Calendar year boundaries are `12*Y` and `12*(Y+1)`. Monthly output uses consecutive integer boundaries. This integrates the ramp exactly; do not apply month-end utilization to the whole month. For zero ramp, use a separately guarded immediate-full-rate formula to avoid division by zero. Negative age contributes zero. A Jan 1 standard opening produces **8,125 vehicles in its first 12 months**, then 13,000 in a fully mature calendar year. No 90% endpoint. No automatic equal output for new and mature sites.

## 7. Volume Summary and revenue handoff

Suggested rows:
- 8–16: six production cohorts, total modeled production, growth.
- 19–26: reconciliation from modeled production proxy to retail sales.
- 29–33: final retail units (bold, pale output shading), growth, optional consensus and difference.
- 36–40: concise assumptions and model status. One stacked annual production chart below, not six small charts.

Historical rows contain reported retail sales, not invented site production: 2024 **416,348**; 2025 **596,641**. Q3 2026 **217,385** and the **869,540 annualized reference** belong in a separate calibration box. A FY2026 estimate is a separate input; do not substitute that annualized reference. Supplied consensus snapshot is 820,413 FY2026 retail units, not a company actual or this model's production result. If used, mark its source/date explicitly. Calculate 2027 growth only against a legitimate FY2026 estimate.

For version 1, preserve the existing **sales-equals-modeled-production** scenario and show an explicit zero net bridge assumption. The starting reference already embeds marketplace sales and unknown inventory movements. Therefore, do not simply add a new marketplace forecast on top: that would risk double counting.

Show a bridge with clear inputs/status:
1. Modeled capacity-based production proxy.
2. Less embedded non-internal units correction, if identified (unknown, credited zero in replication mode).
3. Plus separately modeled marketplace retail units, if identified (zero in replication mode to avoid double counting).
4. Less change in sale-ready owned inventory (assumed zero in replication mode).
5. Plus/minus returns, dispositions and other reconciling adjustments where measured (assumed zero otherwise).
6. Retail units sold **conditional on absorption**.

If upgrading to an independently measured internal-production forecast, reconcile the anchor first and then use the physical inventory identity. Do not imply current zero adjustments are observations. A 95% absorption stress must show cumulative unsold inventory and required production response; it is not sustainable to leave that inventory growing indefinitely without consequence.

### Revenue model interface

Provide one clearly named annual output range, e.g. `CVNA_RetailUnits_Output`, with explicit year headings. Link main-model retail units directly to it. The existing main model owns pricing, not this module.

Simple revenue link: `RetailUnits * RevenuePerRetailUnit / 1,000,000` for $m. Label the price metric “reported retail revenue per unit,” not pure sticker price. Marketplace net/gross revenue accounting can affect it. If separating owned retail and marketplace, forecast gross owned sales and net marketplace fees separately with reconciled unit denominators.

Do not apply retail units to total company revenue. Owned wholesale vehicle sales, third-party auction fees, and loan-sale/ancillary revenue require their own schedules. Current consensus comparison replaces the earlier wholesale/retail ratio with owned-wholesale units of **504,780 / 599,196 / 689,835 in 2027/28/29**. These are supplied estimates, not independent forecasts; do not count auction transactions as acquired inventory or retail units.

## 8. Control totals: reproduce before changing assumptions

Rounded vehicles below; actual Excel calculations must use full precision from input logic, not hardcode this table. One-unit differences in rounded components are normal.

| Year | Recovery 10 | Other original 8 | Mature ADESA 16 | 2026 ramp cohort 5 | Future standard | Major additions | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2027 | 444,999 | 225,674 | 208,000 | 61,106 | 30,547 | 11,667 | 981,992 |
| 2028 | 466,958 | 225,674 | 208,000 | 65,000 | 115,375 | 90,833 | 1,171,840 |
| 2029 | 466,958 | 225,674 | 208,000 | 65,000 | 206,375 | 210,000 | 1,382,007 |
| 2030 | 466,958 | 225,674 | 208,000 | 65,000 | 297,375 | 330,000 | 1,593,007 |
| 2031 | 466,958 | 225,674 | 208,000 | 65,000 | 388,331 | 450,000 | 1,803,963 |
| 2032 | 466,958 | 225,674 | 208,000 | 65,000 | 450,534 | 570,000 | 1,986,166 |
| 2033 | 466,958 | 225,674 | 208,000 | 65,000 | 455,000 | 690,000 | 2,110,632 |
| 2034 | 466,958 | 225,674 | 208,000 | 65,000 | 455,000 | 810,000 | 2,230,632 |
| 2035 | 466,958 | 225,674 | 208,000 | 65,000 | 455,000 | 930,000 | 2,350,632 |

Supplied retail consensus for 2027/28/29 is 1,040,187 / 1,228,260 / 1,461,650. Our current scenario is below these figures. Do not describe it as an above-consensus volume thesis. Consensus is a dated comparison, not a live data feed.

## 9. Capacity Costs: retain latest work, don't invent a finished valuation

Volume outputs must work independently of incomplete cost assumptions. Preserve the separately developed provisional cost schedule, clearly labeled as assumptions. This is phase two; do not delay the volume delivery to seek missing spending or technician data.

Top output rows: direct-labor memo; incremental labor/ramp cost; adjusted SG&A; standard CapEx; major CapEx; other CapEx; total CapEx; incremental working capital. Link these once to the appropriate main-model rows. No duplicate deductions from both GPU and SG&A.

Project CapEx: standard budget midpoint **$2.5m** (range $2–3m); major **$32.5m** ($30–35m). Spend linearly over **six / twelve months before production start**, respectively, as assumed in the cost layer. These clocks differ from the nine/eighteen-month production ramps. For year interval [A,B] and project spend interval [S-L,S], cash CapEx is:

`Budget * MAX(0, MIN(B,S)-MAX(A,S-L)) / L`

The modeled 35 standard plus 27 major budgets sum to **$965m**, including **$55.5m allocated through 2026** under assumed timing, not reported actual incurred spend. Keep project total, modeled incurred and modeled remaining spend separate. Known actual spending can replace these assumptions only with a reconciliation. Do not charge the three 2027 projects' whole budgets in 2027. Do not layer this spending on top of an existing companywide CapEx forecast that already contains it.

Other CapEx: $160m assumed baseline, half volume-linked, 3% annual inflation; use the exact existing script's baseline and year offsets. This replaces the old 1%-of-sales shortcut. It is not disclosed maintenance CapEx. Total CapEx controls: **$290.5m in 2027, $314.3m in 2028, $341.4m in 2029**. The 2035 drop reflects no scheduled 2036 cohort; do not carry that artifact into terminal cash flow.

SG&A: Q3 GAAP $805m less SBC $24m and D&A $39m = **$742m adjusted**, annualized for calibration. Categories: compensation $255m; advertising $152m; occupancy $18m; logistics $68m; other $312m, before adjustments. Use JSON adjusted category allocations; D&A allocation is assumed. Variable shares 80%/90%/40%/90%/60%; fixed costs inflate 3%, variable unit costs flat in Base. Annual category cost is baseline adjusted quarterly cost ×4 × [variable share × volume ratio × variable-cost inflation factor + fixed share × fixed inflation factor]. Do not confuse adjusted output with GAAP cash flow.

Labor memo assumptions: 8 paid hours/car, $35/hour, 30% burden, 2,000 hours/FTE, 3% wage inflation; 50% excess hours during ramp; two months preopening at 25% mature staffing. All are illustrative, not measured CVNA technician productivity. Normal labor is already in baseline GPU: deduct only the incremental inflation/ramp overlay once. FTE equivalents are not gross hiring needs. Keep original-IRC OSHA recovery and this technician-cost assumption distinct.

Working capital: existing $4,200 per incremental annual unit is an unvalidated placeholder. Do not also deduct separately modeled gross inventory investment without replacing/reconciling that placeholder. A proper inventory-days model is a later refinement. Do not push the provisional cost output directly into UFCF without reconciling taxes, SBC, depreciation, leases, financing and noncontrolling ownership treatment.

Use `consensus-comparison-2026-11-01.*` for the latest wholesale earnings replacement. Do not add wholesale GP again to a total-GPU forecast that already includes it. Preserve both cost-only controls and the later business-split reconciliation so the reviewer can see why EBITDA changes.

## 10. Acceptance checks and delivery

Arithmetic checks, shown compactly below the relevant schedule:
- 18 originals = 10 recovery + eight other; preserve missing-history classifications.
- 21 existing candidates = 16 + five; 35 remaining = Orlando + 34 slots; 56 total standard properties. Orlando appears once.
- Positive historical gap = 2,127,888; original allocation plus quarter-average ADESA anchor = 869,540.
- Mature standard output = 13,000/site; first rolling year = 8,125; existing 21 = 273,000; remaining 35 = 455,000; all standard = 728,000.
- 27 unique major slots; mature incremental capacity = 1,080,000; calendar 2035 contribution = 930,000.
- Annual cohort sums match JSON to less than one displayed vehicle, with full-precision underlying tolerance; the output table is a check, not a hardcoded forecast.
- Dates before opening generate zero production; mature sites never exceed their modeled capacity absent an explicit expansion; monthly output sums to annual output.
- Inventory bridge balances and does not double-count marketplace sales. 2026 annualized reference is never used as FY2026 actual.
- CapEx schedules allocate each project budget exactly once, including modeled pre-forecast spend. Costs appear in one accounting location only.
- No broken links, circular formulas, Excel errors or missing-input-to-zero conversions. Check formulas in early, middle and final years.

Behavior checks: change standard capacity, shift a proxy start three months later, set future starts to zero, remove major projects, and set historical gap recovery to already complete. Confirm affected outputs change and unaffected history does not. Restore Base. Do not cap away an error to force a pass. Calibration to sales is not independent validation of site output.

Visual checks: inspect every tab at normal zoom; no clipped labels, microscopic footnotes, mismatched units, blank charts or excessive horizontal scrolling in the main annual view. Render the top section of each tab and verify the print/export view. Main output must be understandable in 30 seconds; site details must remain traceable without a verbal explanation.

Deliver: one editable workbook/module, a short list of main-model output links, and a concise open-items note. Do not deliver multiple near-identical versions or reproduce licensed reports. Save the final workbook in the user-designated location and commit only authorized project artifacts. This handoff itself belongs in Git; the reference spreadsheets remain outside the repository.

The unresolved items are starting internal production versus marketplace/inventory, true site production-start dates, future property suitability, named buildout scopes, customer absorption and actual spending-to-complete. They must remain visible, but they do not prevent implementing the agreed conditional volume scenario now.
