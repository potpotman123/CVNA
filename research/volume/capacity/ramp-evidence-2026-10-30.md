# Site ramp and operating bottlenecks — bounded evidence pass

As of 2026-10-30. Supplements the capacity framework; does not establish site utilization or revise the sales forecast. Reviewed existing capacity research and local CarMax calls before expanding discovery. Public equipment-supplier, technical-conference, consulting, workforce and auction-service sources were examined. No paid acquisition, outreach or bulk collection.

## What changed

The operating-constraint hypothesis now has concrete process evidence, including a Carvana paint-line design benchmark and a peer's account of immature reconditioning centers. It remains unproven how much national output is recoverable through staffing versus equipment, vehicle mix or better execution. No validated site-by-site output/headcount panel emerged.

## Evidence register

### R1 — Tolleson: a stage-capacity benchmark, not demonstrated whole-site output

[Rely-On/Garmat project account](https://relyonusa.com/carvana-silicon-valley-meets-collision-repair/), historical project contracted in 2018, accessed October 30. Supplier describes three four-booth paint lines rated at 30 vehicles/day each. Phase one installed eight booths; phase two is described prospectively. Full completion, shift hours, uptime and current configuration are unverified. Commercial supplier testimony is external to earnings commentary but not an independent performance audit.

Conditional paint capacity is 60/day for two lines or 90/day for three. This counts vehicles requiring paint, not all cars passing through the IRC. Do not extrapolate this old design across ADESA sites.

### R2 — Operational detail predates the latest expansion

[Carvana/Accenture presentation at Oracle CloudWorld, September 10, 2024](https://static.rainfocus.com/oracle/ocw24/sess/1715608388306001FX5q/finalsessionfile/THR2045%20-%20Carvana%20Streamlines%20Operations%20with%20Technician%20Productivity%20Application%20on%20OCI_1726002021102001fm7p.pdf), slides 9–10, 16–18, 24, 26. Carvana's inventory-reconditioning director co-presented: company/vendor evidence, not independent validation. Describes variable routing, just-in-time parts, rework and 47 potential work centers. PartsCart reportedly reduces parts search/purchase time 90%; that is not total technician labor or whole-vehicle cycle time. Expert review is concentrated on flagged repair estimates.

Slide 24 lists percentages for cycle time, QC and costs, but extracted text omits graphical directions; screenshot retrieval did not provide inspectable pixels. Those metrics are withheld from calibration. Baseline dates, site population and mix controls are also missing. Eleven thousand application users are not a recon headcount measure. This establishes that process tools existed by 2024, so their entire historical benefit cannot be treated as incremental future upside.

### R3 — External example: quality and paint queues can hide capacity

[TBM Consulting anonymous online-reseller case](https://tbmcg.com/case-study/auto-reseller-revamps-operations-to-propel-growth/), undated, accessed October 30. Reports reconditioning lead time falling from 21 to 5 days and an 80% smaller paint backlog following inspection, quality, scheduling and workflow changes. It says actual throughput was 40% below perceived throughput because of quality rejects. Its starting quality rate is inconsistent: around 40% in the narrative versus 50% in the results. Do not identify the client as Carvana. Consultant marketing and an unidentified population limit generalization. Doubling output and cutting labor costs 25% appear as objectives, not verified results. Use as mechanism evidence only.

### R4 — Outsourcing can add output without adding owned lines

[Manheim / US Auto Sales case](https://press.manheim.com/2017-10-25-Why-would-a-regional-car-dealer-outsource-reconditioning-services-it-already-offers), page displays October 5, 2018 despite its 2017 URL. Dealer reportedly processed 1,200 vehicles/month at its own facility and outsourced approximately 400/month. Thus external processing represented 25% of combined 1,600 monthly units, or 33.3% incremental to internal output. Its 400 employees cover the dealer organization, not the facility. Supplier/customer testimony illustrates a capacity route; it does not establish Carvana's current outsourcing volume or cost.

### R5 — CarMax is a useful operational comparison already in our files

Existing CapIQ transcript `work/earnings-calls/KMX-Q1-FY2027.txt`, lines 410–434: management describes parts/tire-selection tools and digitizing recon. It says seven off-site centers were open but still ramping; logistics savings were apparent while recon economics had not reached desired operating levels. This supports separating geographic benefits from factory maturity. No quantified mature utilization or ramp duration supplied.

`KMX-Q4-FY2026.txt`, line 348: management explicitly says older/higher-mileage cars require more recon cost and time. This corroborates the repair-mix mechanism, without quantifying Carvana's elasticity. Both are peer management testimony, not audits. Original retrieval provenance is in `work/earnings-calls/manifest.json`. Only transcript passages before provider summaries used.

### R6 — ADESA early/late ramp evidence remains incomplete

[Kansas City announcement, August 19, 2024](https://investors.carvana.com/news-releases/2024/08-19-2024-110010001): Belton transition forecast approximately 200 jobs over coming years. [Nashville announcement, May 22, 2025](https://investors.carvana.com/news-releases/2025/05-22-2025-130112195): approximately 100 jobs over time. Neither is an observed staffed level or an output series; functions include inspection, recon and fulfillment. Different job targets cannot establish relative utilization.

Concrete unresolved lead: search indexing of [NY DOL May 2026 Western New York briefing](https://dol.ny.gov/system/files/documents/2026/05/western-new-york.pdf) attributes an Akron ramp and a 50-person hiring campaign to Buffalo Business First. Indexed text says prior business was one-tenth of current business, but the opened PDF text did not contain the passage. Do not count the search excerpt as validated production: document-version mismatch, ambiguous business metric and underlying source remain unresolved. No numerical Buffalo ramp enters the model.

## Reproducible conditional model

For a stage s, let usable stage hours/day be H_s, hours per visit h_s, and expected visits per completed car v_s (including bypass probability and rework). Then stage-supported completed output is H_s / (h_s * v_s). Facility output is bounded by the minimum across stages, plus inbound supply and outbound constraints. Equipment and labor both constrain H_s. Different role counts cannot simply be pooled.

Paint illustration using R1's three-line conditional design: 3 * 30 = 90 paint vehicles/day. Assume other stages do not bind and each affected car needs one visit:

| Assumed share requiring paint | Paint-supported total cars/day |
|---|---:|
| 70% | 90 / 0.70 = 128.6 |
| 50% | 90 / 0.50 = 180.0 |
| 30% | 90 / 0.30 = 300.0 |

Shares are hypothetical, not observed Carvana data. The same equipment can support 40% more total cars when paint incidence falls from 70% to 50%: 180 / (90 / 0.70) - 1 = 40%. Reversing mix reverses this benefit. This is not evidence that Carvana's 40% growth came from mix.

Separately, 20% more productive hours combined with 10% less labor per car yields 1.20 / 0.90 - 1 = 33.3% potential labor-stage output growth. This requires the same stage to remain binding and no offset from quality or repair mix. No such changes are assumed to have occurred at Carvana.

Shorter elapsed cycle time can reduce work-in-process and working capital without increasing output: steady-state WIP = daily completions * elapsed days. Do not equate a percentage cycle-time improvement with the same labor saving or a production increase.

## Decision and next discriminating evidence

These findings support a stage-based sensitivity framework, not a numerical national utilization estimate. The bullish case requires a matched mature/ramping-site comparison: completed units, staffed shifts, equipment, repair mix, quality/rework and cost. Adding workers away from the binding stage may add expense without output.

Existing CarMax calls already supply the closest peer operating comparison, so no new CapIQ retrieval was needed for this pass. A targeted next retrieval would be older CVNA Q2 2024 commentary on lines/shifts and a CarMax operating presentation with actual off-site center economics, if available. Collision repair operators such as Boyd could inform technician, parts and paint constraints, but accident severity and insurance authorization make their cycle times unsuitable as direct Carvana production assumptions.

Stop here on generalized searches: more job advertisements or announced job targets would not fill the output denominator. Resolve the specific Buffalo document lead or seek actual unit/shift metrics before extending the facility panel. Profitable demand remains a separate test; no supply-side benchmark proves customers will absorb extra cars.
