# Seattle: free public-data feasibility

Checked 2026-10-29. Question: did the Auburn ADESA retail integration increase Carvana retail sales among nearby buyers relative to other markets? Scope: existing public sources only; no paid access, outreach or bulk collection.

## Event evidence

- [July 28, 2025 company announcement](https://press.carvana.com/carvana-brings-inspection-and-reconditioning-center-capabilities-to-adesa-seattle/): plans to add inspection/reconditioning at ADESA Seattle in Auburn, Washington. Announcement date is not a verified production start date.
- [September 4, 2025 same-day delivery announcement](https://press.carvana.com/carvana-expands-same-day-delivery-to-seattle/): eligible greater-Seattle customers/vehicles receive same-day delivery; company credits regional IRCs and its fleet. Does not isolate Auburn's contribution or disclose local sales. July–September is a candidate transition window; Q4 2025 is the first full quarter after the service announcement, not a verified first full production quarter.

## Washington title dataset: field audit

[Washington DOL Vehicle Title Transactions](https://data.wa.gov/Transportation/Vehicle-Title-Transactions-by-Department-of-Licensing/cdk6-5kdf/about_data), inspected in the public browser UI, including both pages of its column dictionary. Metadata: updated October 21, 2026; January 2017–September 2026; roughly 14.1 million rows; 21 columns. Rows are aggregated counts, not individual sales.

Columns: transaction month/year; make; model; model year; primary color; vehicle type; primary use; GVWR class; GVWR range; primary fuel; secondary fuel; electrification level; new/used; owner type; county; state; ZIP; transaction type; transaction channel; 2020 census tract; vehicle record count.

Buyer geography and new/used flags make this useful local market context. There is **no seller/dealer identifier**, so it cannot supply the Carvana numerator. Transaction channel means DOL processing channel (online/in person/mail), not ecommerce vehicle purchasing. Month reflects recording in DOL's system, not necessarily sale month. Original titles include first Washington titles for used vehicles imported from elsewhere; transfers reflect ownership changes of already-Washington-titled vehicles. Do not interpret the total as dealer retail sales: private transfers and other ownership changes are not separated into a clean comparable retail population.

## Result and stopping rule

Bounded searches across company releases, Washington open data, local government documents and indexed local/news coverage found no validated free Seattle Carvana buyer-market unit series. License lists and complaints do not provide it. No bulk dataset download or causal estimate was produced.

Observed: local service availability improved after an integration announcement. Unknown: local Carvana units/share before and after, exact production start, incremental sales attributable to Auburn. Evidence can support the delivery-cost/convenience mechanism qualitatively; it cannot calibrate a sales-growth coefficient. A present-day ZIP-level delivery/selection comparison could test service differences, but would not recover historical local sales. Stop expanding this route unless a concrete seller-linked public source emerges.
