# Carvana research handoff: profitable volume, IRC headroom and loan-sale economics

**As of October 31, 2026. Financial endpoint: Q3 2026.**

This document is a continuity guide for another researcher/model. It consolidates the questions, completed research, evidence quality, corrections, unsuccessful routes and next work. It is not a recommendation to buy or short CVNA. Statements described as company claims, analyst estimates or hypothetical scenarios must retain those labels.

Repository: `/Users/kwu/Documents/ChatGPT/$CVNA`
Remote referenced by the user: `https://github.com/potpotman123/CVNA.git`. This handoff does not verify remote synchronization or imply these files have been committed/pushed.

## 1. Start here

### Central investment question

**How much more desirable inventory can Carvana economically acquire, prepare and deliver using its existing and planned infrastructure—and what evidence shows customers will absorb it at acceptable returns?**

The user is considering two connected investment questions:

1. **Volume sustainability:** Why did retail volume grow so quickly from 2024 through Q3 2026? How much reflects operational capacity recovery/expansion, new locations, better execution, easier vehicle mix, financing concessions, demand or market-share gains? How much repeatable runway remains?
2. **Financing economics:** Why do loan buyers pay prices that support substantial gains on sale? Are those gains economically supported, vulnerable to repricing, or dependent on related-party arrangements? What is a defensible normalized margin?

The active emphasis in this side conversation is **IRC operating and physical headroom**. Loan-sale work exists in parallel and matters because financing affects both demand and the apparent returns from adding production capacity.

### Current conclusion

- Substantial physical optionality is supported by the pre-existing IRC network, acquired ADESA properties and relatively inexpensive light integrations.
- Expansion of an executable operating system—trained staff/managers, balanced repair workflows, appropriate vehicle mix and logistics—is more plausible than a simple national shortage of land as the recent constraint.
- Existing-site employment recovery is measured. Its causal contribution to production is not, because a matched site staffing/output panel is still missing.
- The new sellside material supplies an Elyria production benchmark and specific process mechanisms. It does not solve the historical staffing/output identification problem.
- Later-model cars can increase throughput by reducing work per vehicle. This must be separated from genuine within-category productivity gains.
- Companywide volume and profit are growing, but profit per retail unit has declined. Additional output is not automatically equally profitable output.
- Network utilization claims and empty parking spaces do not establish economically executable production headroom.
- No economically unsupported loan purchase or related-party subsidy has been established. Financing-margin compression is observed; sustainability and buyer returns remain only partly identified.

### Fast reading order

1. This handoff, especially sections 3, 6, 9, 12 and 13.
2. [Expanded sellside synthesis, October 31](research/sellside/2026-10-31-expanded-synthesis.txt).
3. [Capacity overview](research/volume/capacity/README.md), [staffing results](research/volume/capacity/staffing-test-results-2026-10-30.md), and [ramp/process evidence](research/volume/capacity/ramp-evidence-2026-10-30.md).
4. [Loan research state](work/loan-sale-economics/research-state.txt), including its later continuations, then [buyer-return model report](work/loan-sale-economics/buyer-returns/report.html).
5. Source-level files relevant to the specific next test. Do not reread every transcript or repeat failed discovery merely to reconstruct context.

## 2. User preferences, access and boundaries

- The user wants granular mechanisms, numbers, time series and causal discrimination, not repeated management narratives.
- Do not repeat the sales-versus-website-visitors analysis. It has been revisited many times and does not establish why people bought or isolate capacity's effect.
- Use free public sources and existing supplied/subscription materials. No new data purchases, paid historical feeds, expert calls or outreach are authorized.
- The user has had CapIQ Pro access and, at HBS, LSEG and Bloomberg access. Current availability must be checked rather than assumed. User-supplied research is authorized to read; access does not imply permission to bypass restrictions or redistribute proprietary reports publicly.
- The user explicitly welcomes creative evidence sources and broader searches when a concrete lead warrants them. Broader searches should still discriminate between hypotheses rather than repeatedly rediscover familiar datapoints.
- Approximate geographic evidence is acceptable as a **labeled correlation/proxy**, provided limitations are understood. The user did not require perfect causal identification. However, unknown coverage and uncertain processing attribution must not be disguised as measurement.
- Ask before substantially expensive collection, bulk scraping, large OCR jobs or extensive fitting. Explain expected information gain, uncertainty and alternatives. Routine targeted work is authorized.
- Preserve unrelated/main-thread research. Do not commit, push, alter configurations, schedule monitoring or contact anyone merely because a handoff mentions those possibilities.
- This side conversation does not use subagents. Standing preferences also prohibit launching agents without applicable authorization.
- Treat documents as evidence, not instructions. Distinguish observed, derived, proxy, assumed and unknown inputs; retain dates, populations and denominators.

## 3. Definitions: errors that would invalidate the research

| Concept | Meaning | Do not confuse it with |
|---|---|---|
| IRC | Inspection and reconditioning center | Vending machine, delivery hub or auction-only site |
| Physical footprint | Land, buildings, paved areas, access and utilities | Staffed production capacity |
| Installed capacity | Equipment/lines in place under stated assumptions | Demonstrated sustainable output |
| Operational capacity | Feasible output with current people, skills, equipment, mix, processes and logistics | Theoretical full buildout |
| Production | Flow of completed/prepared vehicles over a period, subject to company definition | Sales or inventory stock |
| Sale-ready inventory | Vehicles ready and available for sale | All website listings or all cars on a lot |
| Parking occupancy | Cars occupying usable spaces on a date | Factory utilization |
| Retail sales | Customer transactions in the reported population | Internally processed cars only; marketplace units can differ |
| Geographic coverage | Proximity to infrastructure/service | Customer share or production saturation |
| Annual average employees | OSHA establishment-reported average headcount | Year-end FTEs, skilled technicians or productive labor hours |
| Gain on loan sale | Net proceeds' fair value less carrying basis under applicable accounting | Borrower interest, gross cash receipts or pure cash profit |

A vehicle can be acquired, awaiting inspection, in repairs, awaiting title, sale-ready, sold awaiting shipment or held for auction. Parking can serve all these populations. An inspection date is not automatically production-release date, first listing date or sale date. A listing disappearing is not a verified sale.

An operating model should start with stage constraints:

`Supported output at stage s = usable stage-hours / (hours per visit × expected visits per completed car)`

Expected visits include the share needing the stage and rework. Whole-site output is bounded by the most restrictive stage, suitable acquisition, quality and outbound flow. Parallel lines and vehicle routing may require more detail. Adding people away from the bottleneck need not add output.

For parking/work in process, a stable-flow approximation is:

`Average vehicles occupying relevant spaces = daily throughput × average days occupying those spaces`

Use compatible populations and calendar/operating-day definitions. Peak buffers, mixed auction uses and uncertainty matter. Parking can constrain output, but space alone does not identify throughput without residence time.

## 4. How the research evolved

1. Began with a detailed 2025 10-K business/economics review: owned versus marketplace vehicles, retail/wholesale, sourcing, financing, servicing, loan sales and securitizations.
2. Focus shifted to explaining extraordinary retail-unit growth and forecasting its persistence rather than extrapolating recent growth.
3. Established market demand × market share framework, then focused on ADESA integrations as a potential supply/logistics mechanism.
4. Tried local before/after comparisons around integrations. Lack of a validated free buyer-local Carvana sales series prevented a credible treatment/control study.
5. Distinguished first-nearby-site effects from additional capacity in already-served metros. Original IRCs predate ADESA and must be included.
6. Reconstructed physical footprint, quarterly operating evidence, site ramps and conditional scenarios.
7. Tested employment recovery using official OSHA establishment data. Found substantial same-site recovery, but no matched output panel.
8. Piloted live/archived vehicle listings and history reports to infer processing geography and production timing. Found some useful fields, but not validated site assignments or reliable historical flows.
9. Audited archive coverage and public datasets. Historical panel feasibility remains unvalidated.
10. Reviewed 37 newly supplied sellside PDFs. Added site/process detail, an Elyria output observation, financing time series and a credit-basket composition test.
11. Latest discussion: quantify stage-level operating headroom, especially paint, AND independently assess physical expansion room across the network using a systematic facility/imagery/parcel census.

## 5. Business and macro framework retained from earlier work

`Carvana retail units = addressable retail transactions × Carvana share`

Keep dealer sales separate from all used transactions including private-party sales. Reconcile new-vehicle marketplace contribution where material. “Used-car e-commerce” is not a cleanly defined standalone market: online research, financing and purchase can overlap with physical dealerships.

CarMax is a useful comparator, not the whole market or an unaffected control. Match fiscal/calendar periods, credit profiles, car age/price and company-specific execution. Existing CarMax calls also provide operating comparisons for reconditioning ramps.

Candidate mechanisms for Carvana share gains: broader relevant selection, delivered price/payment, faster delivery, awareness/trust, financing availability, and operating execution. These interact and cannot simply be multiplied as separate growth drivers.

Retail gross profit excludes many costs below gross profit and is not income available to equity. Retail revenue per unit is not a clean sticker-price series because marketplace accounting can change gross versus net presentation. Financing and wholesale profits allocated per retail unit are not profit from preparing that specific car.

Core files: [volume framework](research/volume/README.md), [initial ADESA plan](research/volume/adesa-research-plan.md), [local proximity test](research/volume/adesa-local-proximity-test.md).

## 6. Physical footprint: completed findings and unresolved census issues

### Established context

- ADESA acquisition closed May 9, 2022 for approximately $2.2bn: 56 locations, about 6.5m square feet and more than 4,000 acres. This bought a business/property platform, not 56 fully operational retail IRCs.
- The original IRC network was already substantial. Q4 2024 commentary described potential above one million annual retail units; 2024 retail sales were 416,348. This is evidence of theoretical physical headroom, not proof the network could immediately produce a million cars economically.
- Reconstructed integrated ADESA count: six at year-end 2024, 16 at year-end 2025, 21 at Q3 2026.
- Named 21-site roster is a candidate reconstruction, not a company-certified census. Announcements are not necessarily production-start dates.
- Current register has 18 reconstructed original IRCs and 57 ADESA directory entries. The 57 versus 56 acquisition count is unresolved. These cannot be called 75 active retail factories.
- Q3 disclosures describe approximately 1.5m annual capacity at full buildout and real estate supporting approximately 3m. These are distinct readiness states.
- Three larger builds are expected to begin production in 2027. Jacksonville permitting independently indicates a substantial project, but its membership in that three-project cohort has not been established.

### Expansion routes

1. More staffing/shifts in installed facilities.
2. Light conversion of existing ADESA buildings.
3. Larger buildings/lines on owned properties.
4. Genuinely new greenfields.

Light integrations are described at approximately $2–3m for 13,000 incremental annual capacity; larger buildouts at $30–35m for 40,000. These are guidelines/analyst estimates with source-specific attribution, not audited returns. They exclude original acquisition cost and working capital. Do not count the same project capacity inside both same-site improvement and new-site contribution.

### Geographic examples

| Metro | Sites/context | Implication |
|---|---|---|
| Chicago | Original University Park; ADESA Hoffman Estates | Additional/different-side coverage, not first metro IRC |
| DFW | Original Blue Mound; ADESA Hutchins | Aggregate both when studying local staffing/production |
| Houston | No original metro IRC identified in reconstruction; original Texas sites elsewhere | Stronger first-local candidate, not first customer-market entry |
| Indianapolis | Original Greenfield; ADESA Plainfield | Overlap/different-side capacity |
| Phoenix | Tolleson; Chandler | Multiple labor/inventory catchments |
| Seattle / Kansas City | Auburn / Belton integrations | First-local candidates; no measured local sales uplift |
| Sacramento | Original Rocklin; Brasher's Rio Linda | Distinguish from separate ADESA Sacramento property |

ADESA properties provided logistics functions before retail integration, weakening their use as untreated controls. Vehicles can be processed in one metro and sold elsewhere. No validated road-distance/population coverage model has been completed.

Files: [register](research/volume/capacity/facility-register.md), [structured register](research/volume/capacity/facility-register.json), [site cards](research/volume/capacity/adesa-site-cards.json), [candidate 21 roster](research/volume/adesa-21-site-candidate-roster.json), [regional evidence](research/volume/adesa-regional-evidence-2026-10-29.md).

## 7. Operating capacity: evidence obtained

### National timing

- Management reported more than 40% production growth in 2025.
- Q2 2026 written chart reports 36% companywide production growth; call terminology differed, so preserve the discrepancy.
- Q3 production exceeded 200,000 and slightly exceeded retail sales. Do not invent an exact production figure or equate the reported lower bound to exact annual utilization.
- Late-2025 reconditioning cost pressure was associated with rapid expansion, newer managers and smaller/single-line sites.
- Early 2026 prioritized cost recovery, temporarily constraining inventory expansion. Labor hours per vehicle reportedly returned to prior best levels, but absolute/mix-adjusted hours are unavailable.
- Newer, higher-priced, easier-to-recondition cars became a deliberate lever in Q2; later-model/prime emphasis persisted in Q3.

### Site/process observations

- Citizens June 4, 2026 Elyria tour: approximately 1,280 vehicles produced weekly, four physical lines/two shifts. JPMorgan June 5 calls approximately 1,300 weekly capacity. Same event, different definitions; not independent samples or an audited production series.
- Haines City tour accounts describe lines and second-shift expansion but use physical lines and line-shifts inconsistently. DA Davidson prints 12,800 weekly capacity; visually checked and excluded as suspected error, not silently corrected.
- Morgan Stanley Haines “40% utilization” is approximately 6,000 cars / 15,000 parking spaces. It is NOT factory utilization.
- JPMorgan June tour relays management's approximately 50% average network utilization and no site at 100%. Denominators and distribution are unavailable.
- Management prefers two dispersed sites at 50% to one at 100% where logistics and access to separate labor pools outweigh fixed costs. Strategic slack is not necessarily inefficiency.
- New ROLLCALL/LEADERHUB tools were reportedly in three of 36 sites at the June tour; allocation visibility around 15 minutes versus 60–90 manual minutes. This is shift planning, not repair time per car.
- JPMorgan explicitly says initial cost recovery preceded new software benefits. Do not assign all historical gains to new tools.
- Paint routing, alternative cosmetic techniques, tiered mechanic skills and parts sequencing are concrete mechanisms. Stage targets are not whole-car cycle times.

### Creative/independent evidence already checked

- Tolleson supplier Rely-On/Garmat historical project: three four-booth paint lines rated 30 vehicles/day each; eight booths in phase one, later completion/current setup unverified. Conditional design, not observed current throughput.
- Carvana/Accenture Oracle CloudWorld presentation (September 2024): variable routing, parts tools, 47 possible work centers. Some graphic metrics were withheld because directions/context were not verified. Application users are not recon headcount.
- TBM anonymous reseller case: lead time 21 to five days and 80% smaller paint backlog claimed. Client not identified as Carvana; marketing evidence with inconsistent starting quality rates. Mechanism only.
- Manheim/US Auto Sales outsourcing example: external processing can add output without Carvana-style employee increases. Not evidence of current CVNA outsourcing share.
- CarMax FY2027 Q1: seven off-site centers still ramping; logistics benefits ahead of desired reconditioning economics. FY2026 Q4: older/higher-mileage vehicles need more recon time/cost.
- Former-operator Blue Mound testimony: historical three physical lines × two shifts versus two line-shifts in 2023; restart estimate approximately 120 days, maturation nearer six months. Retrospective, anonymous testimony, not current verified utilization.

Sources and caveats: [ramp evidence](research/volume/capacity/ramp-evidence-2026-10-30.md), [source test](research/volume/capacity/source-test-2026-10-30.md), [three-site test](research/volume/capacity/three-site-output-test-2026-10-30.md), [operating timeline](research/volume/capacity/operating-timeline.md).

## 8. Staffing: the strongest measured historical panel

Official OSHA data provide a constant-ID panel of 14 original IRC establishments for 2022–2025.

| Annual average employees | 2022 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|
| All 14 | 7,212 | 4,356 | 5,048 | 6,806 |
| Haines City | 716 | 296 | 350 | 486 |
| Elyria | 482 | 322 | 325 | 463 |
| Blue Mound | 756 | 400 | 398 | 523 |
| Winder | 665 | 371 | 407 | 465 |
| Chesterfield | 291 | 306 | 389 | 616 |

- Total employment rose 56.2% from 2023 to 2025; all 14 recovered from 2023.
- Ten older sites remained 22.9% below 2022 employment in aggregate; four younger/ramping sites expanded strongly.
- Seven of 14 were below 80% of 2022 employment in 2025. This is a selected-sample staffing comparison, not the share of all sites underutilized.
- Haines City's 2021 address-matched record had 487 employees, versus 486 in 2025. It was below 2022, but essentially back to 2021. Neither 2021 nor 2022 is pre-COVID. Do not describe 2022 layoffs as simply a pandemic shutdown.
- Annual reported hours: 13.020m / 7.410m / 7.245m / 12.684m. The 2024 hours/headcount divergence needs scope/schedule investigation; not a clean productive-hours series.
- Address/ID changes matter. Stricter eight-site sample still supports recovery, but is approximately back to 2022 staffing. Exact remaining gap is sample-sensitive.
- ADESA records excluded to avoid mixing auction and retail functions and duplicated records. Missing matches are not zero employment.
- Historical staffing does not establish efficient full staffing. Outsourcing and job mix further complicate output per employee.

**Missing:** matched site-year/week completed production, skill mix and repair requirements. No staffing/output regression or elasticity is valid yet. Do not divide nationwide sales by the 14-site workforce or June 2026 output by annual 2025 headcount.

Files: [results and full table](research/volume/capacity/staffing-test-results-2026-10-30.md), [data/provenance](research/volume/capacity/staffing-panel-data.json), [reproduction](research/volume/capacity/build-staffing-panel.py).

## 9. Historical local data attempts: do not restart these blindly

### Buyer-local sales

- Washington title dataset lacked VINs and seller identifiers required for a CVNA match. Seattle public-data feasibility did not produce a sales panel.
- Missouri dealer reports mix populations; not a valid proposed retail-demand comparison.
- No validated free historical local CVNA retail-sales series found.
- KMX comparisons must match geography, calendar, customers and execution; KMX alone is not a clean control.

### Vehicle listings and histories

- Same-VIN ZIP experiment changed pickup location, delivery timing and shipping charge. Pickup destination is not processing IRC.
- Carvana inspection modals/printouts expose inspection dates and VINs, but no verified processing location in the pilot.
- CARFAX/service histories give real towns and dates, but prior-owner service is sourcing geography, not processing geography.
- Montana/Helena title records can be administrative; do not infer physical vehicle travel.
- Two-car initial test plus three-car extension were convenience samples, all RAV4s. In the extension, 3/3 had prior-use towns and inspection dates; 0/3 identified a geographic Carvana processing event.
- DFW candidates include Blue Mound AND Hutchins. Massachusetts' one confirmed integrated site does not prove every Massachusetts-source vehicle is processed there.
- Approximate metro assignment is acceptable as a hypothesis only if local-routing assumptions are explicit; no calibrated assignment accuracy exists.

### Archive audit

Wayback CDX query returned 50,000 rows at its cap: URL-ordered, truncated, nonrandom. After filtering: 41,044 numeric-listing capture rows, 32,130 vehicle IDs; 78.9% had one capture row. Among repeated-day intervals, median gap 46 days; 62.4% exceeded 30 days. Replays did not yield a usable historical inspection/geography bundle; some dynamically assembled content was inconsistent.

These counts measure archive capture, not transactions. No regression or historical metro-flow chart was built. A capture timestamp is not listing arrival, and disappearance is not a sale.

Common Crawl selected October 2024/2025/2026 indexes returned no captures for the tested pattern—not a proof that all collections lack data. Saturn's public sample has ten cars labeled sold August 5, 2022 without VIN/geography. Rebrowser CARFAX marketplace sample and Crawl Feeds leads did not establish free, matched historical CVNA data. No paid access obtained.

Potential fallback: prospective, consistently observed VIN cohorts with dated inspections, price, presence and geographic clues, excluding partner inventory for an internal-output proxy. This cannot recover 2024–2026 causality and requires user approval before extensive/recurring collection. Nothing scheduled.

Files: [Seattle](research/volume/seattle-public-data-feasibility-2026-10-29.md), [listing pilot](research/volume/capacity/wayback-listing-pilot-2026-10-30.md), [coverage audit](research/volume/capacity/archive-coverage-audit-2026-10-30.md), [audit data](research/volume/capacity/archive-coverage-audit-summary-2026-10-30.json).

## 10. New sellside batch: findings that enter the analysis

User archives: `/Users/kwu/Downloads/Archive 3.zip` and `/Users/kwu/Downloads/drive-download-20261031T001614Z-1-001.zip`.

37 unique PDFs within this batch: 35 substantive CVNA/industry, one tangential Signet, one unrelated Pharvaris. Relevant narrative reviewed; critical tables visually checked, not every appendix cell audited. Dates span January 2025–September 2026; primary Q3 materials provide later outcomes. Many tours share one company-hosted event: repeated analyst accounts are not independent samples.

Source folder: `work/sellside-expanded-2026-10-31/`; `NN.pdf`, page-separated `NN.txt`, [manifest](work/sellside-expanded-2026-10-31/manifest.json), [37-report catalog](work/sellside-expanded-2026-10-31/report-catalog.json), [calculations](work/sellside-expanded-2026-10-31/calculations.json), [reproduction](work/sellside-expanded-2026-10-31/calculate.py).

Key IDs: 28 Citizens Elyria; 29 JPMorgan Elyria; 31 Morgan Stanley IRC ROI; 34 Morgan Stanley Haines; 37 JPMorgan Haines; 20 DA Davidson Haines; 10 Stephens prime ABS/forecasts; 11 Stephens credit tracker; 36 JPMorgan servicing rebuttal; 35 JPMorgan VIN rebuttal.

### Important quantitative results

1. Stephens prime ABS 2025-P1 → 2026-P3: APR 14.06% → 10.77%; weighted coupon 4.62% → 4.75%; simple difference 9.44% → 6.02%; average principal $24,146 → $29,620 (+22.7%). This is not a companywide gain or equity return. Terms/mix change.
2. July delinquency basket test: original five pools' June equal mean 1.684%; same pools July 1.846%; replacing older 2022-P3 with newer 2025-P2 yields 1.356%. Within-basket +16.2bp, composition -49.0bp, net -32.8bp. Headline improvement is composition-driven; not proof underwriting deteriorated because age/seasonality remain.
3. Stephens FY2026 January→August estimates: revenue $25.7504bn → ~$29.07bn (+12.9%); EBITDA $2.951bn → $2.9062bn (-1.5%); implied margin 11.46% → 10.00%. Bullish volume sentiment can coexist with deteriorating margin expectations.
4. Morgan Stanley IRC illustration: $3,300 retail GPU + $2,800 other GPU - $1,620 operating costs = $4,480 contribution. Other GPU is 62.5% of contribution. This is not standalone manufacturing ROI; capital/corporate costs/working capital are incompletely reconciled.
5. JPMorgan servicing example: ~$10m fee / $8,888m originations = 0.11%, versus $10m / $461m average outstanding = 2.17% from rounded inputs. Report prints 2.3%; retain discrepancy. Correcting stock/flow denominator challenges a low-fee claim but does not prove arm's-length pricing.
6. November 2025 delinquency history differs between later and earlier Stephens reports (2.14% versus 2.86%). Do not splice without population reconciliation.

[Full expanded synthesis](research/sellside/2026-10-31-expanded-synthesis.txt) contains caveats and source pages. [Earlier batch extraction](research/sellside/2026-10-28-extraction.md) remains background.

## 11. Loan-sale economics: parallel work and important corrections

### Mechanism and competing explanations

Carvana originates customer loans, funds/holds them temporarily, then sells through Ally forward flow, other whole-loan buyers or securitizations. Servicing collects/administers borrower payments after ownership changes. Securitization divides pool cash flows among securities with different priority/risk; retained interests still carry credit/prepayment exposure.

The question is whether high gains reflect sustainable origination/pricing and investor appetite, optimistic but independent buyer assumptions, related-party support, or accounting effects. A high borrower APR alone cannot answer it.

### Supported figures and limits

- FY2025 gains $1.193bn. Aggregate bridge: $13.315bn cash proceeds minus ~$12.4bn rounded principal plus $240m new retained fair value plus $38m residual reconciles gains. Residual reflects unresolved basis/timing/rounding/cost issues; not evidence of manipulation.
- 9M2026: gain $1.084bn; cash proceeds $14.722bn; new retained interests $266m; principal sold ~$13.9bn. Gain/principal ~7.80%, versus ~9.87% prior year. Lower ratio is observed but mix and repricing are not isolated.
- Q3 gains $381m vs $331m prior-year. Gains divided by all retail units decline ~$2,123 → $1,753. This denominator includes outside-financed/cash buyers.
- Retained beneficial interests $557m September 2026 vs $486m December 2025. Ending stock is not current-period noncash gain.
- Primary filing says no sales to DriveTime or affiliates in 9M2025/2026; issuer representation, not independent tracing of secondary ownership.
- Securitization trusts not consolidated under the stated assessment. Avoid broker statements implying all securitized loans remain consolidated or that retained exposure is risk-free.
- Ally corroborates comparable performance for similarly characterized loans; does not disclose channel purchase premium/return. Forward-flow commitment is capacity, not fixed pricing; contract has repricing mechanisms.
- Private fixed-pool buyers remain unnamed. Underwriters or shareholders must not be relabeled as loan purchasers.

### Buyer-return work completed

Actual public CRVNA 2026-P2 security pricing was recovered. Later work partially superseded the claim that residual pricing was wholly unavailable: filed FWP includes entire R-class value ~$49.272m at an 18.5% Case 2 modeled yield. XS economics, Case 2 details and full settlement remain incomplete.

A 67-cohort sensitivity with 3% net losses and 1.3% total ABS prepayment assumption values R at ~$45.477m at 18.5%, implying ~14.87% prospective modeled IRR at $49.272m. These are conditional modeling results, not realized returns or a buyer's actual forecast. Historical cohorts show 3% losses is not automatically conservative. Model/provenance/checks live in `work/loan-sale-economics/buyer-returns/`.

APR decomposition in `work/apr-decomposition/` supports substantial within-observable-category APR declines, not just FICO mix. However, Carvana changed its underwriting-score usage in December 2025, limiting FICO as a consistent risk control. No subsidy amount is inferred.

CarMax correction: most CAF loans are retained and earn spread over time. The selected ~$16.6m gain on ~$596m sales is not a companywide equivalent of CVNA gain-on-sale. Exclude the earlier raw 2.785% comparison and 4.613-point gap from valuation calibration. See [correction](work/loan-sale-economics/carmax-benchmark-correction-2026-10-30.json).

### Remaining discriminating evidence

One actual whole-loan settlement with UPB, carrying basis, price, accrued interest, side agreements, servicing terms and buyer funding; comparable bids/credit memo; matched acquired-cohort losses, collections, servicing and remaining marks. More borrower APRs, title locations or ratings alone will not establish buyer economics.

Use [research-state.txt](work/loan-sale-economics/research-state.txt) and its dated continuations, [evidence ledger](work/loan-sale-economics/evidence-ledger.json), [buyer-return report](work/loan-sale-economics/buyer-returns/report.html), and [servicing expanded audit](work/loan-sale-economics/servicing-expanded-audit-2026-10-30.json). Do not treat the opening date of the state file as the date of all appended work.

## 12. Latest actual results and scenario status

| Q3 metric | 2025 | 2026 |
|---|---:|---:|
| Retail units | 155,941 | 217,385 |
| Adjusted EBITDA | $637m | $800m |
| EBITDA / retail units | $4,085 | $3,680 |
| Retail GPU | $3,456 | $3,556 |
| Total GPU | $7,362 | $6,997 |

Units +39.4%, EBITDA +25.6%, EBITDA per retail unit -9.9%. Companywide allocations are not site contribution or marginal returns. Retail GPU increased even while other economics deteriorated.

Primary local sources: [Q3 letter](work/loan-sale-economics/sources/cvna-q3-2026-letter.pdf), [letter text](work/loan-sale-economics/sources/cvna-q3-2026-letter.txt), [filing text](work/loan-sale-economics/sources/cvna-q3-2026.txt).

Existing [conditional scenarios](research/volume/capacity/scenarios.md) are NOT forecasts. They start with normalized 800,000 annual production, not a measured annual run rate; hypothetical same-site improvements, buildout ramps and demand absorption drive outputs. Six further integrations in 2027 are an assumption, not guidance. Do not carry scenario outputs into the base model without recalibration.

Working capital matters: assumed $22,000 vehicle cost × 45 days × 100,000 incremental annual sales / 365 ≈ $271m vehicle inventory. At 60 days ≈ $362m. This is steady-state inventory, not required incremental cash borrowing, and excludes receivables/payables. Do not add assumed unsold accumulation twice.

Existing charts distinguish stocks and flows, but incomplete production disclosures prevent a complete measured production series. See [chart inputs](research/volume/capacity/charts/inventory-sales-data.json) and [overlay](research/volume/capacity/charts/inventory-sales-production-overlay.png). Do not interpolate missing production as observed data.

## 13. Current workstream A: quantify operating headroom, starting with paint

**Status: next investigation proposed; no new site-level headroom estimate has been established.** Existing supplier/process evidence above should be reused, not rediscovered.

### Questions

1. At which representative sites is paint actually binding, and on what dates/mix?
2. How many booths/lines are installed, usable and staffed? How many shifts/days run?
3. What share of cars requires full paint, spot repair, paintless dent repair or no paint?
4. How many productive hours and repeat visits does each category consume?
5. What constrains booth occupancy: labor, prep, cure/dry time, scheduling, equipment, permits, rework or feedstock?
6. Does moving the paint constraint expose mechanical, quality-control, title or transport constraints?
7. How much improvement comes from easier cars versus better processing of comparable cars?
8. What incremental hiring/training/equipment/working capital is required, and over what ramp period?
9. Can cheaper/older inventory return without reducing output or increasing queues/costs?

### Sources ranked by information value

- Dated site tours or operating disclosures with completions and shifts: best direct observations, often company-mediated.
- Equipment suppliers/installers and contractors: installed configuration and design rates; actual output must be verified separately.
- Air/VOC permits, inspections, paint-consumption/operating records: may provide equipment and activity limits; permitted maximum is not actual use.
- Training/manager progression and local employment records: executable labor availability, not automatic productive capacity.
- Collision-repair operators, suppliers and process specialists: task/cycle-time bounds; repair severity and insurance delays differ from CVNA.
- Job postings and employee accounts: weak corroboration, not headcount or throughput estimates.

### Initial sites and outputs

Start Elyria (new output/process detail), Haines City (repeat tours and staffing), and Tolleson (equipment benchmark). Include an integrated ADESA comparison if a named source reveals meaningful metrics. Avoid treating showcased mature IRCs as a representative network sample.

Produce a stage ledger: site/date, equipment, physical lines, staffed shifts, productive hours, affected-car share, cycle/work time, rework, completed output, queue, cost, source and confidence. Missing values remain missing.

Estimate separate conditional contributions from added staffed hours, better flow, less repair work and additional equipment. Do not sum improvements that unlock the same bottleneck twice. Report low/base/high assumptions only where anchored; no national utilization estimate from one site.

Acceptance condition: at least one matched dated site-stage observation with enough information to bound additional output, or a clearly explained inability to identify it. Anecdotes alone support mechanism, not a growth parameter.

## 14. Current workstream B: unbiased physical-headroom census

**Latest user proposal:** inspect all IRCs/related properties—or a defensible sample—to assess parking and undeveloped room using Google Maps/aerial imagery and other property evidence.

**Status: proposed, not executed.** No new satellite occupancy counts, aerial measurements, parcel audit or network land-headroom estimate has been completed in this discussion.

### Precise research target

Identify whether physical expansion room is widespread or concentrated, and what share of relevant sites can accommodate more storage/production without acquiring new property. This complements the operating study; it cannot independently determine annual production.

### Sampling and population

1. Reconcile the existing register before mapping: original IRC, active integrated ADESA, auction-only, planned construction, delivery/storage, closed/uncertain.
2. Separate property, establishment and operating-function identifiers. Do not count colocated ADESA/Carvana records as two land parcels or two independent factories.
3. Prefer a census of verified active retail-producing sites. If too time-consuming, predefine a stratified sample by original/integrated, vintage, region, metro overlap and site size. Record selection before viewing available room.
4. Include constrained/ordinary sites, not only easy-to-find or impressive facilities. Report missing imagery/records as missing, not zero capacity.

### Observation fields

- Site ID, actual address/town, type, coordinates with source, property boundary/parcel IDs.
- Ownership/lease where documented; shared tenants and auction uses.
- Imagery provider, acquisition date if known, access date, resolution and visibility limitations.
- Existing buildings, paved vehicle areas, circulation/loading, identifiable production areas.
- Usable marked parking where countable; measurement method and confidence.
- Date-specific occupied versus empty spaces, separately from total space.
- Undeveloped land inside confirmed boundary; constraints such as wetlands, drainage, topography, access, setbacks and utilities.
- Active construction, permits, proposed buildings/lines, and production-start uncertainty.
- Space plausibly allocated to retail recon versus auction/storage/logistics; unknown/shared categories retained.

### Interpretation and checks

- Imagery may be stale or seasonally unrepresentative. A 2022–2023 empty lot cannot establish 2026 spare room. Record unknown imagery date explicitly.
- One aerial observation cannot establish typical occupancy or inventory turns.
- Vacant ground may be stormwater infrastructure or unavailable land. Parcel/planning documents are needed before calling it buildable.
- Space and production equipment are complementary. Large parking slack with full paint booths does not imply easy output growth.
- Parking throughput bound requires dwell time and population alignment. Hypothetical 3,000 spaces / 10, 20 or 30 calendar days supports 300, 150 or 100 daily vehicles under strong simplifying assumptions—not CVNA estimates.
- Access aisles, safety buffers, peak demand and auction schedules reduce simplistic space utilization.
- No paid imagery or extensive manual stall counting before a small pilot establishes value. If building footprints/permits already answer the expansion question better, use that route.

### Deliverable

A map/register and distribution of sites with (a) documented existing paved slack, (b) potential expansion requiring construction, (c) apparent constraints, and (d) insufficient evidence. Keep measured area, estimated spaces, date-specific occupancy and buildable-land judgments in separate columns. Do not collapse them into one capacity score without justification.

Then connect to workstream A: how much operating equipment/staffing is required to use that physical option? The combined result should distinguish inexpensive activation, equipment expansion and major development—not extrapolate empty lots into sales forecasts.

## 15. Open questions, ranked and linked to model decisions

| Priority | Question | Evidence that would change the model |
|---|---|---|
| 1 | How much additional output can existing staffed/installed equipment produce economically? | Dated stage output, shifts, workload and productive-hour data |
| 1 | Is physical headroom broadly distributed? | Defined facility census with dated imagery and parcel/permit validation |
| 1 | How much apparent productivity is easier-car mix? | Age/mileage/repair-intensity cohorts and comparable-mix labor/cost |
| 1 | Will incremental output sell without eroding returns? | Ready-stock aging/markdowns, delivered price/payment, cost and cash returns |
| 2 | How long do new ADESA teams take to mature? | Actual commissioning, staffing/manager progression and output/cost at matched dates |
| 2 | Do first-local sites outperform overlapping additions? | Buyer-local series with consistent observation and all nearby sites accounted for |
| 2 | How much financing compression remains? | Channel pricing, terms, mix, buyer economics and gain/retained breakdown |
| 3 | Can listing proxies support historical local inference? | Verified processing-origin calibration AND adequate archive coverage |

Potential alternatives to a fragile local causal study: direct operating accounting at a few well-documented sites; a broader cross-sectional physical census; scenario bounds using observed stage constraints; prospective cohorts with consistent observation. Compare precision, access and cost rather than assuming more scraped rows improve identification.

## 16. Corrections and supersession ledger

- Older staffing notes say the two Morgan Stanley reports were missing. **Now obtained and read:** expanded IDs 34 (Nov 18, 2025 Haines) and 31 (June 10, 2026 IRC ROI). Do not ask the user to retrieve them again.
- Earlier notes say Wayback coverage had not been tested. **Superseded by completed October 30 audit**, which did not validate the historical panel.
- Earlier notes say no usable site-output observation. **Partly superseded by Elyria June 2026 reported weekly output**. Still no paired site staffing/output time series.
- Haines 40% = parking, not factory utilization.
- 12,800/week Haines printed number = excluded suspected error, not accepted or silently repaired.
- Haines 2025 staffing is near 2021, below 2022; do not call 2022 an efficient normal baseline or pre-COVID.
- Early buyer work says residual pricing unavailable. **Partly superseded by P2 FWP discovery**; full settlement/XS economics still incomplete.
- Selected CarMax loan-sale ratio is not companywide finance profitability.
- Reported 50% network utilization remains management testimony with unresolved denominator.
- Existing scenario production and future project counts remain assumptions, not observed output or guidance.

## 17. Practical file map and reproduction

### Primary/transcripts

- `work/cvna2025.txt`: existing annual-report extraction.
- `work/earnings-calls/manifest.json`: retrieval provenance.
- Calls available include CVNA Q4 2024; Q1–Q4 2025; Q1–Q2 2026; KMX Q4 FY2026 and Q1–Q2 FY2027; AN/LAD Q1–Q2 2026; ALLY Q3 2026. Check the directory for additions. Do not claim a local CVNA Q3 call is present merely because the letter/filing are.
- `work/loan-sale-economics/sources/`: primary filings, contracts, ABS material and Q3 2026 letter.

### Analysis/reproduction

- `research/volume/capacity/reproduce.py`, `scenario-inputs.json`, `scenario-results.json`: conditional output/capital sensitivities.
- `research/volume/capacity/build-staffing-panel.py`, `staffing-panel-data.json`: OSHA panel and scope checks; raw downloads may be outside a fresh checkout.
- `research/volume/capacity/charts/`: inventory/sales/production overlay and employee chart. Definitions in associated data/code.
- `work/sellside-expanded-2026-10-31/calculate.py`: selected financing series, same-pool delinquency bridge, forecasts and ROI arithmetic. Outputs `calculations.json` and `evidence-chart.png`.
- `work/loan-sale-economics/calculate.py`, `calculations.json`, `evidence-ledger.json`: financing arithmetic/provenance.
- `work/loan-sale-economics/buyer-returns/model.py`, `checks.py`, `provenance.json`, `results.json`: conditional buyer model and checks. Read assumptions before running or extending.
- `CVNA-research-terminal-prompt.txt`: earlier extensive terminal research request; use as background, not current evidence status.

Many `work/` and research files are local/untracked. A fresh remote checkout may not contain them. Confirm file availability and do not confuse a local save with Git publication. Keep proprietary source PDFs local unless separately authorized to publish them.

## 18. Suggested next session

1. Read this handoff and the October 31 sellside synthesis; inspect only source passages needed for the next question.
2. Reconcile the active retail-facility sampling frame and the 56/57 directory discrepancy as far as free sources permit.
3. Pilot aerial/parcel classification on a few predefined contrasting sites to assess imagery date, land-boundary and auction-use ambiguity. Then decide whether a census is feasible without expensive collection.
4. In parallel conceptually—but without assuming agent delegation—develop the Elyria/Haines/Tolleson stage ledger using existing tours and the supplier benchmark; search specific missing equipment/operating records.
5. Report what is measured, what is bounded and what remains unknown. Update the model only with clearly labeled inputs. If output cannot be identified, do not manufacture an elasticity.
6. Integrate operating scenarios with financing contribution, inventory funding and demand absorption. A supply-only capacity forecast is not the investment conclusion.

**Success means a credible range for economically executable headroom, with identifiable constraints and falsification tests. It does not require proving that every facility can double, or forcing all recent volume growth into one explanation.**


## 19. October 31 municipal/headroom pilot update

See [headroom pilot](research/volume/capacity/headroom-pilot-2026-10-31.md). Dayton plans and watershed approval support roughly 68k sq ft of proposed repair/detail construction replacing ~350 parking spaces; they do not establish commissioning or throughput. Elyria June/August 2026 air-permit records were identified, but document bodies remain inaccessible. Belton and Boston remain leads, not model inputs. No current facility-utilization percentages were established; no national aerial census was completed. Targeted permit/equipment follow-up is preferable to more parking or job-posting proxies. Reproducible paint-workload sensitivity is illustrative only.


## 20. Equipment follow-up

[Follow-up note](research/volume/capacity/equipment-followup-2026-10-31.md) adds Tolleson-specific paint bottleneck testimony (March 2026 conference), Greenfield contractor equipment baseline (2019: eight paint booths), and Trenton opening-era equipment (2022: 12 booths, 91 lifts). Greenfield reported hours grew faster than headcount in 2025, with reporting-scope caveats. These strengthen mechanism evidence but do not establish current utilization or justify changing the production forecast. Elyria permit bodies remain unavailable.


## 21. Paint bottleneck model completed

[Paint study](research/volume/capacity/paint-headroom/README.md) provides the evidence register, process map, ranked mechanisms, executable model, requirements, costs and monitoring gaps. Current site estimates remain null. Tolleson historical booths are organized into serial side-load lines; do not pool them as independent parallel booths. Visual review resolved Oracle 2024 slide 24: cycle time down 60%, first-time QC pass up 13%, but baseline/scope/units remain insufficient for calibration. New 3M/GFS/PPG technical guidance helps distinguish cycles, refinish work content and curing; none is imported as a CVNA rate. At fixed productive hours, +20% output needs 16.7% less binding workload; eliminating a small rework burden cannot create arbitrarily large gains. Constructed plant scenarios demonstrate bottleneck migration and mix sensitivity, not a company growth range. `model.py` reproduces outputs and eight arithmetic checks; no empirical validation claimed. Elyria portal controls still did not yield permit bodies.

## 22. Matched operating-observation follow-up

The [follow-up search](research/volume/capacity/paint-headroom/matched-observation-search-2026-10-31.md) found two partial historical accounts: an unidentified IRC's staffing-sensitive inspection cadence and an interview estimate of cosmetic labor. Neither pairs paint resources, workload and accepted output at the same site and period. Do not transfer inspection rates to paint, equate more staffing with labor productivity, or combine historical general labor estimates with current Elyria production. Recurve's repeated Haines visits provide qualitative changes but its numerical output series is network-level and was already known. No model parameter or forecast changes; stop generic searches until a concrete matched operating lead appears.
