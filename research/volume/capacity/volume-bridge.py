"""Crude volume-only bridge. Explicit assumptions; not observed production."""
import json
from pathlib import Path
P=Path(__file__).resolve().parent
hours=json.loads((P/'labor-recovery-calculations-2026-11-01.json').read_text())['sites']
allobs=json.loads((P/'staffing-panel-data.json').read_text())['all_name_matches']
cohort=json.loads((P/'adesa-cohort-build-2026-11-01.json').read_text())
future=json.loads((P/'adesa-future-pipeline-2026-11-01.json').read_text())
extra_ids={'1498104':'Carvana Tooele','1498105':'Carvana Trenton','1498108':'Carvana University Park','1498112':'Carvana West Memphis'}
original=[]
for r in hours:original.append(dict(site=r['site'],hours_2025=r['annual_hours']['2025'],gap_hours=r['additional_hours'],bin='original_recovery' if r['additional_hours'] else 'original_other',history='matched 2022–2025'))
for r in allobs:
 if r['source_year']==2025 and r['establishment_id'] in extra_ids:
  original.append(dict(site=extra_ids[r['establishment_id']],hours_2025=int(r['total_hours_worked']),gap_hours=0,bin='original_other',history='2025 only; no inferred zero historical gap'))
assert len(original)==18

def cumul(age,cap=13000,ramp=9):
 age=max(0,age);t=min(age,ramp);return cap/12*(t*t/(2*ramp)+max(0,age-ramp))
def q3_adesa():
 from datetime import date
 from calendar import monthrange
 total=0
 for r in cohort['rows']:
  d=date.fromisoformat(r['start_proxy']);s=d.year*12+d.month-1+(d.day-1)/monthrange(d.year,d.month)[1]
  total+=cumul(2026*12+9-s)-cumul(2026*12+6-s)
 return total

# Forecast project slots, not claimed named properties. All incremental capacities.
projects=[]
for yr in [2027]+list(range(2030,2036)):
 for n,mo in enumerate([3,6,9]):
  projects.append(dict(id=f'buildout-{yr}-{n+1}',production_start_month=yr*12+mo,year=yr,capacity_increment=40000,ramp_months=18,budget_low=30000000,budget_high=35000000,status='company-reported 2027 cohort; within-year starts assumed' if yr==2027 else 'assumed future project',site=None,spend_already_incurred=None,remaining_spend=None,construction_spend_schedule=None))

anchor_sales=217385;annualized=anchor_sales*4
ad_q=q3_adesa()*4
orig_anchor=annualized-ad_q
assert orig_anchor>0

def calculate(gap_closed=.5,other_growth=.05,production_vs_sales=1.0):
 anchor=annualized*production_vs_sales-ad_q
 weights=[r['hours_2025']+gap_closed*r['gap_hours'] for r in original]
 base=[anchor*w/sum(weights) for w in weights]
 rows=[]
 for yr in range(2027,2036):
  bins={'original_recovery':0.,'original_other':0.}
  for i,r in enumerate(original):
   if r['bin']=='original_recovery':
    # Average-year recovery milestone, not year-end rate.
    f=gap_closed+(1-gap_closed)*min(1,(yr-2026)/2)
    v=base[i]*(r['hours_2025']+f*r['gap_hours'])/weights[i]
    v*= (1+other_growth)**max(0,min(yr,2030)-2028)
   else:v=base[i]*(1+other_growth)**(min(yr,2030)-2026)
   bins[r['bin']]+=v
  if sum(bins.values())>1000000:
   factor=1000000/sum(bins.values());bins={k:v*factor for k,v in bins.items()}
  existing={b:cohort['summaries'][b]['annual_production'].get(str(yr),cohort['summaries'][b]['capacity']) for b in ['mature_ADESA','ramping_ADESA']}
  fut=next((x['future_pool_production'] for x in future['scenarios']['base']['annual'] if x['year']==yr),455000)
  builds=sum(cumul(12*(yr+1)-p['production_start_month'],40000,18)-cumul(12*yr-p['production_start_month'],40000,18) for p in projects)
  builds=min(builds,2000000-56*13000)
  total=sum(bins.values())+sum(existing.values())+fut+builds
  rows.append(dict(year=yr,**bins,**existing,future_ADESA=fut,major_buildouts=builds,total_production=total,sales_if_absorbed=total,sales_at_95pct_absorption=total*.95,unsold_addition_at_95pct=total*.05))
 return rows,base
rows,base=calculate()
for r,b in zip(original,base):r['allocated_q3_annualized_production_proxy']=b
sens={}
for k,args in {'all_historical_recovery_already_done':dict(gap_closed=1),'none_historical_recovery_done':dict(gap_closed=0),'no_growth_beyond_recovery':dict(other_growth=0),'production_5pct_above_sales_anchor':dict(production_vs_sales=1.05)}.items():sens[k]=calculate(**args)[0]
assert abs(sum(base)+ad_q-annualized)<1e-6
assert sum(r['gap_hours'] for r in original)==2127888
assert len(projects)==21
assert len({p['id'] for p in projects})==len(projects)
assert all(abs(r['total_production']-sum(r[k] for k in ['original_recovery','original_other','mature_ADESA','ramping_ADESA','future_ADESA','major_buildouts']))<1e-6 for r in rows)
assert all(r['total_production']<=3000000 for r in rows)
out=dict(anchor=dict(period='Q3 2026 annualized, not FY2026 estimate',quarter_retail_sales=anchor_sales,annualized_sales_proxy=annualized,modeled_ADESA_quarter_annualized=ad_q,residual_original_production_proxy=orig_anchor,production_equals_sales_assumption=True),assumptions=dict(historical_gap_closed_by_anchor=.5,remaining_gap_closed_by_annual_average_2028=True,annual_hours_growth_beyond_recovery=.05,growth_beyond_recovery_end_year=2030,original_planning_limit=1000000,all_ADESA_planning_limit=2000000,full_buildout_ramp_months=18,new_full_buildouts_2030_onward_per_year=3,base_sales_absorption=1),original_sites=original,annual=rows,project_register=projects,sensitivities=sens)
out['provenance']={
 'quarter_retail_sales':{'classification':'company-reported','source':'https://investors.carvana.com/~/media/Files/C/Carvana-IR/documents/cvna-shareholder-letter-q3-2026.pdf'},
 'original_site_hours':{'classification':'reported OSHA establishment hours; reconstructed site matching','source':'staffing-panel-data.json; labor-recovery-calculations-2026-11-01.json'},
 'original_production_allocation':{'classification':'assumed residual allocation, not observed site output','method':'Q3 sales annualized less modeled Q3 ADESA output; distribute by adjusted 2025 hours'},
 'original_growth':{'classification':'assumed','note':'50% historical gap closure at anchor and 5% subsequent annual growth are scenario choices, not independently measured'},
 'ADESA_capacity_and_budgets':{'classification':'company-reported illustrative project increments','source':'https://investors.carvana.com/~/media/Files/C/Carvana-IR/reports-and-presentations/jp-morgan-auto-conf-aug-2026.pdf','page':'slide 6'},
 'ramp_timing':{'classification':'analog-informed assumption; linear shape assumed','source':'adesa-peer-ramp-evidence-2026-11-01.md'},
 'future_standard_starts':{'classification':'assumed extrapolation','source':'adesa-future-pipeline-2026-11-01.json'},
 'major_project_placement':{'classification':'assumed','note':'Unique eligible properties; each 40,000 increment is additional to standard integration capacity. Site identities and compatibility with standard rollout remain unverified.'},
 'sales_absorption':{'classification':'assumed','note':'Production is not sales. Persistent 95% absorption would accumulate inventory and require production cuts; stress columns are arithmetic, not a sustainable operating plan.'}
}
(P/'volume-bridge-2026-11-01.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out['anchor'],indent=2))
for r in rows:print(r['year'],*[round(r[k]) for k in ['original_recovery','original_other','mature_ADESA','ramping_ADESA','future_ADESA','major_buildouts','total_production']])
print('SENS',[(k,round(v[0]['total_production']),round(v[3]['total_production'])) for k,v in sens.items()])
print('HOURS',sum(r['hours_2025'] for r in original))
