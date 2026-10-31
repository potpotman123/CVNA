# ADESA pilot feasibility findings

As of 2026-10-29. First bounded pass under the [research plan](adesa-research-plan.md). No before/after sales estimate or site-return estimate is yet supported.

## Free-data discovery: Missouri dealer sales

**Validation update:** This sample fails the retail-demand identification test. The reporting rules include wholesale and retail, license numbers may survive dealership buy-outs, and current names/addresses cannot establish historical identity. Keep the counts as administrative observations, not local retail demand, production, or a causal ADESA estimate. See validation below.

User constraint: no paid data. The vendor inquiry below is not authorized for sending and is superseded by free-source research.

Following a local-news lead to Missouri DOR's [public report index](https://dor.mo.gov/public-reports/) produced a useful free [motor vehicle dealer report](https://dor.mo.gov/public-reports/dealers_mv_report.txt), dated October 6, 2026. The separate franchised-dealer report does not contain Carvana. The full motor-vehicle report was retrieved as browser-rendered text after web extraction and a download attempt failed. Raw local evidence: `work/adesa-pilot/2026-10-29-missouri-dealer-report.txt`; selected reproducible counts and hash: [JSON extract](missouri-dealer-sales-sample.json).

| Current dealer identity | License | 2023 used units | 2024 | 2025 | 2025 / 2024 |
|---|---|---:|---:|---:|---:|
| ADESA Kansas City / Carvana, Belton | D2160 | 198 | 225 | 742 | +229.8% |
| Carvana, Kansas City | D4620 | 6,070 | 3,397 | 2,664 | -21.6% |
| Combined two licenses (derived) | — | 6,268 | 3,622 | 3,406 | -6.0% |
| CarMax, Independence | D6038 | 3,540 | 3,822 | 3,480 | -8.9% |

These are observed counts labeled USED under UNITS SOLD IN each year, not verified local consumer deliveries or reconditioning output. The Belton increase of 517 units coexists with a 733-unit decline at the separate Kansas City license. Thus selecting only the expanding Belton license would produce a misleading impression of the combined licensed activity. This does not establish transfers between the licenses: changes in routing, reporting, customer geography, wholesale mix, or genuine demand remain competing explanations.

The same report lists Carvana at Jackson (D9582), Hazelwood (D9584), and Strafford (D9015). Across the five Carvana-named licenses, reported used counts sum to 9,553 in 2024 and 11,688 in 2025 (+22.4%). This is a current-license sample, not a verified complete Missouri retail-sales series. Missing/closed/renamed licenses and historic ownership matter. Counts predating the current Carvana business at some licenses demonstrate why current dealership names cannot simply be projected backward. The 2026 entries are partial-year and must not be compared with full-year 2025 as YoY growth; reporting cutoff is unknown.

**What can enter the decision:** Free administrative data exist and can test whether the apparent site expansion survives aggregation across related licenses. The first sample does not support claiming a Kansas City demand surge caused by ADESA. It also does not establish falling Kansas City consumer demand. Kansas-side licenses and online sales booked elsewhere are coverage gaps. No causal coefficient or local market-share estimate is model-ready.

### Reporting and license validation, 2026-10-29

- **Observed reporting scope:** Missouri's [Dealer and Business Operating Manual](https://dor.mo.gov/forms/Dealer-Operating-Manual.pdf), PDF page 31, requires monthly reports for each dealer number and includes both wholesale and retail transactions. [Form 385](https://dor.mo.gov/forms/385.pdf) summarizes new/used units without a separate retail-only subtotal. No public-report data dictionary was found demonstrating that the annual public counts remove wholesale. Therefore, classify the public counts as potentially mixed, not confirmed retail.
- **Observed continuity rule:** The same manual, section 11-2 (PDF page 46), permits the purchaser of a dealership to retain the seller's license number with authorization. Section 11-1 permits changes of address/name. A stable number and present-day label do not establish a constant historical business or location. No actual D4620/D2160 transfer history was established; the rule supplies a possible explanation, not proof of a particular transfer.
- **Observed chronology mismatch:** [Carvana's May 9, 2019 announcement](https://www.carvana.com/press/carvana-unveils-kansas-city-car-vending-machine/) dates the opening of the vending machine at 1700 W. 29th Street to that day and says Kansas City delivery launched just over a year earlier. The current D4620 entry nonetheless includes 2009 and 2012 counts. Those cannot be assigned to this vending-machine operation. D2160 also includes pre-acquisition/pre-integration counts, so its older rows are not Carvana megasite production.
- **Observed geography limitation:** The public file shows dealer addresses, not aggregate buyer locations. The underlying reporting form captures buyers, but those fields are not in this public annual summary. A dealer address cannot define resident demand or a reconditioning origin.
- **Observed timing limitation:** Reports are due by the following month's 15th. An October 6 report cannot be assumed to contain complete September reporting. Retain 2026 as partial with unknown coverage; do not annualize it or calculate YoY against full-year 2025.

**Revised analytical decision:** Do not expand a matched Carvana–CarMax demand regression from this series. The previously calculated -6.0% versus -8.9% changes remain arithmetic descriptions of selected license counts only; their roughly 3-percentage-point difference is not a retail share-gain estimate. The +230% Belton number is likewise not a production or consumer-demand estimate. Adding more dealers would not cure these definition problems. Preserve the free data for triangulation, but use disclosed regional inventory/sales comparisons and delivery-launch chronology for the next evidence layer. These are descriptive management evidence, not independent causal validation. A clean administrative test would require a free retail-only series with stable historical license mapping and defined geography; none was obtained in this bounded pass.

## Decision from the first pass

Current Carvana pages support a buyer ZIP based availability and delivery study. The inspected sample does not identify the reconditioning facility, so it cannot yet support a site-specific inventory cohort. Historical comparisons require an existing archive or historical feed; collecting today's surviving listings and looking up their histories would exclude vehicles already sold in the historical period.

Kansas City remains the strongest initial candidate because an August 2024 integration announcement is followed by a September 2024 same-day delivery announcement explicitly linking the service to the integrated site. Exact first production remains unknown. The proposed 2020–2022 comparison is useful background but is too distant to isolate this integration: use a closer 2023–2025 window where accessible, handling the announcement-to-service-launch period as a transition rather than imposing a known opening day.

## Observed website pilot

One search-results page was inspected using research ZIP 64012 (Belton, Missouri), followed by one vehicle's detail page, inspection checklist, printable inspection report and linked CARFAX report. This is a field-feasibility sample, not a representative inventory sample. Recommended ranking preferentially surfaces locally attractive cars.

| Field | Observation | Interpretation |
|---|---|---|
| Vehicle | 2022 Toyota RAV4 LE, vehicle ID 4782233 | Stable listing identifier observed |
| VIN | 2T3H1RFV5NW219806 | Allows deduplication and history matching |
| Stock number | 3006578006 | Observed; no facility mapping established |
| Mileage | 86,663 | Detail-page reading |
| Asking price | $22,990, previously displayed as $23,590 | Advertised prices, not realized transaction prices |
| Buyer location | ZIP 64012 / Belton, MO | Research query location, not vehicle origin |
| Delivery and pickup | Delivery today to Belton; pickup tomorrow at Kansas City; free shipping | Observed customer offer; does not identify storage or reconditioning site |
| Inspection date | Checklist: 09/23/2026; print report: September 24, 2026 | Unresolved one-day presentation discrepancy; preserve both |
| Facility identity | Not displayed in the inspected detail/checklist/print surfaces | Cannot assign this VIN to ADESA Kansas City |
| First listing, sale and acquisition dates | Not established | Inspection date is not a substitute |

Sources: [vehicle page](https://www.carvana.com/vehicle/4782233), [print inspection](https://www.carvana.com/vehicle/4782233/inspection-print), [linked CARFAX](https://www.carfax.com/VehicleHistory/p/Report.cfx?partner=CVN_0&vin=2T3H1RFV5NW219806). Live pages can change. Local evidence is under `work/adesa-pilot/` and is untracked. The CARFAX report loaded after an automatic device check; no user challenge was solved. Its inspected history did not establish a Carvana facility or completed current sale.

The location selector explicitly says it changes delivery options and shipping costs. A ZIP-filtered result set must not be relabeled inventory held at that ZIP. The displayed results count is not used as a local inventory estimate. New vehicles can appear among the results and must be excluded from a used-only study.

## Historical data and sales access

| Route | Verified public documentation | Remaining access or identification gap |
|---|---|---|
| MarketCheck | Historical listings since 2015; VIN history includes price, mileage, seller and first/last observations | Carvana historical completeness, site mapping and ability to enumerate historical cohorts unverified; no authenticated sample retrieved |
| MarketCheck past inventory search | Standard endpoint describes last 90 days; sold status is inferred from absence | Not a sufficient 2023–2025 backfill; confirm historical feed scope separately |
| Earnest Auto Seller Web Data | Start date 2016; advertised granularity aggregate, company/make | Useful possible national benchmark; public description does not establish local/VIN access |
| Mobility Global automotive data | US/Canada used transaction product advertises up to ten years and census-tract geography | Need seller attribution, definitions, licensing and access confirmation; CapIQ access alone is not confirmation |
| Missouri DOR | Dealer sales reporting exists; a route for bulk/custom records is described | No downloadable local Carvana sales panel obtained; aggregate/deidentified availability, geographic coverage and charges remain unknown |
| Crawl Feeds sample | Browser inspection verified a 2023 preview with vehicle-level addresses and location IDs | Location semantics and repeated historical observations remain unverified; not sufficient for site attribution or time-to-sale |

Sources and interpretation:

- [MarketCheck VIN history](https://developers.marketcheck.com/use-cases/vin-listing-history): price or mileage changes can create new rows, so row end dates are not vehicle sale dates. Group rows into continuous inventory episodes.
- [Past inventory search](https://docs.marketcheck.com/docs/api/cars/inventory/past-inventory-search) and [inferred-sale rules](https://docs.marketcheck.com/docs/guides/data/cars/inventory/key-concepts): a disappearance threshold is a vendor inference, not a confirmed retail delivery. Distinguish days at a source from days across all sources.
- [MarketCheck access and samples](https://www.marketcheck.com/support/faqs): sample datasets/trials exist, but entitlement and historical scope need confirmation.
- [Earnest product description](https://www.earnestanalytics.com/datasets/auto-sellers).
- [Mobility Global product description](https://www.mobilityglobal.com/en-us/products/automotive-market-data-analysis). The linked Market Monitor detail page returned an error in this pass; specific retailer-level fields were not verified.
- [Missouri DOR records](https://dor.mo.gov/sunshine-request/motor-vehicle-records.html) and [dealer reporting source](https://www.revisor.mo.gov/main/OneSection.aspx?section=301.280). Existence of reporting does not establish public access. Kansas City crosses the Missouri/Kansas border; Missouri-only data cannot stand in for the whole metro. Do not request personal buyer information.

## CapIQ Pro access check

At the user's request, inspected the open logged-in CapIQ Pro dashboard, Apps and Links menu, Sitemap and Mobility topic page. The Mobility entry is a news topic, not a vehicle-registration interface. The dashboard's Market Monitor is a securities monitor, not the similarly named automotive product. No historical inventory or dealer registration entitlement was established. This is a bounded navigation audit, not proof that the institution lacks every relevant license.

Retain CapIQ for company disclosures, transcripts and broker research. Some broker charts may contain useful estimates, but they do not establish access to the underlying local panel. No subscription, account, vendor message or paid data request was initiated.

## Next executable test and data specification

Seek a small historical sample before subscribing or expanding collection. Required scope: Carvana inventory episodes covering approximately September 2023–September 2025, including vehicles no longer listed today; two candidate markets plus a potential control, subject to verified geography. Requested fields:

1. VIN and listing/episode ID; source URL; original observation timestamps and crawl coverage.
2. Asking-price history; mileage, model/year/trim, new/used, partner inventory and availability/reservation status where available.
3. Geography with a definition: seller business address, storage location, reconditioning origin, pickup site and buyer ZIP are different fields. Unknown fields should remain unknown.
4. First/last listing and relisting records; explanation of inferred sales, cancellations, transfers and returns.
5. Delivery/fee history by query ZIP if retained. Ordinary dealer location alone cannot supply this.
6. For transaction data: month, aggregated buyer geography, normalized seller group, used retail units and corresponding market totals. No buyer identities.

Validate a small stratified set of historical VIN episodes before collecting a panel. Require consistency around price changes and relistings and compare aggregate inferred sales with disclosed quarterly units. That aggregate comparison calibrates coverage; it does not independently validate local geography or causal attribution.

Time-to-sale analysis should follow entry cohorts and retain unsold vehicles as censored observations. Comparing only sold vehicles or surviving listings would bias duration estimates. Separate inspection-to-availability, listing-to-reservation and reservation-to-completed-delivery where observable. A shorter listing duration can also result from lower pricing or an easier vehicle mix.

The immediate result is a partial feasibility pass: live field collection works; historical access and physical-site attribution do not yet pass. A more defensible fallback is a buyer-market study linking local Carvana registrations to integration exposure, with website delivery/selection as mechanism evidence. If neither historical route is available, retain descriptive evidence and start no large scrape merely to manufacture a weak proxy.

## Historical sample follow-up, 2026-10-29

The bounded follow-up found two public previews. Neither supports an ADESA effect estimate yet. No account, subscription, purchase or vendor message was initiated.

**Saturn Data:** The [AWS product](https://aws.amazon.com/marketplace/pp/prodview-y77x3t6zisn4w) links to a [ten-record GitHub sample](https://github.com/saturndatacloud/datasets/blob/master/Automative/Carvana/used%20cars/carvana_used_cars.csv). Rendered records are labeled sold on August 5, 2022. Fields include listing and stock IDs, vehicle characteristics, prices labeled sold prices, partner flag, delivery fee and earliest delivery date. There is no VIN, location, facility ID or first-listing timestamp. The definition of sold and whether prices represent completed transactions are unverified. GitHub reports a CSV formatting warning; raw-byte download failed, so no strict file-validation claim is made. This preview cannot measure local selling durations, and the advertised broader product coverage has not been validated.

**Crawl Feeds:** [Product preview](https://crawlfeeds.com/datasets/carvana) loaded through the browser after ordinary web retrieval timed out. The vendor advertises approximately 18,000 records and 43 fields; the visible offer was $115 one-time, not purchased. Preview records carry a May 27, 2023 scrape date. Examples:

| Vehicle ID | Location ID | Address shown | Qualification |
|---|---|---|---|
| 2662441 | 82 | 269 Dedham St, Norfolk, MA 02056 | Preview also labels this vehicle Partner Inventory |
| 2668122 | 209 | 200 N Main St, Manville, NJ 08835 | Address is associated with Carvana in NJ licensing records |
| 2623030 | 327 | 152 US HWY 206, Hillsborough, NJ 08844 | Facility function not verified |

The [NJ MVC autobody-facility list](https://nj.gov/mvc/pdf/business/autobody_fac.pdf) associates Carvana LLC with the Manville address. This corroborates a business location, not the sample vehicle's physical presence or reconditioning there in 2023. The preview does not define location, and its one-day observations do not establish longitudinal coverage. The service_from field predates the scrape substantially and must not be treated as first listing without a definition. Partner inventory also needs separate treatment. Browser evidence saved locally at `work/adesa-pilot/2026-10-29-crawlfeeds-preview-ax.txt`.

**Decision:** Location-bearing historical records are a credible lead, so site-level research is not ruled out. However, neither preview passes the two required tests: defined physical geography and repeated vehicle observations around the 2024 integration. Do not purchase the static dataset as a substitute for a historical panel. No numerical growth, conversion or duration assumption from these previews can enter the forecasting model.

### Reviewable vendor inquiry — not sent

Suggested first recipient: contact@crawlfeeds.com, as listed on the product page. Its preview directly exposes the location field whose meaning is the immediate question. MarketCheck remains an alternative if longitudinal coverage is unavailable.

> I am evaluating historical Carvana inventory data for research on reconditioning-site expansion. Before purchasing, could you clarify whether the location object (address and locationId) represents the vehicle's physical storage location, reconditioning facility, pickup location, seller address or the shopper's selected location? Does its meaning differ for Partner Inventory?
>
> Do you retain repeated observations covering September 2023–September 2025, including vehicles sold or removed before today, rather than only the May 27, 2023 snapshot shown in the preview? Could you provide a small sample following approximately 20–30 vehicles across multiple observations, including price changes, removals and any relistings, with original timestamps and collection frequency? Kansas City/Belton and one comparison market would be useful if the location definition permits that selection.
>
> Please explain how listing removals are distinguished from sales, reservations, transfers and cancellations, and whether location IDs can be mapped to facility types over time. Please also confirm historical coverage, gaps, licensing and cost before any order. No personal buyer data is needed.
