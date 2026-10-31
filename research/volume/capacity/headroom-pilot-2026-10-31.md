# Operating and physical headroom: municipal-record pilot

Research date: October 31, 2026. Follow-up to the [sellside synthesis](../../sellside/2026-10-31-expanded-synthesis.txt) and [operating ramp evidence](ramp-evidence-2026-10-30.md).

## What changed

**A concrete expansion option on existing ADESA land is now supported by detailed municipal plans and a subsequent watershed approval. Current site operating utilization remains unmeasured.** The strongest new case is Dayton, Minnesota (ADESA Minneapolis): a roughly 68,000-square-foot repair/detail building would replace approximately 350 parking spaces. Parking headroom and production headroom can move in opposite directions.

This is a purposive pilot, not a random sample or a national estimate. Elyria, Haines City and Tolleson were chosen for existing operating evidence; Boston and Belton for contrasting ADESA footprints. Dayton was added after a concrete municipal-document lead. No current nationwide aerial census or parking-occupancy survey was completed. The useful imagery was the dated planning packet's aerial/plan overlay and survey; its underlying aerial acquisition date is unknown.

## 1. Dayton: independent evidence of a physical expansion route

Address: 18270 Territorial Road, Dayton, MN; marketed as ADESA Minneapolis.

The January 27, 2026 city packet, PDF pp128–131, describes a proposed **68,791 sq ft**, single-story minor-repair/detail building including washing, painting and photography. It sits on existing paved vehicle storage. The relevant parcel is **35.54 acres**; the staff report describes the broader three-parcel use as **40.41 acres**. Neither number should be confused with the acreage of every boundary shown on the survey.

The site had approval for **over 2,000 parking spaces**. The proposed building removes **roughly 350**. These are planning counts, not measured occupancy or retail-only storage. The original car-wash addition failed setback requirements and was moved into the new building. This is direct evidence that owned land does not imply unrestricted placement of equipment or structures.

The packet's aerial overlay (p132), survey (p145), preliminary floor plan (p152) and engineer's letter (p154) were inspected. They expose stage-specific work areas, easements, wetland/utility considerations and approval requirements. They do not establish present equipment installation, staffing or output. Paint-labelled positions in a preliminary plan are not automatically certified operational paint booths.

A later watershed record, June 10 packet p70, describes **67,400 sq ft**, **35.5 acres**, **6.50 acres disturbed** and **0.01 acre less impervious surface**, with a complete application received March 25. It states approval occurred **April 8, 2026**, conditioned on escrow reconciliation and an operations/maintenance plan if required by the city. Preserve the building-area difference between document versions; do not average them or infer extra facilities. The January packet contains a proposed council resolution, not by itself proof of council adoption. Watershed approval is verified; city-final/building-permit, construction-completion and production-start dates were not independently established in this pilot.

**Interpretation:** an existing property can accommodate additional processing infrastructure, but achieving that requires construction, utilities, equipment and commissioning. This case does not prove cheap staffing-only growth, establish annual output, or identify Dayton as one of the three company-announced 2027 buildouts. Do not add an assumed Dayton capacity to management's capacity total: it may already be included.

Sources: [Dayton January packet](https://www.daytonmn.gov/Documents/Government/Mayor%20and%20Council/Meeting%20Packet/2026/01-27-26%20Council%20packet.pdf?t=202601231116000); [June watershed packet, p70](https://www.elmcreekwatershed.org/uploads/5/8/3/0/58303031/june_10_2026_regular_meeting_packet.pdf).

## 2. Three original IRCs: what the operational test can actually say

| Site | Existing evidence retained | New evidence or retrieval result | Still needed to estimate headroom |
|---|---|---|---|
| Elyria/Lorain, Ohio | Citizens June 4 tour reports ~1,280 produced/week, four physical lines and two shifts; JPM June 5 uses ~1,300 weekly capacity. Same event, not independent confirmations. | Ohio EPA portal lists June/August 2026 air-permit approval/acknowledgement records for facility 0247082027. Document bodies could not be retrieved. | Current booth/equipment schedule, productive hours, paint incidence, repair complexity, downtime, queues and comparable-period output. |
| Haines City, Florida | MS tour's 6,000 cars / 15,000 parking spaces is 40% parking occupancy, not factory utilization. OSHA 2025 average workforce 486 vs 716 in 2022 is neither skilled-FTE utilization nor a matched output comparison. | Public hiring material corroborates advertised first/second-shift work, not filled positions or incremental headcount. | Resolve physical-line versus line-shift descriptions; obtain completed output and stage-level resources/workload. |
| Tolleson, Arizona | Historical supplier design: three four-booth lines rated 30 paint jobs/day each; phase one eight booths, later phase prospective. | No verified current configuration or output series found. | Completion/current equipment, productive schedule and actual cars needing paint. Historical design is not current demonstrated throughput. |

Prior evidence locators: sellside synthesis sources 28 p2 and 29 p2 (Elyria), 34 pp1–2 (Haines); [staffing panel](staffing-recovery-2026-10-30.md); [Rely-On/Garmat historical project](https://relyonusa.com/carvana-silicon-valley-meets-collision-repair/).

Ohio document metadata: P0140559 June 4 (doc4140973); P0140630 August 19 (doc4236308 and doc4236309). Two August documents do not establish two expansions. Approval/acknowledgement labels do not identify new equipment. The downloaded responses were HTML challenge pages, not permits; filenames were corrected. [Ohio EPA portal](https://edocpub.epa.ohio.gov/publicportal/edochome.aspx). Advertised roles: [Elyria](https://www.carvana.com/careers/apply?gh_jid=8301769), [Haines](https://www.carvana.com/careers/apply?gh_jid=8181016). No headcount estimate is inferred from postings.

## 3. Conditional paint test, not a growth forecast

For a fixed target of 1,280 completed vehicles/week, paint demand equals total completed vehicles times the fraction requiring paint. At hypothetical paint incidence of 30%, 50% and 70%, that is **384, 640 and 896 paint jobs/week**. These are required loads, not equipment capacities. They assume one paint-job-equivalent per affected vehicle; multiple panels, repeat work and differing job durations complicate the mapping.

A useful stage equation is:

`weekly supported total vehicles = productive paint-resource hours / (paint incidence × average resource-hours per painted vehicle)`

Apply the analogous calculation to bodywork, mechanical work, inspection and downstream release. The smallest supported output constrains the system; staffing or speeding one stage may simply move the queue. Productive resource-hours must account for shifts, downtime, skills and equipment constraints without double-counting labor and booth hours.

At unchanged paint resources and hours/job, reducing incidence from 70% to 50% increases paint-supported total throughput 40%. This is sensitivity arithmetic, not evidence that mix caused Carvana's reported growth. It illustrates why recovering older/cheaper inventory could consume apparent headroom. Reproducible arithmetic is in `headroom-pilot-calculations.json` and `headroom-pilot-calculate.py`.

## 4. Other leads and limits

- **Belton / ADESA Kansas City:** July/August 2026 secondary council transcripts describe an approximately 93,440–93,444 sq ft maintenance building, roughly 90 indoor vehicle positions, a roughly 1,000–1,050 sq ft wash and restriping/reorientation of over 12,500 spaces. These are secondary leads, not primary-verified approval, completion or throughput. Cross-jurisdiction Kansas City/Belton boundaries may matter. Do not enter quantities in the capacity model. [July meeting](https://www.myhamlet.com/belton-mo/city-council--1834/07-14-2026/565f0083-d0a2-4a95-a3d7-282ce37e5c2b); [August meeting](https://www.myhamlet.com/belton-mo/city-council--1834/08-11-2026/c77daabb-0ae1-4af9-99c1-a0f0cc6ca6b6).
- **Boston / Framingham–Sherborn:** found a primary special-permit application but readable text/rendering was unavailable in this pass. Historical local reporting describes a disputed parking extension; current outcome unverified. No usable-space or processing estimate. [Application](https://sherbornma.org/DocumentCenter/View/3267/Adesa-Application-2025).
- Google Maps location inspection did not yield a validated parcel/imagery-date/occupancy measurement. No unverified image counts entered the register.

## Decision and next evidence

**Supported:** property-level construction options exist, and public plans can expose real constraints much better than counting apparently empty parking. Physical expansion and staffing/productivity expansion are distinct investment routes.

**Still unproven:** the fraction of the network that is cheaply rampable, current stage-level utilization, incremental throughput per technician, time/cost to reach it, or demand at acceptable returns. This pass does not justify increasing a numerical production-growth forecast.

Prioritize obtaining the content of the identified Elyria permits and a matched equipment/shift/paint-workload description over further broad satellite collection. For Dayton/Belton, contractor commissioning or final building records would move the evidence from planned space to installed capability. A second observed operating date with comparable repair mix is needed to test productivity rather than infer it from staffing. Stop at these named gaps if public access fails; more job postings or parking counts will not solve them.

Keep future sales absorption, inventory aging, financing concessions and cash returns separate: even demonstrated additional processing capacity would not establish profitable demand.
