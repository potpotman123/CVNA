# ADESA pilot feasibility findings

As of 2026-10-29. First bounded pass under the [research plan](adesa-research-plan.md). No before/after sales estimate or site-return estimate is yet supported.

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
| Crawl Feeds sample | Search surfaced a 2023 vehicle sample with a location-shaped field | Full-page retrieval timed out; semantics/history not verified; excluded from analytical evidence |

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
