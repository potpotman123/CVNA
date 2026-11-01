# ADESA versus original IRC geography

Completed November 1, 2026. Integration categories fixed at September 30, 2026.

## Finding

The geographic evidence supports a qualified version of Citizens’ claim: integrated ADESA sites are generally closer to their assigned major-city reference points than original IRCs. This is useful evidence of location differences, **not a measured delivery-time, hiring or sales benefit**.

| Group | Located / primary roster | Median straight-line miles | Within 25 miles |
|---|---:|---:|---:|
| Original IRCs | 17 / 18 | 19.6 | 65% |
| Integrated ADESA candidates | 21 / 21 | 12.5 | 86% |
| Other ADESA entries | 34 / 35 | 10.4 | 88% |
| All primary ADESA entries | 55 / 56 | 11.5 | 87% |

Open [interactive map](map.html), [distance table](facility-distances.csv), or [complete calculations and alternate-city distances](comparison.json). Filter categories, select a city to zoom, or click a marker/row for its address and coordinate source. Faded markers indicate approximate coordinates or excluded records.

The roster contains 18 originals and 57 ADESA directory entries. Queen City is mapped but excluded from primary statistics because its operating status is unresolved. This exclusion is a working choice, **not proof that the remaining 56 precisely reproduce the acquired estate**. Including it changes the all-ADESA median only from 11.55 to 11.47 miles. The 21 integrations are a previously reconstructed candidate roster, not a company-certified census. “Other” means no confirmed integration at the Q3 cutoff; Orlando’s later October announcement does not change that category.

## Same-city comparisons matter more than the aggregate alone

| Market | Original IRC miles | Integrated ADESA miles | Interpretation |
|---|---:|---:|---|
| Atlanta | 40.3 | 16.9 | Strong central-proximity improvement |
| Chicago | 27.2 | 33.4 | ADESA is farther; adds a different side of the metro |
| Dallas | 31.2 | 12.1 | Closer to Dallas, but not Fort Worth |
| Indianapolis | 13.2 | 10.4 | Modest difference |
| Phoenix | 10.8 | 11.5 | Essentially similar proximity |

Five of seven available integrated-site same-city comparisons favor ADESA; two original-site coordinates in those seven are approximate. Excluding those two leaves three of five favoring ADESA. The sample is small and selected by overlapping markets.

**Dallas–Fort Worth is the clearest warning against overclaiming:** using Fort Worth instead, Blue Mound is 8.5 miles away and ADESA Dallas is 34.8 miles away. The economic argument here is complementary coverage, not a universally superior central location.

## Robustness and missing observations

- Excluding all five approximate coordinates: original median 19.9 miles; integrated ADESA 12.5 miles. Original strict sample is 14 located facilities, versus 17 in the primary calculation.
- Excluding sites with an explicitly ambiguous city assignment: original median 16.0 miles; integrated ADESA 12.4 miles. The gap narrows.
- Unmatched: **Carvana West Memphis and ADESA St. Louis**. Neither is mapped or counted as zero. Town coordinates and unrelated business matches were rejected.
- Approximate: Haines City and Concord road locations; Rocklin exact street address but another named occupant; Jacksonville conflicting address results; Pittsburgh road location. These five are excluded from strict statistics.
- Inserting any nonnegative distance for the missing original IRC puts the complete 18-site original median between 18.1 and 21.5 miles, still above the integrated median.
- Census results are address-range interpolations, not verified rooftop or gate locations. This is an approximate regional geographic comparison.

## Method and reproducibility

1. Start with the existing `../facility-register.json`; preserve integration classifications and save address inputs in `facility-inputs.json`.
2. Assign common major-city reference points in `../geography-config.json` before computing distances. Explicit alternatives cover polycentric or ambiguous markets; do not select the closest town separately for each facility.
3. Geocode addresses with the Census geocoder. Review unmatched cases with OpenStreetMap/Nominatim, Photon and named parcels. Cache responses and record accepted overrides in `coordinate-review.json`.
4. Calculate Haversine distance with Earth radius 3,958.7613 miles. Summaries exclude missing values and use clearly identified eligible populations. The map projection does not determine the distance calculations.
5. Generate JSON, CSV and a self-contained offline HTML map. Reproduce without network access from the repository root:

```sh
python3 research/volume/capacity/geography-analyze.py
```

Collection scripts `geography-fetch.py`, `geography-fallback.py`, `geography-photon.py` and `geography-address-review.py` document the retrieval steps and use cached public responses. They are unnecessary for recalculation. `business-name-review.json` preserves rejected final searches. No licensed report text is included.

City points are **GeoNames populated-place reference coordinates**, not formally measured CBD boundaries, city halls or population-weighted customer centers. They are a consistent proxy for this first comparison. Distance alone does not establish where customers or qualified workers live. The result must not be entered into a volume forecast as a conversion or delivery elasticity.

Address corrections include Delanco’s 600 Creek Road and Greenfield’s alternate 6369 W 300 N address from the expanded establishment record (see `../equipment-followup-2026-10-31.md`). A Census result for ADESA New Jersey incorrectly matched South Main Street; it was replaced with the named North Main Street parcel. These checks matter more than extra decimal precision.

## Source provenance

- Facility population and integration status: existing `../facility-register.json` and its provenance; [ADESA location directory](https://www.adesa.com/auction-location/).
- [US Census geocoding service](https://geocoding.geo.census.gov/geocoder/): exact request URLs and returned matches in `census-geocodes.json` and `address-variants.json`.
- [GeoNames cities15000 data](https://download.geonames.org/export/dump/cities15000.zip), US subset in `city-points.json`; individual GeoNames IDs and URLs are retained per facility. Attribution: GeoNames, CC BY 4.0.
- [OpenStreetMap](https://www.openstreetmap.org/copyright) contributors, ODbL; Nominatim and Photon responses retained with request URLs. Named Chicago, Kansas City and New Jersey parcels are linked in `coordinate-review.json`; Mapcarta is a view of OSM evidence, not an independent second source.
- [Delanco municipal master-plan reexamination](https://www.delancotownship.com/filestorage/5328/6391/6479/6752/2019__Master_Plan_Reexamination_Report.pdf), supporting the IRC street address.
- State outline rendering: [PublicaMundi MappingAPI US states GeoJSON](https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json), retrieved November 1, 2026. Outlines are visual context only.

## Checks and remaining questions

Arithmetic checks cover unique facility names, group counts, missing/approximate populations, coordinate ranges and Haversine sanity checks. Browser checks cover all 73 mapped locations, category filters, city zoom, marker details and absence of script errors; national and Chicago views were visually reviewed.

This can enter the memo as evidence of differing geography. It does not independently verify legacy zoning advantages, reduced delivery times, a larger skilled-labor pool, or profitable incremental demand. Best next evidence would be matched road-time/customer-population coverage or hiring-catchment evidence for a few contrasting metros, rather than treating every mile toward downtown as equally valuable.
