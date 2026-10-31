# Sources, definitions and discovery record

As of 2026-10-29. Period endpoint Q3 2026; October facility information is explicitly subsequent evidence. Company statements establish what management disclosed; they are not independent proof of causal sales effects or profitable unmet demand.

## S1 — Annual filing and local baseline

[May 2022 acquisition disclosure](https://investors.carvana.com/news-releases/2022/05-10-2022-113013333): $2.2bn cash acquisition, 56 properties, roughly 6.5m square feet and over 4,000 acres. The [2024 annual report](https://investors.carvana.com/~/media/Files/C/Carvana-IR/documents/annual-report-2024.pdf) specifies May 9 closing. This includes an operating wholesale business, not exclusively retail-production real estate.

[2025 annual report](https://investors.carvana.com/~/media/Files/C/Carvana-IR/documents/cvna-2025-annual-report.pdf), local `work/cvna2025.txt`: Item 2 p.32, financial statements and operating metrics. Retail units 416,348 in 2024 and 596,641 in 2025; purchases of property/equipment $91m/$147m. Property table pools IRCs, hubs, vending machines, dealerships and auction locations: other-facility owned/leased interior area 5.3m/5.9m square feet; owned/leased land 4,176/3,132 acres. Neither a recon-only footprint nor individual property title record.

## S2 — Quarterly letters

- [Q3 2024](https://investors.carvana.com/~/media/Files/C/Carvana-IR/documents/cvna-shareholder-letter-q3-2024.pdf): quarter-end versus publication-date integration distinction; approximately 300 fewer shipping miles to customers in integrated-site metros. Existing [local proximity research](../adesa-local-proximity-test.md) preserves passage context.
- [Q4 2025](https://investors.carvana.com/~/media/Files/C/Carvana-IR/documents/cvna-shareholder-letter-q4-2025.pdf), pp.5,9: cost dispersion, production investment routes. Top-quartile comparison is not adjusted for vehicle mix or site age; do not treat its approximately $220/unit opportunity as guaranteed savings.
- [Q2 2026](https://investors.carvana.com/~/media/Files/C/Carvana-IR/documents/cvna-shareholder-letter-q2-2026.pdf), printed p.4 and capacity chart: quarterly integration counts and 36% companywide production growth. The call calls the regional series inventory growth. Written label retained, discrepancy unresolved. See [prior verification](../adesa-regional-evidence-2026-10-29.md).
- [Q3 2026](https://investors.carvana.com/~/media/Files/C/Carvana-IR/documents/cvna-shareholder-letter-q3-2026.pdf), printed p.5 and financial tables. Local `work/loan-sale-economics/sources/cvna-q3-2026-letter.txt` preserves page markers; `cvna-q3-2026.txt` contains filing tables. 21 integrations, three full buildouts under construction for 2027; approximately 1.5m annual capacity described as fully built out within current footprint, real estate for 3m. These are not current staffed output. Financial numbers are consolidated company figures.

## S3 — Existing earnings calls

Full local transcripts in `work/earnings-calls/`; original CapIQ URLs and retrieval details in that folder's `manifest.json`. Used existing access only, no new purchase. **Use the transcript before its Disclaimer; ignore provider AI summaries.**

| File | Locator | Evidence used |
|---|---|---|
| CVNA-Q4-2024.txt | lines 75–79, 228–234 | Pre-integration IRC network capacity above 1m; hiring/training/execution required |
| CVNA-Q1-2025.txt | lines 242–250 | Weekly output-rate increase around 80 units/week over preceding year; average about 23 producing locations |
| CVNA-Q2-2025.txt | prepared results | 143,280 retail units; no internally produced unit count inferred |
| CVNA-Q3-2025.txt | lines 93 onward | Marketplace accounting transition complicates average revenue per unit |
| CVNA-Q4-2025.txt | lines 91, 132–140, 218–220, 305–316 | Facilities investment for 1.5m stated; newer managers and single-line sites; production grew more than 40% |
| CVNA-Q1-2026.txt | lines 86–92, 127–135, 171–178, 390–414 | Staffing allocation, paint flow, productivity tools; four expansion routes; HPU recovery and training |
| CVNA-Q2-2026.txt | lines 128–130, 292–308, 328–388 | Cost-first sequence, execution limit, site selection, newer-car mix, financing interaction and intended broadening |

Locators are line numbers in the inspected local snapshots, not universal transcript pagination. Files were present except **Q3 2026 Carvana call**, which was missing locally. Public transcript filled that gap.

## S4 — Q3 call obtained publicly

[Q3 2026 transcript, StockAnalysis](https://stockanalysis.com/stocks/cvna/transcripts/718716-q3-2026/) (October 28 call; read October 29). Jenkins answer to Marvin Fong: production exceeded 200,000, slightly exceeded retail sales; exact production unspecified. Garcia answer to Jeff Lick: supply-chain execution cited as constraint; later-model, higher-price and prime mix remained. Jenkins prepared remarks identify hiring/training across recon, logistics and customer care. These are management testimony, not independent validation. No full transcript copied into the repository.

## S5 — Expansion economics

[August 2026 JPMorgan conference presentation](https://investors.carvana.com/~/media/Files/C/Carvana-IR/reports-and-presentations/jp-morgan-auto-conf-aug-2026.pdf), slide 6: staffing existing facilities requires no incremental facility capex; integrations $2–3m/~13k incremental annual capacity; full buildouts $30–35m/~40k. 19 integrations and 37 total recon sites at Q2 imply 18 non-ADESA sites. This is an aggregate arithmetic reconciliation, not validation of every named candidate. Capex guidance excludes the cost of the original property acquisition and does not establish year-one realized output.

## S6 — Facility names and locations

- [ADESA directory map](https://www.adesa.com/map/#), observed October 29: bounded read of 57 location cards, not vehicle-listing scraping. Raw snapshots saved in `adesa-site-cards.json` and `adesa-directory-snapshot.txt`. Displayed address text extracted; stale map-camera coordinates deliberately ignored.
- [ADESA post-sale inspection policy](https://www.adesa.com/wp-content/uploads/2019/02/AD-0624-PSI-Updates-TC-Policy-5.pdf): names 16 Carvana locations. It supports identity, not a certified IRC census. Twelve primary location pages and additional regulatory/employer sources supply addresses. `original-irc-inputs.json` contains source URLs and quality distinctions.
- [Prior 21-site candidate reconstruction](../adesa-21-site-candidate-roster.json): announcement links retained without converting dates to starts. Buffalo's month explicitly denotes operations; Portland conversion timing is bounded. Original centers are mapped separately.
- [May 2024 acquisition anniversary](https://press.carvana.com/carvana-marks-second-anniversary-of-adesa-acquisition-with-new-integration-and-performance-milestones/): last-mile operations at 30 ADESA properties and middle-mile at nine. An auction site without retail integration may already affect delivery.

The map's 57 entries versus the acquired portfolio's 56 is **unresolved**. Queen City is an extra named map entry relative to the usual directory navigation, but there is insufficient evidence to attribute the entire discrepancy to its closure, duplication or ownership. The register is a research inventory, not an asserted current company facility count. Delanco street address, most opening dates, site ownership/leases and individual output remain unverified.

## S7 — Independent project check

[Jacksonville January 27 plans reporting](https://www.jaxdailyrecord.com/news/2026/jan/27/carvana-files-civil-engineering-plans-for-northwest-jacksonville-megasite/), [September 8 permit report](https://www.jaxdailyrecord.com/news/2026/sep/08/carvana-lands-permit-for-12-million-northwest-jacksonville-megasite/), and [October 21 approvals](https://www.jaxdailyrecord.com/news/2026/oct/21/carvanas-dinsmore-megasite-lands-more-approvals/), Jax Daily Record. Regulatory-record reporting is independent of earnings commentary, but underlying permit files were not separately downloaded. January plans: 77,000 sf plus 6.9 acres staging. September: $12m site-work approval. October: $10m, 74,400 sf building permit; city-reported total site improvement cost $32m. Do not sum $12m+$10m+$32m, or call the permit cost audited actual spend. No verified production-start date or confirmed match to the three company buildouts.

[Arkansas EDC opening, January 5 2021](https://www.arkansasedc.com/news-events/newsroom/detail/2021/01/05/carvana-completes-new-inspection-distribution-center-in-west-memphis): $40m original IRC project, illustrates a pre-ADESA construction cycle. Planned jobs are not present headcount. OSHA address records corroborate location only; no safety interpretation enters this research.

[University Park contractor record](https://witechcompany.com/project/carvana-inspection-facility-project-description/): Witech completed its site-development scope in November 2021 for ARCO/Murray; describes a 145-acre job. This corroborates pre-acquisition construction, not production commencement. An indexed 2025 municipal newsletter described a 120-acre site and 200,000-square-foot building, but full PDF retrieval failed due to size; those uninspected dimensions are not used in calculations or the register.

[Oklahoma City Chamber, March 30 2022](https://www.greateroklahomacity.com/news/2022/03/30/automotive/carvana-celebrates-opening-of-brand-new-oklahoma-city-inspection-center/): >$40m investment and >150 staff hired against >350 eventual jobs. The article reports an opening celebration while saying official opening follows in weeks; exact production start remains unknown. Its ~10,000 stored-vehicle figure is stock capacity, not annual production.

## Method and stopping rule applied

Reviewed the named local framework, candidate roster, regional and Seattle feasibility notes first. Searched company documents, announcements, official facility directories, municipal/development evidence and local project reporting. Followed concrete Jacksonville approvals and original-IRC address leads; stopped before a national permit crawl, population overlay or speculative vehicle-sales proxy. Existing CapIQ transcripts are available; no validated free site-level output, buyer-local sales, mix-adjusted HPU or ready-inventory history emerged.

No repeat Washington/Missouri searches, traffic exercise, paid data, outreach, bulk VIN collection or fitted causal model. Scenario parameters are explicitly assumed. Arithmetic consistency is a check, not independent validation; Jacksonville corroborates construction, not demand or production economics.
