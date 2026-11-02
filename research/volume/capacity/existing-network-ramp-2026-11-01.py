import json
from pathlib import Path
P=Path(__file__).resolve().parent
v=json.loads((P/'volume-bridge-2026-11-01.json').read_text())
c=json.loads((P.parent.parent/'valuation/consensus-comparison-2026-11-01.json').read_text())
cost=json.loads((P.parent.parent/'valuation/cost-layer-2026-11-01.json').read_text())
a=v['anchor']['residual_original_production_proxy']; t0=2026+7.5/12
h=sum(s['hours_2025']+.5*s['gap_hours'] for s in v['original_sites'])
cons={r['year']:r for r in c['consensus']}
nonorig=['mature_ADESA','ramping_ADESA','future_ADESA','major_buildouts']
cases={'slow_5pct':(.05,0,1000000),'working_10pct':(.10,0,1000000),'fast_15pct':(.15,0,1000000),'10pct_hours_2pct_productivity':(.10,.02,1000000),'10pct_hours_900k_effective_cap':(.10,0,900000)}
out={'status':'Scenario extension, not a validated base forecast. Original bridge preserved.','anchor_original_units':a,'anchor_time':t0,'anchor_hours_proxy':h,'timing':'Q3 midpoint anchor; calendar years are means of 12 monthly midpoint annual output rates.','scenarios':{}}
for name,(g,p,cap) in cases.items():
 rows=[]
 for old in v['annual']:
  y=old['year']; values=[]; hourvalues=[]
  for m in range(12):
   t=y+(m+.5)/12-t0
   q=min(cap,a*((1+g)*(1+p))**t)
   values.append(q);hourvalues.append(h*q/a/(1+p)**t)
  orig=sum(values)/12; hours=sum(hourvalues)/12
  total=orig+sum(old[k] for k in nonorig); delta=total-old['sales_if_absorbed']
  old_orig=old['original_recovery']+old['original_other']
  # Marginal cost illustrations retain previous unvalidated cost assumptions.
  sga=delta/v['anchor']['annualized_sales_proxy']*4*sum(cost['quarter_adjusted_sga_allocated_m'][k]*cost['assumed_variable_sga_shares'][k] for k in cost['assumed_variable_sga_shares'])
  r={'year':y,'original_output':orig,'original_establishment_hours_proxy':hours,'original_FTE_equivalent_proxy':hours/2000,'retail_units_if_absorbed':total,'old_retail_units':old['sales_if_absorbed'],'delta_vs_old':delta,**{k:old[k] for k in nonorig},'marginal_adjusted_SGA_m':sga,'incremental_normal_direct_labor_memo_m':delta*8*35*1.3*1.03**(y-2026)/1e6,'incremental_nonproject_capex_m':80*delta/v['anchor']['annualized_sales_proxy']*1.03**(y-2026),'incremental_net_WC_balance_vs_old_m':delta*4200/1e6}
  if y in cons:
   r.update(consensus_retail_units=cons[y]['retail_units'],vs_consensus_pct=100*(total/cons[y]['retail_units']-1),owned_wholesale_units=cons[y]['owned_wholesale_units'])
  assert abs(total-orig-sum(r[k] for k in nonorig))<1e-6 and orig<=cap+1e-6
  rows.append(r)
 out['scenarios'][name]={'annual_effective_hours_growth_assumed':g,'annual_productivity_growth_assumed':p,'original_capacity_cap':cap,'annual':rows}
out['limitations']=['Effective hours are hours after training/absence/skill constraints, not gross hires or job postings. Hiring must lead output; no observed training lag is fitted.','Original output and hours at Q3 are residual/proxy allocations, not measured site production or contemporaneous hours. OSHA hours include multiple roles; FTE equivalents are not technician counts.','10% is a working sensitivity, not estimated from two tours. 5/15% bracket execution; no rate is calibrated to consensus.','Existing ADESA cohorts remain at earlier 13k standard capacity; further staffing headroom there is unquantified.','Capacity is potential, not guaranteed demand. Growth needs inventory sourcing and profitable sales absorption. No new demand forecast is supplied.','Incremental normal direct labor is already inside unit gross profit: memo only; do not subtract twice. SG&A, capex and WC use previous provisional assumptions; no revised EBITDA or target price is claimed.','Physical line/equipment expansion needs separate capex; staffing-only plan does not fund new line installation.','Marginal SG&A inherits a companywide retail-volume cost driver even though wholesale units are held at consensus; a segment-specific cost split remains necessary.',
'No standalone historical-gap recovery is added: the new original-network path replaces that calculation.','Monthly midpoint averaging is numerical approximation; seasonality is not modeled.','Post-cap productivity case allows fewer hours at constant output; that is an efficiency scenario, not a layoff forecast.']
out['sources']=[{'type':'company primary','url':'https://investors.carvana.com/~/media/Files/C/Carvana-IR/documents/IR_Intro-to-Carvana_Q2_2026.pdf','locator':'slide 16','claim':'18 original IRCs support over 1m units; ADESA adds 2m when expanded.'},{'type':'company primary','url':'https://investors.carvana.com/~/media/Files/C/Carvana-IR/reports-and-presentations/jp-morgan-auto-conf-aug-2026.pdf','locator':'slide 6','claim':'Staffing existing sites separate from integrations/buildouts; logistics and customer care scale too.'},{'type':'licensed secondary, existing local extraction not redistributed','file':'work/sellside-expanded-2026-10-31/20.txt','locator':'DA Davidson 2025-11-16, lines 29-38','claim':'Haines adding fifth line, ramping second shift; printed 12800/week excluded as unreliable.'},{'type':'licensed secondary, existing local extraction not redistributed','file':'work/sellside-expanded-2026-10-31/28.txt','locator':'Citizens 2026-06-04 p2','claim':'Elyria four physical lines, two shifts, reported 1280 completed vehicles/week.'}]
(P/'existing-network-ramp-2026-11-01.json').write_text(json.dumps(out,indent=2)+'\n')
for y in [2027,2028,2029,2030,2031,2035]:
 print(y,[(n,round(next(r for r in x['annual'] if r['year']==y)['retail_units_if_absorbed'])) for n,x in out['scenarios'].items()])
print('CENTRAL',json.dumps(out['scenarios']['working_10pct']['annual'][:4],indent=2))
