# Historical listing coverage audit — 2026-10-30

## Decision

**Not yet suitable for a historical metro inventory-flow/staffing correlation panel.** Wayback has substantial listing metadata, but frequent repeated observation and recoverable historical geography have not been established. This is not a claim that the archive has no data or that approximate geography is unacceptable. Approximate sourcing regions remain permitted; this audit concerns observation coverage and content recovery.

## Metadata retrieved and transformations

Read Internet Archive's [CDX documentation](https://github.com/internetarchive/wayback/blob/master/wayback-cdx-server/README.md?plain=1), then queried metadata through the browser. Shell network access failed DNS resolution; browser access worked intermittently.

Successful query:

`https://web.archive.org/cdx/search/cdx?url=carvana.com/vehicle/*&from=2024&to=2026&output=json&fl=timestamp,original,statuscode,mimetype&filter=statuscode:200&limit=50000`

Returned **exactly 50,000 rows**, reaching the explicit query cap; therefore this is a **URL-ordered, nonrandom, truncated sample**, not an exhaustive archive census. Initial 5,000-row query is contained in this sample and is not a separate observation. Do not present sample annual/monthly counts as total archive coverage. An attempted 100,000-row query returned the archive's Temporarily Offline page. A separate numeric-path-filtered query returned a 504; a 2026-only query also returned Temporarily Offline. These are access failures, not zero-result findings.

Parse the JSON body; remove header; retain originals matching `^https?://(www\.)?carvana\.com/vehicle/\d+(\?.*)?$`. Group by numeric vehicle ID (not VIN); remove query-string variants for ID-level grouping. For intervals, deduplicate capture days within each ID, sort, then subtract adjacent calendar dates. This does not merge vehicles relisted under different IDs or prove captured availability.

| Sample metric | Result |
|---|---:|
| Returned metadata rows, all matched paths | 50,000 |
| Clean numeric-listing capture rows | 41,044 |
| Distinct numeric vehicle IDs | 32,130 |
| IDs with exactly one capture row | 25,354 (78.9%) |
| IDs with multiple capture rows | 6,776 |
| IDs captured on multiple distinct days | 6,058 |
| Adjacent distinct-day gaps | 7,205 |
| Median adjacent gap | 46 days |
| Gaps over 30 days | 4,497 (62.4%) |
| Rows containing “inspection” in URL | 46 |

Numeric IDs in the returned sample extend through 4,841,935. The final returned row is an `/vehicle/lt/` URL, rather than the last numeric ID. This suggests substantial standard-path coverage, but does not independently verify query completeness or all URL conventions. The 46 inspection-related rows are not an estimate of all inspection records: some reports may be embedded or use different paths.

Monthly counts within this returned sample are saved in `archive-coverage-audit-summary-2026-10-30.json`. Illustrative contrasts: April 2024 2,315 captures vs August 2024 18; April 2025 4,107 vs May 326; March 2026 1,466 vs April 313. These measure capture activity in a capped sample, **not Carvana sales or inventory**. URL-order selection, crawler priorities and changing URL formats prevent treating these ratios as unbiased coverage comparisons.

The long intervals and one-off captures undermine arrival/removal measurement. Capture timestamps are crawler visits, not vehicle arrival dates. A missing capture is not a sale. Even repeated rendering of an old listing does not establish continuous sale availability.

## Content replay tests in this audit

| Capture | Observed result | Required research fields recovered? |
|---|---|---|
| [BMW 1461042, Jan 24 2025](https://web.archive.org/web/20250124091627/https://www.carvana.com/vehicle/1461042) | Model and 81,944 miles; partial page; inspection navigation/scroll did not reveal checklist | No VIN-linked inspection date plus sourcing geography recovered |
| [Same BMW, Apr 7 2025](https://web.archive.org/web/20250407014929/https://www.carvana.com/vehicle/1461042) | Model/mileage, $24,990 price, destination/shipping details; owner-review section contained Jeep Cherokee reviews on BMW page | No usable historical inspection/history bundle; mismatched component warns against treating assembled replay as uniformly trustworthy |
| [Inspection path for 2978621, Mar 18 2024](https://web.archive.org/web/20240318055614/https://www.carvana.com/vehicle/inspection/2978621) | Page title “Inspection Report”; body blank in browser observation | No |
| [Tesla 4841935, Oct 20 2026](https://web.archive.org/web/20261020201323/https://www.carvana.com/vehicle/4841935) | Initial model, 48,245 miles and photos; after inspection navigation/scroll, no recoverable report fields and later observation blank | No |

Four capture replays across three vehicle IDs; purposive tests, not a random recovery-rate sample. Prior 2021/2022 examples are recorded separately in `wayback-listing-pilot-2026-10-30.md`. The January-to-April BMW captures do not independently establish that the vehicle remained unsold throughout. Cause of incomplete/mismatched rendering was not diagnosed; missing dependencies, capture timing differences or replay behavior are possible, not proven.

## Independent archives and public datasets

- **Common Crawl:** searched `www.carvana.com/vehicle/*` in October 2024, October 2025 and October 2026 indexes. All three ultimately returned “No Captures found”; October 2026 initially returned 504, then explicit no-captures on one reload. This is restricted to those collections/pattern, not all Common Crawl history. Queries: `https://index.commoncrawl.org/CC-MAIN-2024-42-index?url=www.carvana.com%2Fvehicle%2F*&output=json`, same path using `CC-MAIN-2025-43-index` and `CC-MAIN-2026-43-index`. [Index documentation/UI](https://index.commoncrawl.org/).
- **[Saturn Data Cloud public GitHub sample](https://github.com/saturndatacloud/datasets/blob/master/Automative/Carvana/used%20cars/carvana_used_cars.csv):** ten cars, all labeled sold August 5, 2022. No VIN/geography columns; not a 2024–2026 longitudinal series. “Sold” is publisher terminology, not independently verified transactions.
- **[Rebrowser CARFAX marketplace dataset](https://github.com/rebrowser/carfax-dataset/blob/main/README.md):** publisher reports full coverage starting November 16, 2025, but free public sample retains latest 30 days with up to 1,000 rows/day. VIN/listing ID marked restricted in schema. This is marketplace inventory, not the detailed history reports used in our five-car pilot. No established Carvana-specific historical panel. No paid access or outreach undertaken.
- **[Crawl Feeds Carvana sample](https://crawlfeeds.com/datasets/carvana):** indexed sample dated May 27, 2023 includes a Norfolk MA address and partner-inventory flag. Full page fetch timed out. Location-field meaning, repeated coverage and free historical access not established; do not treat address as IRC evidence. Lead only, no purchase.
- Searches of public GitHub/Hugging Face datasets and historical-inventory terms found scraper software and paid/custom collection services but no verified free longitudinal replacement. Search snippets advertising large datasets are not coverage validation.

## Implications / next decision

1. **No regression or metro-growth chart from current archive counts.** We cannot distinguish a local business increase from changing capture probability, and did not recover the dated geography needed for metro grouping in the replay sample.
2. **Archive remains useful for individual historical observations**, provided page fields and their dates can be verified. It is not disproven as a possible data source; a complete index/archived-content extraction might improve recovery but requires additional technical collection and still would not fix selective crawling by itself.
3. **More defensible feasible fallback:** a prospective, consistently observed, narrowly defined vehicle cohort, tracking new VINs, inspection dates, recent service geography, prices and continued presence. This can test subsequent changes, not reconstruct 2024–2026. Exclude partner inventory for an internally processed-output proxy and retain relistings/returns as unresolved events. No recurring collection has been scheduled.
4. **Continue the historical operating-capacity analysis independently** using metro-aggregated IRC staffing/hours and direct production observations where available. DFW includes Blue Mound and Hutchins; do not attribute metro changes to a single facility or mix auction staffing with retail processing without qualification.

Overall: archive feasibility is **not validated**, rather than confidently impossible. The strongest new quantitative evidence is sparse repeat capture in a large metadata sample. This audit does not test whether staffing caused volume growth and should not enter that model as an estimated effect.
