# ADESA local market research plan

Drafted 2026-10-29 under the [profitable volume framework](README.md). This is an execution plan, not a completed study or forecast.

## Hypothesis and decision

Test whether adding Carvana retail reconditioning to an ADESA location improves nearby selection and delivery, increases Carvana's local sales share, and produces attractive incremental cash returns.

The sequence to verify is **production starts → suitable local inventory and delivery improve → local sales share increases → contribution covers operating costs and capital invested**. Identify which links are observed and which remain assumptions.

Alternatives include pre-existing local demand growth, simultaneous advertising or financing changes, used-market recovery, competitor weakness, and inventory redistribution from other Carvana sites. More local sales may reflect cannibalization rather than incremental company sales.

## Phase 1 Establish event dates and data access

Run a bounded discovery pass across company disclosures, local operating records, vehicle registration sources, historical listings, industry demand data and competitor disclosures. Inspect representative samples before attempting full collection.

Build an event register with location/address, announcement date, verified production start or date interval, integration type, later expansions, evidence of output, source URL/passage and confidence. Keep original Carvana IRCs, converted ADESA sites, combined auction/retail sites, storage/delivery hubs and full buildouts distinct. Do not treat all sites as equal or an announcement as a production start.

Candidate early events include the May 2024 transition disclosures and Kansas City in 2024. Kansas City offers an explicit link between integration and subsequent same-day delivery. Select the pilot based on verifiable dates and data availability, not on how impressive the subsequent sales look. Prefer two or three events if access permits, with enough pre-event history to inspect trends.

| Source family | What to check | Limitation or alternative |
|---|---|---|
| Company releases, letters, calls | Site dates, scope, local pools, delivery, output | Management attribution is not independent validation |
| Local permits, certificates, planning records, hiring | Construction and operating milestones | Permit or job posting does not establish production volume |
| State registration/title records and registration providers | Monthly retailer-attributed retail registrations by buyer geography, used/new flag | Retailer identity, coverage, licensing and cost may block access; assess metadata first |
| Historical vehicle listing providers or existing archives | VIN, status, first/last seen, price, delivery quote, availability by ZIP | Removal is not a sale; current browsing cannot reconstruct history |
| Industry and local market records | Comparable local used retail transactions, price/mix, credit conditions | Match scope; broad national data cannot identify local effects |
| Competitor filings and local changes | CarMax and other dealer pricing, openings, closures and performance | Corporate totals are contextual, not local controls |

Registration records should be aggregated; no buyer personal information is needed. Audit whether retailer attribution and buyer location actually exist before relying on the source. Vehicle registration timing can lag deliveries and change across states.

**Feasibility gate:** Can we observe a credible treatment date, comparable local sales denominators, pre/post history and suitable controls? If not, narrow the claim to selection/delivery mechanisms or descriptive regional evidence. Seek user approval before paid data, bulk scraping, large OCR or extensive fitting. Explain expected information gain, uncertain cost and alternatives first.

## Phase 2 Define the pilot and outcomes

Use buyer residence geography for market demand and sales outcomes. Operational benefits may cross state or metro boundaries. Define treatment exposure from documented service changes or distance/travel time to sites, not simply whether a county contains a site. Pre-specify geographic definitions before inspecting post-event results; report sensitivity to reasonable alternatives.

Aim for at least twelve months before and twelve months after an event where available, to capture seasonality and ramp. Shorter windows remain explicitly preliminary. Avoid averaging away a gradual production ramp.

Primary outcome: Carvana used retail registrations divided by comparable local used retail registrations. Secondary outcomes: absolute sales, suitable available inventory, delivery time/fees, matched-vehicle pricing, listing age and markdowns.

For inventory, distinguish owned versus partner where identifiable, available versus reserved, preparation status, local availability versus nationwide listings, and actual storage location versus estimated delivery availability. Segment by price band, body type, age and mileage. A large increase in expensive cars may not improve selection for a budget buyer.

If observing listings, use stable ZIPs and query definitions. Deduplicate VINs; retain relistings, withdrawals and censoring. Audit a sample of disappeared listings before interpreting them as sales. Do not equate inferred listing duration with acquisition-to-sale holding time.

## Phase 3 Compare mechanisms and outcomes

1. Plot pre/post levels and trends for treated markets, local industry transactions and candidate controls. Record concurrent pricing, financing, advertising and competitor changes.
2. Choose controls with similar pre-event trends, vehicle/customer mix and local conditions, without recent comparable integrations or major spillovers. An untreated Carvana market still experiences national Carvana changes.
3. Where sample quality permits, compare changes in treated versus control markets and estimate effects by months around production start. Use not-yet-treated or never-treated comparisons appropriately for staggered rollout; avoid a mechanical pooled estimator that treats already-affected markets as clean controls.
4. Inspect anticipation, delayed ramp, placebo dates, pre-trends and alternate boundaries. Report effect ranges and uncertainty; a small event sample does not justify precise significance claims.
5. Check the chain: capacity/availability changes should precede delivery and sales effects. A sales increase predating production weakens the capacity explanation.
6. Examine adjacent markets and national totals for displacement. Distinguish a total integration effect, including induced marketing, from a direct physical-capacity effect. Do not control away inventory or delivery when estimating the total effect; they are proposed mechanisms.

A predictive model is a separate exercise. Lag available inputs, preserve publication dates and hold out later observations. A strong prediction score does not resolve site-selection bias or identify a causal driver.

## Phase 4 Estimate incremental economics

Direct site profitability may not be disclosed. Use observed components where available and transparent ranges elsewhere; national average GPU is not a verified local contribution margin.

Incremental operating contribution = genuinely incremental sales × incremental contribution per sale + documented transport/operating savings on existing sales − incremental advertising and site operating costs − incremental inventory losses and financing costs.

Define the per-sale contribution boundary first so logistics, labor, financing and markdowns are not counted twice. Keep existing ADESA auction profits separate from incremental retail benefits. Include any displaced wholesale activity or shared-site opportunity cost when material.

Incremental cash flow also reflects inventory working-capital investment, ramp and ongoing capex, and cash taxes. Evaluate site-expansion returns on incremental investment; evaluate the broader acquisition thesis separately including the original purchase price and subsequent investment. Existing property is not economically costless.

Report conservative, central and favorable cases without invented local precision. Stress sales lift, ramp speed, markdowns, utilization, marketing and normalized finance contribution together. Local sales growth with weakening contribution or rising inventory age does not establish profitable growth.

## Deliverables and stopping rules

- Event register and source ledger, including unverified start dates and definition conflicts.
- Data feasibility memo naming accessible fields, coverage, timing, cost constraints and the strongest achievable claim.
- Pilot dataset and reproducible transformations, followed by before/after comparisons only if the feasibility gate passes.
- Mechanism and economics assessment: supporting evidence, disconfirming evidence, uncertainty and permissible forecast inputs.

Stop expanding collection if historical sales cannot be attributed locally, control markets are contaminated, or proxy validation fails. Complete the descriptive evidence and specify the missing observation. Do not assign a causal sales elasticity to ADESA from aggregate inventory/sales correlations.

## Starting sources and continuity

- [May 2024 transition announcement](https://investors.carvana.com/tools/viewpdf.aspx?page=%7BB51188FE-0C1A-4894-9BBB-2C1D554E2210%7D).
- [Kansas City megasite announcement, August 19, 2024](https://www.carvana.com/press/press-releases/carvana-develops-first-auction-irc-megasite-in-kansas-city).
- [Kansas City same-day delivery announcement, September 30, 2024](https://investors.carvana.com/news-releases/2024/09-30-2024-100009412).
- [2025 annual report](https://investors.carvana.com/~/media/Files/C/Carvana-IR/documents/cvna-2025-annual-report.pdf): 56 acquired locations and 16 integrated sites at year-end.
- [Q3 2026 shareholder letter](https://investors.carvana.com/~/media/Files/C/Carvana-IR/documents/cvna-shareholder-letter-q3-2026.pdf): 21 integrated sites and three full buildouts under construction expected to start production in 2027.

Retrieve full source passages during event-register construction; announcements are leads, not verified operating dates. Prior sell-side material labels a regional comparison as production growth while the local Q2 2026 call transcript calls it inventory growth (57% versus 17% across region groups). Reconcile with the original shareholder-letter chart before using it. Existing transcripts and raw research under `work/` remain untracked; preserve them and do not sweep them into a documentation commit.
