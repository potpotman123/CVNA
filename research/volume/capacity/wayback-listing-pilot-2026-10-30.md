# Carvana listing / Wayback feasibility pilot — 2026-10-30

## Result

Pickup location cannot be used as a processing-IRC identifier. A same-vehicle ZIP experiment changes the pickup destination. The small archive pilot did not recover a reliable IRC field or a facility-level inventory/production series. This is a feasibility finding, not proof that every archived page lacks useful information.

## Live same-VIN experiment (observed)

Listing: https://www.carvana.com/vehicle/4782233?refSource=srp

2022 Toyota RAV4 LE; VIN **2T3H1RFV5NW219806**, stock 3006578006; 86,663 miles; $22,990. Changed only the shopping ZIP through the pickup selector; did not initiate a purchase.

| Shopping ZIP | Pickup displayed | Delivery displayed | Shipping |
|---|---|---|---:|
| 64012 | Kansas City, MO, tomorrow | Belton, MO, today | Free |
| 33844 | Orlando, FL, Thursday November 5 | Haines City, FL, Wednesday November 4 | $1,290 |

The vehicle/VIN and price remained unchanged. Destination labels therefore cannot assign a car to Haines City's IRC, Orlando, or Kansas City's processing operation. Shorter delivery and cheaper shipping may be consistent with proximity, but do not independently identify where reconditioning occurred. No explicit processing facility was found in the rendered vehicle details; the inspection navigation did not reveal a usable location field in this session.

Official explanatory sources:
- https://www.carvana.com/help/carvana-inventory/where-are-carvana-cars-located — nationwide inventory; ZIP determines pickup/delivery options.
- https://www.carvana.com/help/pickup-and-delivery/why-has-my-vehicle-appointment-been-delayed — vehicles stored at reconditioning centers and transported to a nearby Carvana location after purchase approval.

## Archive observations

Directory: https://web.archive.org/web/*/https://www.carvana.com/vehicle/*

The interface reported more than 10,000 captured URLs. This is **not** 10,000 unique vehicles or a complete historical census: URL variants, query strings, duplicates and other paths can be included. URL-directory filtering is not a capture-year filter.

| Capture tested | Visible result | Site attribution |
|---|---|---|
| [2021-10-22, vehicle 2024024](https://web.archive.org/web/20211022072756/https://www.carvana.com/vehicle/2024024) | 2019 Dodge Journey SE, $24,990, 9,486 miles; partial page and vehicle-details navigation | No usable IRC identifier recovered |
| [2022-05-14, vehicle 2361117](https://web.archive.org/web/20220514233357/http://www.carvana.com/vehicle/2361117) | 2014 INFINITI Q50 3.7 Premium, $24,990, 47,069 miles; partial page and 150-point-inspection navigation | No usable IRC identifier recovered |
| [2023-03-26, vehicle 2655597](https://web.archive.org/web/20230326081245/http://carvana.com/vehicle/2655597) | Replay said URL not archived, despite directory lead | Not inspected successfully |
| [2025-08-28, vehicle 1415822](https://web.archive.org/web/20250828181140/http://carvana.com/vehicle/1415822) | Replay said URL not archived, despite directory lead | Not inspected successfully |

Method: ordinary browser navigation, rendered page/accessibility inspection, vehicle-detail and inspection-section navigation. No bulk scrape, hidden application-state extraction, or exhaustive archive coverage test. Dynamic sections and incomplete captures limit what this pilot establishes.

## Implication for the staffing/output test

Do not enter pickup-market listing counts as IRC output. Three separate links must be verified: vehicle-to-processing-site attribution; sufficiently consistent historical observation; and a distinction between listing stock, completed production and retail sale. Listing disappearance alone is not a verified sale, and historical snapshots omit cars appearing and disappearing between captures.

The next potentially discriminating check is a small sample of public vehicle-history/service entries for an explicitly named Carvana inspection facility and dated preparation event. Dealer or sale location alone remains insufficient. Broad Wayback collection is not justified until site attribution is established. Follow-up findings below supersede the initial untested status of this lead.

## Follow-up: linked histories and full inspection checklists

Observed 2026-10-30; two current vehicles, convenience sample, not representative. Access was free through the listing links. CARFAX loaded after its automatic device check; no CAPTCHA interaction or purchase was needed. Read rendered reports, not hidden application state. No bulk collection.

### New usable field: dated Carvana inspection

Navigate listing → Inspection → scroll to load section → View complete 150-point inspection. The modal supplies VIN, stock number and an **Inspected On** date. This section required scrolling to finish loading; the initial pilot's unsuccessful navigation should not be interpreted as absence of inspection data.

| Vehicle ID / VIN | Modal inspection date | Printable report | Location field |
|---|---|---|---|
| 4782233 / 2T3H1RFV5NW219806 | 09/23/2026 | September 24, 2026 | None found in complete checklist or printable version |
| 4835052 / 2T3W1RFV1NW203299 | 10/13/2026 | Link exposed; not read | None found in checklist |

Sources: https://www.carvana.com/vehicle/4782233?refSource=srp#inspection ; https://www.carvana.com/vehicle/4782233/inspection-print ; https://www.carvana.com/vehicle/4835052#inspection

Preserve the first car's one-day display discrepancy; timezone conversion is a possible explanation, not verified. Inspection date is not established as final production release, listing start, or sale date. On October 30, the first vehicle was listed 36–37 days after the displayed inspection dates; that is an elapsed-time observation, not verified days-on-market. A sample of currently listed cars preferentially includes slower-selling stock, so its inspection-date distribution cannot measure historical production volume.

### Linked histories: locations are real, but event meaning is decisive

First car's [CARFAX](https://www.carfax.com/VehicleHistory/p/Report.cfx?partner=CVN_0&vin=2T3H1RFV5NW219806) includes named service businesses/towns, including Warrensburg, Missouri, on December 23, 2025. September 17, 2026 records dealer titling while in inventory in Helena, Montana at 86,202 miles. Summary labels the vehicle last owned in Montana. This does not establish physical travel to Montana or processing there. No Carvana-specific preparation event was identified. Its [AutoCheck](https://www.carvana.com/vehicle/autocheck/4782233) also has the Helena title event, but provides less precise location information for several service records. Both reports disclose incomplete reporting.

Second car's [CARFAX](https://www.carfax.com/VehicleHistory/p/Report.cfx?partner=CVN_0&vin=2T3W1RFV1NW203299) shows Orlando/Kissimmee ownership and service history. September 1, 2026 has an unspecified inspection event; September 18 has a Florida DMV repossession/title entry with Wilmington, Ohio shown; October 2 has an unnamed online-sale listing. Carvana's own October 13 inspection is distinct from that September inspection. Neither the Ohio title entry nor the nearby Florida service history identifies its processing IRC. Current listing offered free shipping and Orlando pickup tomorrow, consistent with local availability but not proof of Haines City processing.

### What can enter the model

- **Observed:** VIN-linked inspection dates; dated named service locations; title/registration locations and event types; current listing presence.
- **Not identified:** Carvana acquisition date, processing IRC, final production-release date, first Carvana listing date, retail-sale date, or per-site production totals.
- **Useful next discriminator:** a named Carvana service/inspection event near the Carvana checklist date, or an inspection document explicitly naming the facility. Prior-owner service geography is only a sourcing-region clue until acquisition and routing are validated.
- **Historical route:** archived full inspection/print pages may preserve inspection timing more cleanly than dynamic listing summaries; this remains untested. It would still require facility attribution and coverage validation before a staffing-to-production test.

Decision: meaningful progress on timing, no defensible facility assignment yet. Do not substitute last-owned state, title city, pickup destination, or generic inspection events for an IRC identifier.

## Three-vehicle bounded municipal-attribution test

2026-10-30 follow-up at user request. Selected three additional vehicles from the first listing's recommendation links (4851314, 4777903, 4808559). All are RAV4s: convenience sample, not random, no Massachusetts-specific vehicle selected. Read each full inspection modal and linked CARFAX. Classified physical service events separately from administrative title/registration events. No longitudinal tracking or sale observation was performed.

| Listing / VIN | Carvana modal inspection | Recent observed geographic evidence | Conditional processing candidates | Assessment |
|---|---|---|---|---|
| [4851314](https://www.carvana.com/vehicle/4851314) / 2T3F1RFV1MW194974 | Oct 19, 2026 | July 16 service at Walmart, Fayetteville WV, 82,810 miles; July 30 registration Danese WV | No useful single candidate; broader eastern network remains possible | Prior-use area identifiable; 95-day service-to-inspection gap too weak for processing assignment |
| [4777903](https://www.carvana.com/vehicle/4777903) / JTMW1RFV1PD100934 | Sept 23, 2026 | Aug 27 service at Toyota of Melbourne, FL, 88,875 miles; Sept 7 Montana purchase report; Sept 30 dealer-inventory title Helena MT, 89,007 miles | Haines City is a plausible central-Florida candidate; Bradenton integration is another regional possibility. Sanford announcement Oct 6 postdates this inspection and is not evidence of September operations | Strong recent prior-use/sourcing-area clue, 27-day service gap; low-confidence processing-region hypothesis, not validated IRC attribution |
| [4808559](https://www.carvana.com/vehicle/4808559) / 2T3H1RFV5MW120840 | Oct 5, 2026 | July 21 service Princeton TX, 94,804 miles; Sept 15 lien-release title Princeton; Sept 30 Montana purchase report; Oct 2 dealer-inventory title Helena MT, 99,356 miles | Dallas–Fort Worth region: Hutchins ADESA Dallas or original Blue Mound IRC, conditional on local processing | Prior-use area identifiable; 76-day service gap; administrative September events do not prove continued physical presence |

Linked CARFAX reports use `https://www.carfax.com/VehicleHistory/p/Report.cfx?partner=CVN_0&vin=` followed by the VIN in the table. All reports accessed via public listing links. Service-to-inspection gaps are calendar-date subtraction. Exact acquisition dates, actual routing and whether service occurred before acquisition remain unknown. Mileage changes do not bound transport distance because vehicles can travel on trucks.

Outcome: **3/3 have identifiable recent prior-use towns and inspection dates; 0/3 have a geographically identified Carvana processing event.** Two support tentative regional candidate sets under an explicit local-processing assumption. Do not translate this into a measured classification accuracy or production count. Report abstentions rather than forcing nearest-site assignments. No numeric probabilities or road-distance rankings estimated.

Massachusetts check: [Carvana's Nov 20, 2024 announcement](https://www.carvana.com/press/carvana-announces-auction-irc-megasite-integration-in-boston-area/) identifies ADESA Boston in Framingham as a retail IRC integration. It is the sole Massachusetts retail-integrated location identified in the current project register, not an independently exhaustive census. ADESA Concord in Acton is a separate auction property without confirmed retail integration in that register. Even one identified in-state IRC does not imply every Massachusetts-source car uses it; out-of-state routing remains possible. Do not invent a Massachusetts match from this non-Massachusetts sample.

Facility check: [ADESA Dallas integration announcement, Aug 26, 2025](https://www.carvana.com/press/carvana-brings-inspection-and-reconditioning-center-capabilities-to-adesa-dallas/) places the facility in Hutchins; [official directory](https://www.adesa.com/auction_location/adesa-dallas/) gives 3501 Lancaster-Hutchins Road. Original Blue Mound is in the existing facility register. These demonstrate competing DFW candidates, not which handled the sampled car. Existing register also supplies Haines City, Bradenton and Sanford evidence/timing. Announcement dates are not exact production starts.

Decision: feasible for a small **sourcing-geography** proxy and candidate-site hypotheses, not yet suitable for the causal staffing/output panel. The key unvalidated assumption is local processing, not address precision. A verified-origin calibration sample would be needed before assigning historical units to sites or interpreting changes as production growth.
