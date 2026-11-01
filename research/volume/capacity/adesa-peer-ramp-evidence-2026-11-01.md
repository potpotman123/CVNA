# Peer reconditioning ramp benchmarks

November 1, 2026. Supersedes the earlier practitioner-only 12-month/90%-endpoint proposal. User specifies a linear ramp to 100% of management's 13,000 annual capacity. Proposed timing: 9 months base, 6 fast, 18 slow. These are analog-informed assumptions, not measured CVNA ADESA ramps.

## Strongest directly comparable time benchmark

Aramis Group FY2021 sales call, November 9, 2021, PDF p8. Management describes opening refurbishing hubs and staffing additional shifts progressively. It states a typical six-to-nine-month ramp with target capacity around 15,000 cars per hub, varying by geography. This matches ADESA's 13,000 standard integration far better in scale and activity than a large greenfield IRC. Aramis operates online used-car retail and internal vehicle refurbishment. European hiring, shifts, vehicle mix and building configurations differ.

Source: https://aramis.group/wp-content/uploads/2025/05/aramis-group-2021-sales-audio-transcript.pdf

Classification: management description of typical practice applied to planned hubs, not an independently audited opening-to-full-output panel. The 2025 URL directory is not the event date; transcript header dates the call in 2021.

## Slower facility-specific plan and evidence that economics affects timing

Aramis Nemours inauguration release, June 29, 2022, pp1–2: two production lines, approximately 5,000 square metres of building space, and full capacity expected by end-2023. This implies roughly 18 months from inauguration. The release says French capacity would double to 50,000/year; approximately 25,000 is consequently an inferred site addition, not a separately stated output observation. Planned employment 150. This is a larger planned facility and supports a slower case, not proof it actually met that deadline.

Source: https://ml-eu.globenewswire.com/Resource/Download/561749a5-96d8-46aa-bc2b-2781110221e5

Aramis FY2022 results, December 1, 2022, explicitly say Antwerp (inaugurated November 2021) and Nemours (June 2022) ramping was adjusted to effective demand. Therefore staffing capability and economically justified realized output are distinct. This follow-up does not validate the original six-to-nine-month schedule as universally achieved.

Source: https://www.globenewswire.com/news-release/2022/12/01/2566215/0/en/Aramis-Group-2022-annual-results.html

## CarMax cross-check: useful but not a precise site ramp

CarMax opened its first standalone recon center in the Atlanta metro in Q4 FY2024 (December 2023–February 2024). On June 20, 2025, management said one standalone center was probably fully ramped, without naming it. Chronology is consistent with roughly 16–18 months between first opening and the later report, but does not establish which site, when it reached capacity, or the duration required. Do not label this a measured Atlanta 18-month ramp.

Sources:
- https://investors.carmax.com/news-and-events/news/news-details/2024/CarMax-Reports-Fourth-Quarter-and-Fiscal-Year-2024-Results/default.aspx
- https://www.roic.ai/quote/KMX/transcripts/2026-year/1-quarter (management transcript hosted by third party; query 'fully ramped')

## Rejected or weaker routes

- AUTO1 Hemau disclosures identify opening and capacity expansion, but no matched achieved-output endpoint recovered. Increasing design capacity is not reaching that capacity. Vendor site and older releases also differ in opening year; not used to time the ramp.
- Cazoo/Vroom searches found ramp descriptions, outsourcing and macro-demand constraints, but no stronger verified site-level duration in this pass.
- Buffalo's roughly tenfold 'business' growth remains undefined and cannot calibrate production.
- The former CVNA director's 120-day estimate concerns staffing a single line-shift, not a whole site's realized production.

## Working numerical application

Use 13,000 annual capacity, linear output-rate ramp from zero at first production, then hold at 100%. The analogue informs duration; the linear shape is the user's simplifying choice, not observed monthly performance. No 90% endpoint remains.

| Case | Months to full rate | First rolling 12 months output | Second rolling 12 months output | Mature annual |
|---|---:|---:|---:|---:|
| Fast | 6 | 9,750 | 13,000 | 13,000 |
| Proposed base | 9 | 8,125 | 13,000 | 13,000 |
| Slow | 18 | 4,333 | 11,917 | 13,000 |

For a nine-month ramp, first-year output is 13,000 × [(9/12 × 1/2) + 3/12] = 8,125. Five sites on identical age clocks produce 40,625 in their first twelve months, rising to 65,000 annually. Calendar-year forecasts require actual/proxy start dates; baseline production must be subtracted to find incremental growth.

Reproduce with `python3 research/volume/capacity/adesa-ramp-benchmark-calculate.py`. Formula integrates rate over time. The slow-case two-year cumulative total is 16,250; fast/base second-year output equals capacity. This is arithmetic validation, not empirical validation.

Decision: the peer evidence supplies a much better reason for a 6–9-month normal ramp than the previous arbitrary 12-month extension. The 18-month alternative accommodates larger setups, hiring or demand delays. No verified independent production panel establishes that every ADESA integration achieves these dates. Stop the search expansion here: the relevant evidence is sufficient for explicitly benchmarked scenario timing.
