"""User-provided Bloomberg screenshots vs existing model; explicit business split.
USD millions unless per-unit or units. Screenshot values are transcribed, not refreshed.
"""
import json
from pathlib import Path
P=Path(__file__).resolve().parent
C=json.loads((P/'cost-layer-2026-11-01.json').read_text())
# Columns verified against dated company-specific screenshots. Contributor counts vary.
data=[
[2025,596641,297643,24365,10519,7026,3315,806,2905,3433,2237,20322,147],
[2026,820413.17,406461.02,27308.24,10533.03,6827.70,3370.77,732.56,2722.43,3206.12,2945.77,29586.57,218.389],
[2027,1040187.07,504779.87,27681.37,10327.21,6786.32,3405.05,705.81,2687.01,2927.40,3884.67,37393.04,260.389],
[2028,1228259.82,599196.02,28196.29,10524.91,6849.87,3506,703.73,2708.94,2902.76,4825.60,45267.94,279.533],
[2029,1461649.78,689835.33,27016.12,10451.29,6933.49,3508.30,653.35,2855.10,2987.82,5791.75,52487.75,350.375]]
keys=['year','retail_units','owned_wholesale_units','retail_ASP','wholesale_ASP','GAAP_total_GPU','retail_GPU','wholesale_GP_per_retail_unit','other_GP_per_retail_unit','adjusted_SGA_per_retail_unit','adjusted_EBITDA_m','revenue_m','capex_outflow_m']
cons=[dict(zip(keys,r)) for r in data]
anchor=dict(retail_units=217385,owned_wholesale_units=111119,retail_revenue_m=6144,wholesale_total_revenue_m=1302,other_revenue_m=594,retail_GP_m=773,wholesale_total_GP_m=154,other_GP_m=594,wholesale_ASP=9854,wholesale_GP_per_owned_unit=963,total_nonGAAP_GP_adjustment_m=21)
anchor['wholesale_owned_revenue_m']=111119*9854/1e6
anchor['marketplace_revenue_residual_m']=1302-anchor['wholesale_owned_revenue_m']
anchor['wholesale_owned_GP_m']=111119*963/1e6
anchor['marketplace_GP_residual_m']=154-anchor['wholesale_owned_GP_m']
rows=[];comparison=[]
for r in C['annual']:
 y=r['year'];u=r['retail_units'];factor=u/anchor['retail_units'];w=u*anchor['owned_wholesale_units']/anchor['retail_units']
 parts={
 'retail_used':dict(units=u,revenue_m=factor*6144,GAAP_GP_before_incremental_cost_m=factor*773),
 'owned_wholesale':dict(units=w,revenue_m=w*9854/1e6,GAAP_GP_before_incremental_cost_m=w*963/1e6),
 'wholesale_marketplace':dict(units=None,revenue_m=factor*anchor['marketplace_revenue_residual_m'],GAAP_GP_before_incremental_cost_m=factor*anchor['marketplace_GP_residual_m']),
 'other_financing_and_ancillary':dict(units=None,revenue_m=factor*594,GAAP_GP_before_incremental_cost_m=factor*594)}
 gp=sum(p['GAAP_GP_before_incremental_cost_m'] for p in parts.values());rev=sum(p['revenue_m'] for p in parts.values())
 reconstructed=gp+factor*21-r['incremental_labor_cost_vs_flat_GPU_m']-u*C['assumed_inputs']['incremental_nonlabor_COGS_per_unit']/1e6
 assert abs(reconstructed-r['adjusted_gross_profit_m'])<1e-7
 assert abs(rev-factor*8040)<1e-7
 row=dict(year=y,businesses=parts,retail_plus_owned_wholesale_units=u+w,revenue_m=rev,GAAP_GP_before_incremental_cost_m=gp,nonGAAP_adjustment_m=factor*21,incremental_labor_cost_m=r['incremental_labor_cost_vs_flat_GPU_m'],adjusted_EBITDA_m=r['adjusted_ebitda_m'])
 rows.append(row)
 if y<=2029:
  b=next(z for z in cons if z['year']==y)
  metrics={'retail_units':u,'owned_wholesale_units':w,'revenue_m':rev,'adjusted_EBITDA_m':r['adjusted_ebitda_m'],'capex_outflow_m':r['total_capex_m'],'adjusted_SGA_per_retail_unit':r['adjusted_sga_per_unit']}
  comparison.append(dict(year=y,metrics={k:dict(ours=v,consensus=b[k],difference=v-b[k],difference_pct=100*(v/b[k]-1)) for k,v in metrics.items()},
   consensus_wholesale_to_retail_ratio=b['owned_wholesale_units']/b['retail_units'],
   owned_wholesale_at_consensus_ratio=u*b['owned_wholesale_units']/b['retail_units'],
   marketplace_flat_vs_proportional_GP_change_m=4*anchor['marketplace_GP_residual_m']-parts['wholesale_marketplace']['GAAP_GP_before_incremental_cost_m']))
output=dict(as_of='2026-11-01 supplied screenshots; capture time visible in filenames, underlying consensus update time unknown',
 source_images=['Screenshot 2026-11-01 124654.png','Screenshot 2026-11-01 124709.png','image (1).png','image-2 (1).png','image-2.png'],
 primary_source='https://www.sec.gov/Archives/edgar/data/1690820/000169082026000067/cvna-20260930.htm',
 consensus=cons,anchor_Q3_2026=anchor,annual=rows,comparison=comparison,
 limitations=[
 '2025 is actual; 2026 onward estimates. No FY2026 model comparison: existing anchor is Q3 annualized, not FY2026.',
 'Owned wholesale forecast holds Q3 wholesale/retail ratio constant. This is a newly explicit placeholder, not an independent procurement or trade-in forecast.',
 'Marketplace growth remains proportional to retail solely to reproduce prior aggregate model. Auction transaction volumes and fee forecasts remain unknown.',
 'Wholesale revenue/GP split uses reported rounded per-owned-wholesale-unit metrics and residuals; approximate, not exact separately reported quarterly balances.',
 'Wholesale GPU displayed in Bloomberg company-specific section is per RETAIL unit and includes marketplace. Never multiply it by wholesale units.',
 'Category split reconciles to prior model; no wholesale contribution or extra recon labor is added on top. Prior labor assumption is per retail unit, not per total transactions.',
 'Non-GAAP gross profit adjustment is kept unallocated; compare GAAP with GAAP, adjusted with adjusted.',
 'Bloomberg contributor populations differ by metric. Component sums and products of independently averaged inputs need not reproduce headline consensus.',
 'Business-breakdown screenshot has material anomalies: 2025 used margin 43.40 vs 1978/14537=13.61%; 2028 used cost 41349.69m exceeds revenue34307.98m while GP4264m is positive. Do not import those cost or margin rows without checking mappings.',
 'No retail growth uplift beyond agreed capacity scenario is introduced to match consensus. Source images are not committed.' ])
(P/'consensus-comparison-2026-11-01.json').write_text(json.dumps(output,indent=2)+'\n')
for c in comparison:
 print(c['year'],{k:round(v['difference_pct'],2) for k,v in c['metrics'].items()})
