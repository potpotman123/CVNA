# Merge prompt: wire the loan-thesis tabs into the company three-statement model

**As of November 1, 2026.** Workbook: `CVNA Model v3.xlsx` (company model). The workbook is not in this repository; get it from the team directly. It already contains the loan-thesis tabs (`Model`, `Subsidy`, `ABS`, `Deal econ`, `Evidence`, `Shorts`, `Notes`), copied from `CVNA-loan-thesis-model-v4.xlsx`. A cell-by-cell comparison on November 1 found them identical to v4 apart from floating-point rounding and one ABS header label ("Sprd (I)" vs "Sprd (I-curve)").

The tabs are present but **not connected**: no formula on `3SM` reads `Model`, and no formula on `Model` reads `3SM`. Instead, `3SM` re-types the loan levers as hard-coded inputs, and those hard-codes use different growth mechanics (see "Why this merge matters" below). This document tells another LLM how to connect them.

---

## Prompt (paste this into the other LLM along with the workbook)

> You are editing `CVNA Model v3.xlsx`, an Excel model of Carvana (CVNA). Two builds live in it:
>
> 1. **Company build**: `Volume Summary` → `3SM` (three-statement model) → `WACC + Reverse DCF` → `Cover`. Retail units come from the capacity build; revenue is split into retail, wholesale and "other". The P&L, balance sheet, cash flow and valuation all sit downstream of `3SM`.
> 2. **Loan-thesis build**: the `Model` tab forecasts the "other sales and revenues" line (gain on loan sales + VSC commissions + GAP/insurance/other) per retail unit. `Subsidy` and `Deal econ` read from `Model`.
>
> Your job is to make `Model` the single source of the four per-unit finance drivers on `3SM`, and to make `3SM` the single source of units, revenue, gross profit and adjusted EBITDA on `Model`. Follow the instructions in this document exactly. Do not change any lever value, any historical value, or anything outside the cells listed. Do not create circular references. Read the whole document before editing, make the edits in the order given, then run every check in the "Checks" section and report the results. If a check fails or a cell is not where this document says it is, stop and report it instead of improvising.

---

## 1. Layout of the two tabs

### `3SM` columns (header row 4, units in column B)

| 3SM col | Period | | 3SM col | Period |
|---|---|---|---|---|
| C | FY2024A | | N | 1Q27E |
| D | 1Q25A | | O | 2Q27E |
| E | 2Q25A | | P | 3Q27E |
| F | 3Q25A | | Q | 4Q27E |
| G | 4Q25A | | R | FY2027E (formula: sum or ratio of N:Q) |
| H | FY2025A | | S | FY2028E |
| I | 1Q26A | | T | FY2029E |
| J | 2Q26A | | U | FY2030E |
| K | 3Q26A | | V | FY2031E |
| L | 4Q26E | | W | FY2032E |
| M | FY2026E (sum or ratio of I:L) | | X–Z | FY2033E–FY2035E |

`3SM` has **no quarterly 2028**. FY2028 onward is annual.

### `Model` columns (header row 1)

C–I = 2Q23A–4Q24A, J = FY24A, K–N = 1Q25A–4Q25A, O = FY25A, P–R = 1Q26A–3Q26A, **S = 4Q26E**, T = FY26E, **U–X = 1Q27E–4Q27E**, Y = FY27E, **Z–AC = 1Q28E–4Q28E**, AD = FY28E, **AE–AK = FY29E–FY35E**, AM = basis/source notes.

### Column map (use this for every link)

| 3SM | Model | Period |
|---|---|---|
| C | J | FY24A |
| D, E, F, G | K, L, M, N | 1Q25A–4Q25A |
| H | O | FY25A |
| I, J, K | P, Q, R | 1Q26A–3Q26A |
| L | S | 4Q26E |
| M | T | FY26E |
| N, O, P, Q | U, V, W, X | 1Q27E–4Q27E |
| R | Y | FY27E |
| S | AD | FY28E (Model also has quarters Z–AC; 3SM does not) |
| T, U, V, W, X, Y, Z | AE, AF, AG, AH, AI, AJ, AK | FY29E–FY35E |

### Units

- `3SM` row 8 retail units are in **thousands**; `Model` row 4 retail units are in **units**. Multiply by 1,000 going 3SM → Model.
- Both tabs hold per-unit figures in **$ per retail unit**; `3SM` builds them as `$mm / 000s × 1000`. No conversion is needed for per-unit links.
- Dollar lines are $mm on both tabs.

### Rows involved

| Tab | Row | Line |
|---|---|---|
| 3SM | 8 | Retail Units Sold (000s); forecast = `IF(Vol_Link=1, row 7 capacity build, growth)` |
| 3SM | 18 | Loan Originations ($mm) = units × row 19 / 1000 |
| 3SM | 19 | Originations per Retail Unit ($), **forecast currently `prior-year same quarter × (1 + row 20)`** |
| 3SM | 20 | % Growth (YoY), hard-coded 1.4% (2027 quarters), 1.9% (FY28), 0 after |
| 3SM | 21 | Loan-Sale Margin, **hard-coded** 7.41% (4Q26) … 7.82% (FY29+) |
| 3SM | 22 | VSC Commission per Retail Unit ($), **forecast currently `prior-year same quarter × (1 + row 23)`** |
| 3SM | 23 | % Growth (YoY), hard-coded 3.21% |
| 3SM | 24 | GAP / Insurance / Other per Retail Unit ($), **hard-coded 354** |
| 3SM | 47 / 48 / 49 / 50 | Gain on loan sales / VSC commissions / GAP & other / Other sales & revenues ($mm) |
| 3SM | 52 | Total Revenue ($mm) |
| 3SM | 69 | Gross Profit ($mm) |
| 3SM | 111 | Adjusted EBITDA ($mm, model-built) |
| 3SM | 113 | Memo: Company-reported adjusted EBITDA (historicals only) |
| Model | 4 | Retail units (yellow placeholders in forecast columns) |
| Model | 5 / 6 / 7 | Net sales and operating revenues / Gross profit / Adjusted EBITDA (Kendall link block) |
| Model | 10–13 | Thesis levers (blue inputs): margin change (bp), originations-per-car growth, VSC growth, GAP change ($) |
| Model | 16 / 17 / 18 / 19 | Originations per car ($) / Loan-sale margin / VSC per car ($) / GAP-insurance-other per car ($) |
| Model | 21–25 | Originations, gain, VSC, GAP-other, other revenue ($mm) |
| Model | 26 | Other GPU ($ per retail unit) |
| Model | 32–36 | Street comparison (Bloomberg EE); leave alone |
| Model | 39–44 | Share-of-P&L statistics, which read rows 5–7 |

---

## 2. Why this merge matters (what is wrong today)

`3SM` re-types the loan levers, but grows originations per car and VSC per car **year-over-year off the same quarter of the prior year**. `Model` compounds them **sequentially from the latest quarter** (3Q26), at `(1 + annual growth)^0.25` per quarter. The two methods give different per-car levels. The values below were computed from the v3 workbook on November 1, 2026:

| Quarter | Originations per car, 3SM today | Originations per car, Model | VSC per car, 3SM today | VSC per car, Model |
|---|---|---|---|---|
| 4Q26E | $22,181 | $23,838 | $605.9 | $579.6 |
| 1Q27E | $23,019 | $23,919 | $611.4 | $584.2 |
| 2Q27E | $24,414 | $24,000 | $591.0 | $588.8 |
| 3Q27E | $24,172 | $24,082 | $593.5 | $593.5 |
| 4Q27E | $22,491 | $24,164 | $625.4 | $598.2 |

The 4Q gap (about 7% lower loan size in `3SM`) comes from carrying 4Q25's loan size ($3,627mm ÷ 163.522k units, 10-K less 9M) forward. The loan thesis is that loan size per car is held at the 3Q26 level and grows with car prices. Linking levels, rather than re-typing growth rates, removes the inconsistency and leaves one place to change each lever.

The margin path (row 21) and GAP ($354 vs $353.76) already match `Model` to rounding. They are still hard-codes, so a lever change on `Model` would not flow through.

---

## 3. Edits, in order

Colour convention (from `Cover`): green font = link to another sheet, black = formula, blue = historical input, red = projection input. Format every new cross-sheet link in **green font**. Keep number formats as they are.

### Step 1: Model ← 3SM (units and P&L context)

Forecast columns only. Leave historical columns C–R on `Model` exactly as they are (hard-coded actuals that already tie to `3SM`; see Checks).

| Model cell(s) | New formula | Notes |
|---|---|---|
| S4 | `='3SM'!L8*1000` | 4Q26E |
| U4, V4, W4, X4 | `='3SM'!N8*1000` … `='3SM'!Q8*1000` | 1Q27E–4Q27E |
| Z4:AC4 | `='3SM'!$S$8*1000*` *(existing Z4 ÷ existing SUM(Z4:AC4))* | Spread 3SM's FY28 total across quarters using the **current** Model seasonal shares. Compute each share from the existing hard-coded values **before** overwriting them, and paste the share as a constant in the formula, e.g. `='3SM'!$S$8*1000*0.2284`. Show the share to four decimals. |
| AE4:AK4 | `='3SM'!T8*1000` … `='3SM'!Z8*1000` | FY29E–FY35E |
| Z5:AC7 | leave blank | 3SM has no 2028 quarters. |
| S5 | `='3SM'!L52` | revenue, 4Q26E |
| U5:X5 | `='3SM'!N52` … `='3SM'!Q52` | |
| S6, U6:X6 | `='3SM'!L69`, `='3SM'!N69` … `='3SM'!Q69` | gross profit |
| S7, U7:X7 | `='3SM'!L111`, `='3SM'!N111` … `='3SM'!Q111` | model-built adjusted EBITDA |
| AD5 / AD6 / AD7 | `='3SM'!S52` / `='3SM'!S69` / `='3SM'!S111` | Replace the existing `IF(COUNT(Z:AC)=4, …)` FY28 formulas, because 3SM has only an annual FY28. |
| AE5:AK7 | `='3SM'!T52` … `='3SM'!Z111` (rows 52 / 69 / 111) | FY29E–FY35E (these cells are blank in v3). |

Leave `T`, `Y` (FY26E, FY27E) on `Model` as the existing sum formulas. They will now sum linked quarters.

### Step 2: 3SM ← Model (the four per-unit finance drivers)

Replace the forecast hard-codes and growth formulas with level links. Forecast columns only: L, N–Q, S–Z. Do **not** touch C–K, M or R (historicals and FY roll-ups that are already ratio formulas).

| 3SM row | Columns | New formula pattern | Example |
|---|---|---|---|
| 19 Originations per Retail Unit | L, N–Q, S, T–Z | `=Model!<col>16` | L19 `=Model!S16`; N19 `=Model!U16`; S19 `=Model!AD16`; T19 `=Model!AE16` |
| 21 Loan-Sale Margin | same | `=Model!<col>17` | L21 `=Model!S17`; S21 `=Model!AD17`; Z21 `=Model!AK17` |
| 22 VSC per Retail Unit | same | `=Model!<col>18` | L22 `=Model!S18`; Q22 `=Model!X18` |
| 24 GAP / Insurance / Other per Retail Unit | same | `=Model!<col>19` | L24 `=Model!S19` |

Then convert the growth input rows into memo formulas, so they still display growth but are no longer inputs:

| 3SM row | Columns | New formula |
|---|---|---|
| 20 (originations growth) | L, N–Q | same quarter prior year, e.g. L20 `=IF(G19=0,0,L19/G19-1)`, N20 `=IF(I19=0,0,N19/I19-1)`, Q20 `=IF(L19=0,0,Q19/L19-1)` |
| 20 | S | `=IF(R19=0,0,S19/R19-1)` |
| 20 | T–Z | prior column, e.g. T20 `=IF(S19=0,0,T19/S19-1)` |
| 23 (VSC growth) | same pattern on row 22 | |

Change the font of rows 20 and 23 in those columns from red (input) to black (formula). Add a note in column AB of rows 19, 21, 22 and 24: "Linked to Model tab (loan thesis). Change levers on Model rows 10–13, not here."

### Step 3: FY2028 consistency

`3SM` S19, S21, S22 and S24 now read `Model` AD16:AD19. Those are FY28 ratios built from `Model`'s quarterly 2028 columns, which after Step 1 are weighted by 3SM's FY28 units. Confirm that `'3SM'!S47` (FY28 gain on loan sales = `S18*S21`) equals `Model!AD22` within $1mm. Small differences from quarterly mix are acceptable. Report the difference.

### Step 4: do not change

- Any blue lever on `Model` rows 10–13. Rows 10–13 are the thesis inputs. Their sourcing lives in `Model` column AM and on the `Deal econ` tab (margin path: 3Q26 7.35% actual → +5.77bp/quarter through 4Q27 (Treasury pass-through) → +4.5bp/quarter through 4Q28 → 7.82% flat FY29+).
- `Model` row 11 (originations-per-car growth). It currently uses Street ASP growth as loan-size growth (`Notes` row 7). `3SM` row 12 holds Kendall's own retail-revenue-per-unit growth. Whether to replace `Model` row 11 with `='3SM'!<col>12` is a judgement call for the team. **Do not make it. List it as an open decision in your report.**
- `Model` rows 32–36 (Bloomberg Street comparison), the `ABS`, `Evidence` and `Shorts` tabs, and anything on `Volume Summary`, `Capacity Costs`, `ADESA Rollout`, `Original IRCs`, `Inputs & Sources`, `WACC + Reverse DCF` or `Cover`.
- Named ranges. `Vol_Link` and `Cost_Link` (on `Inputs & Sources` C7 / C8) must keep working.

---

## 4. Circularity check (reason it out before editing)

The links above are safe because:

- `Model` rows 16–19 (per-car drivers) in forecast columns depend only on the prior period's per-car value and the levers on rows 10–13. Historical per-car values depend on hard-coded actuals. **They do not read rows 4–7.** The one exception is the FY columns (T, Y, AD), which are ratios of `Model` totals and do read row 4. `3SM` only reads AD16:AD19 from those, and `3SM` row 8 (units) does not depend on anything in rows 18–24 or 47–50.
- `3SM` units (row 8) come from `Volume Summary` row 30 (when `Vol_Link = 1`) or growth inputs. `Volume Summary` reads only `'3SM'!M8` (FY26 units), and M8 = SUM(I8:L8), where L8 is a growth input. No finance line feeds units.
- `Model` rows 5–7 read `3SM` revenue, gross profit and EBITDA, which depend on the per-unit links. Rows 5–7 feed only the share statistics on `Model` rows 39–44 and `Subsidy` B17, B18 and B28. Nothing on `3SM` reads those.

After editing, turn on Excel's circular-reference warning (or check Formulas → Error Checking → Circular References). It must report none.

`Subsidy` and `Deal econ` keep their existing references to `Model` (Subsidy B4, B17, B18, B26–B28; Deal econ F66, G66, G72, G73, G76). Do not edit them. They will pick up 3SM units automatically.

---

## 5. Checks (run all, report each result)

1. **Historical tie (no edits expected).** For 3SM columns C–K vs Model J–R: units (3SM row 8 × 1000 = Model row 4), originations (18 = 21), gain (47 = 22), VSC (48 = 23), GAP & other (49 = 24), reported adjusted EBITDA (113 = 7). On November 1 every one of these tied exactly. Report any difference.
2. **Forecast tie.** For every forecast column, 3SM row 50 (other revenue, $mm) must equal Model row 25 within $1mm. Use the column map; for FY28 compare 3SM S50 with Model AD25.
3. **Other GPU tie.** 3SM row 25 must equal Model row 26 for L, N–Q, R, T–Z.
4. **Lever pass-through test.** Temporarily change `Model` U10 (1Q27 margin change) from 5.77 to 15.77. `3SM` N21 should rise by 10bp, and the rise should carry into O21–Q21, R21, S21 and T21:Z21. `3SM` N47 should rise by about `N18 × 0.0010`. Then restore 5.77 and confirm everything returns to its prior value.
5. **Balance sheet and cash.** `3SM` row 156 (balance check) and row 197 (cash check) must be 0 in every column.
6. **No new errors.** No `#REF!`, `#VALUE!`, `#DIV/0!` or `#NAME?` anywhere in the workbook that was not there before.
7. **No circular references.**
8. **Report the change in key outputs**, before vs after: 3SM FY27E and FY28E Other Sales & Revenues (row 50), Other GPU (row 25), Adjusted EBITDA (row 111), and `Cover` C10 (reverse-DCF implied share price). Expect 4Q26E and 4Q27E gain on loan sales to rise, because loan size per car moves from the 4Q25 base to the 3Q26 base. Explain any other material move.

---

## 6. What to send back

- The edited workbook saved as a **new file** (`CVNA Model v4 (merged).xlsx`). Never overwrite v3.
- A short change log: each cell or range edited, old content → new content.
- The result of each check in Section 5.
- Open decisions: at minimum the `Model` row 11 ASP-growth question, and any cell this document points to that did not hold what it describes.

---

## Provenance

- Structure, formulas, values and the per-car comparison in Section 2 were read from `CVNA Model v3.xlsx` (received November 1, 2026) and `CVNA-loan-thesis-model-v4.xlsx`, with formulas evaluated by a script. The workbooks are not committed because they contain Bloomberg-derived Street estimates (`Model` rows 32–34; `ABS` tab).
- The 4Q25 loan-size base is $3,627mm of originations ÷ 163,522 retail units: Carvana FY2025 10-K less 9M25 10-Q, as entered in both workbooks.
