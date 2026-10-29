# Carvana profitable volume growth framework

Updated 2026-10-29. Agreed research framework; causal attribution and investment conclusions remain open. First focused study: [ADESA local market research plan](adesa-research-plan.md).

## Decision and scope

Determine how much Carvana retail volume can grow sustainably, what causes that growth, and what incremental cash returns it generates. Combine the eventual operating conclusions with normalized loan-sale economics and valuation before drawing a long or short conclusion. Strong sales growth alone does not establish attractive investment returns.

Start with a consistent identity:

**Carvana retail units = addressable used vehicle retail transactions × Carvana market share.**

Keep dealer transactions distinct from all transactions including private-party sales. Reconcile any new-vehicle contribution to Carvana's reported units before comparing with a used-only denominator. Keep owned and marketplace vehicles distinct where disclosed.

Online research, digital financing and online checkout overlap with physical dealership transactions. Treat digital adoption as a possible driver of share shifts; do not assume a consistently measurable, separate e-commerce market or double-count channel adoption and company share gains.

## Three linked questions

| Question | Evidence | Forecast use |
|---|---|---|
| What is happening to market demand? | Used transactions, affordability, credit availability, replacement demand, consistent channel surveys | Establish market baseline |
| Why does Carvana gain or lose share? | Relative selection, delivered price and financing, delivery speed, qualified traffic, trust, operational execution | Explain company outperformance |
| Is the additional volume profitable? | Incremental contribution, advertising, logistics, inventory funding and markdowns, capex and utilization | Estimate incremental cash returns |

CarMax is a comparator, not the entire market or an unaffected control. Match calendar periods and customer/vehicle mix; account for its own pricing and execution changes. Add industry data and other dealers where they distinguish explanations.

## Mechanisms to test

| Mechanism | Observable implication | Disconfirming observation |
|---|---|---|
| Broader relevant selection | More appropriate vehicles by budget/type/location precede stronger sales | Listings grow but sales do not; aging increases |
| Better delivered price or payment | Relative prices, shipping or financing improve and affected segments gain share | Sales require persistent concessions that erase returns |
| Faster fulfilment | Delivery improves before relative local sales improve | Delivery improves without share gains |
| Awareness and trust | Qualified traffic, referrals or repeat sales strengthen | More spending produces little incremental contribution |
| Better operating execution | Reconditioning throughput, ready inventory and reliability improve | Nominal capacity rises but usable output does not |

These mechanisms interact. Do not multiply inventory growth, conversion growth and capacity growth as independent drivers. Sales per average monthly visitor is a purchase-yield proxy, not a measured customer-cohort conversion rate. Marketing changes visitor quality; financing can affect both volume and profit per transaction.

## Evidence and model rules

- Label inputs observed, derived, proxy, assumed or unknown, with source passage, date, population and denominator.
- Separate announcement, production start, ramp and full buildout. Separate inventory stock, throughput flow and theoretical capacity.
- Distinguish predictive backtests from causal tests. Use only information available at each forecast date; hold out later quarters and compare against simple seasonal/share benchmarks.
- Reconcile traffic methodology changes, inventory definitions, new/used mix, marketplace treatment, fiscal calendars and reported/restated figures before fitting.
- Track inventory age, markdowns and cash tied up alongside volume. Website listing coverage is not actual days to sale or owned inventory turnover.
- Do not infer a regional effect from national correlations or attribute all peer-relative growth to ADESA.
- Model loan-sale economics and volume jointly in downside scenarios: a weaker financing advantage may require lower profit, higher customer payments or additional marketing.

## Deliverables and next step

1. Matched quarterly market and company baseline through Q3 2026, with reproducible definitions and a source ledger.
2. Evidence-ranked explanation of share gains, including competing hypotheses and unresolved data gaps.
3. Incremental economics and volume scenarios with capital requirements, rather than an unconditional continuation of recent growth.

Begin with the ADESA data-feasibility study below. Do not buy data, start bulk scraping or fit an extensive model before establishing that observations can answer the question.

First execution update: [ADESA pilot feasibility findings](adesa-pilot-feasibility-2026-10-29.md) and [initial event register](adesa-event-register.json). Live buyer-ZIP availability fields were observed; historical access and reconditioning-site attribution remain unresolved.

## Existing evidence

- [Sell-side extraction and cautions](../sellside/2026-10-28-extraction.md).
- Local working inputs: `work/cvna2025.txt` and `work/earnings-calls/`. These are not tracked in Git; do not assume a fresh checkout contains them.
- [2025 annual report](https://investors.carvana.com/~/media/Files/C/Carvana-IR/documents/cvna-2025-annual-report.pdf).
- [Q3 2026 shareholder letter](https://investors.carvana.com/~/media/Files/C/Carvana-IR/documents/cvna-shareholder-letter-q3-2026.pdf) and [release](https://press.carvana.com/carvana-announces-record-third-quarter-2026-results/).

The discussion through 2026-10-29 supports testing selection, delivery, financing and marketing jointly. It does not establish their individual causal contributions. Detailed Q3 call Q&A remains to be incorporated.
