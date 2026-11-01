"""Cost extension of the agreed volume bridge. USD millions except explicit units.
Run from any directory. Inputs marked assumed are scenarios, not management forecasts.
"""
import json
from pathlib import Path
P=Path(__file__).resolve().parent
V=json.loads((P.parent/'volume/capacity/volume-bridge-2026-11-01.json').read_text())
F=json.loads((P.parent/'volume/capacity/adesa-future-pipeline-2026-11-01.json').read_text())
BASE=V['anchor']['annualized_sales_proxy']
SOURCES={'accounting_and_anchor':'https://www.sec.gov/Archives/edgar/data/1690820/000169082026000067/cvna-20260930.htm','project_budgets':'https://investors.carvana.com/~/media/Files/C/Carvana-IR/reports-and-presentations/jp-morgan-auto-conf-aug-2026.pdf'}
A=dict(standard_lead_months=6,major_lead_months=12,incremental_nonlabor_COGS_per_unit=0.0,
       wage_per_paid_hour=35,benefit_payroll_burden=.30,paid_direct_hours_per_vehicle=8,
       annual_paid_hours_per_FTE=2000,wage_inflation=.03,
       extra_labor_during_ramp_fraction=.50,preopening_months=2,preopening_staff_fraction=.25,
       fixed_sga_inflation=.03,variable_sga_inflation=0.0,
       nonproject_capex_anchor_m=160,nonproject_capex_volume_share=.50,nonproject_capex_inflation=.03,
       incremental_net_working_capital_per_annual_unit=4200)
# All A values assumed, including the $160m nonproject anchor. No source discloses it.
GAAP={'compensation':255,'advertising':152,'occupancy':18,'logistics':68,'other':312}
VARIABLE={'compensation':.80,'advertising':.90,'occupancy':.40,'logistics':.90,'other':.60}
# SBC allocation is disclosed. D&A allocation among these three categories is not;
# distribute the disclosed $39m total proportionally as a transparent placeholder.
ADJ={k:float(v) for k,v in GAAP.items()};ADJ['compensation']-=24
for k in ['occupancy','logistics','other']:ADJ[k]-=39*GAAP[k]/398
assert abs(sum(ADJ.values())-742)<1e-9
projects=[]
for s in F['scenarios']['base']['slots']:
 projects.append(dict(id=s['id'],kind='standard',start=s['start_month_index'],capacity=13000,ramp=9,lead=A['standard_lead_months'],low=2,mid=2.5,high=3))
for s in V['project_register']:
 projects.append(dict(id=s['id'],kind='major',start=s['production_start_month'],capacity=40000,ramp=18,lead=A['major_lead_months'],low=30,mid=32.5,high=35))
def overlap(a,b,c,d):return max(0,min(b,d)-max(a,c))
def cumulative(age,cap,ramp):
 age=max(0,age);t=min(age,ramp)
 return cap/12*(t*t/(2*ramp)+max(0,age-ramp))
def output(p,yr,ramp_only=False):
 a=max(yr*12,p['start']);b=min((yr+1)*12,p['start']+p['ramp']) if ramp_only else (yr+1)*12
 if b<=a:return 0
 return cumulative(b-p['start'],p['capacity'],p['ramp'])-cumulative(a-p['start'],p['capacity'],p['ramp'])
for p in projects:
 p['cash_by_year_m']={str(y):{b:p[b]*overlap(y*12,(y+1)*12,p['start']-p['lead'],p['start'])/p['lead'] for b in ['low','mid','high']} for y in range(2025,2037)}
 for b in ['low','mid','high']:assert abs(sum(v[b] for v in p['cash_by_year_m'].values())-p[b])<1e-7

def model(a=A,variable=VARIABLE):
 rows=[];prev=BASE
 for r in V['annual']:
  y=r['year'];t=y-2026;u=r['sales_if_absorbed'];scale=u/BASE
  sga={k:4*ADJ[k]*(variable[k]*scale*(1+a['variable_sga_inflation'])**t+(1-variable[k])*(1+a['fixed_sga_inflation'])**t) for k in ADJ}
  hourly=a['wage_per_paid_hour']*(1+a['benefit_payroll_burden']);normal=u*a['paid_direct_hours_per_vehicle'];ramp_units=sum(output(p,y,True) for p in projects)
  extra=ramp_units*a['paid_direct_hours_per_vehicle']*a['extra_labor_during_ramp_fraction']
  pre=sum(p['capacity']/12*a['paid_direct_hours_per_vehicle']*a['preopening_staff_fraction']*overlap(y*12,(y+1)*12,p['start']-a['preopening_months'],p['start']) for p in projects)
  premium=(normal*hourly*((1+a['wage_inflation'])**t-1)+(extra+pre)*hourly*(1+a['wage_inflation'])**t)/1e6
  gp=1542*4*scale-premium-u*a['incremental_nonlabor_COGS_per_unit']/1e6;ebitda=gp-sum(sga.values())
  cash={k:sum(p['cash_by_year_m'][str(y)]['mid'] for p in projects if p['kind']==k) for k in ['standard','major']}
  nonproject=a['nonproject_capex_anchor_m']*((1-a['nonproject_capex_volume_share'])+a['nonproject_capex_volume_share']*scale)*(1+a['nonproject_capex_inflation'])**t
  capex=sum(cash.values())+nonproject
  prior_sga=742*4*(.7*scale+.3*1.03**t)
  rows.append(dict(year=y,retail_units=u,adjusted_sga_by_category_m=sga,adjusted_sga_m=sum(sga.values()),adjusted_sga_per_unit=sum(sga.values())*1e6/u,
   normal_direct_labor_memo_m=normal*hourly*(1+a['wage_inflation'])**t/1e6,normal_direct_FTE_equivalents=normal/a['annual_paid_hours_per_FTE'],extra_ramp_and_preopening_FTE_equivalents=(extra+pre)/a['annual_paid_hours_per_FTE'],
   ramp_units=ramp_units,incremental_labor_cost_vs_flat_GPU_m=premium,adjusted_gross_profit_m=gp,adjusted_ebitda_m=ebitda,ebitda_change_vs_preliminary_m=prior_sga-sum(sga.values())-premium-u*a['incremental_nonlabor_COGS_per_unit']/1e6,
   standard_project_capex_m=cash['standard'],major_project_capex_m=cash['major'],nonproject_capex_m=nonproject,total_capex_m=capex,
   project_capex_low_m=sum(p['cash_by_year_m'][str(y)]['low'] for p in projects),project_capex_high_m=sum(p['cash_by_year_m'][str(y)]['high'] for p in projects),
   incremental_net_working_capital_m=(u-prev)*a['incremental_net_working_capital_per_annual_unit']/1e6))
  prev=u
 return rows
rows=model()
sens={}
for name,changes in {'no_labor_inflation_or_ramp_penalty':dict(wage_inflation=0,extra_labor_during_ramp_fraction=0,preopening_staff_fraction=0),'labor_hours_6':dict(paid_direct_hours_per_vehicle=6),'labor_hours_12':dict(paid_direct_hours_per_vehicle=12),'nonproject_capex_100m':dict(nonproject_capex_anchor_m=100),'nonproject_capex_250m':dict(nonproject_capex_anchor_m=250),'variable_sga_inflation_3pct':dict(variable_sga_inflation=.03),'extra_nonlabor_COGS_100_per_unit':dict(incremental_nonlabor_COGS_per_unit=100)}.items():sens[name]=model({**A,**changes})
sens['no_fixed_sga_leverage']=model(variable={k:1.0 for k in VARIABLE})
assert len(rows)==9 and all(abs(a['retail_units']-b['sales_if_absorbed'])<1e-6 for a,b in zip(rows,V['annual']))
assert sum(p['mid'] for p in projects)==965
assert all(abs(r['adjusted_ebitda_m']-(r['adjusted_gross_profit_m']-r['adjusted_sga_m']))<1e-8 for r in rows)
assert all(r['incremental_labor_cost_vs_flat_GPU_m']==0 for r in sens['no_labor_inflation_or_ramp_penalty'])
out=dict(status='Working cost scenario; not a validated forecast or revised valuation',sources=SOURCES,assumed_inputs=A,assumed_variable_sga_shares=VARIABLE,quarter_GAAP_sga_m=GAAP,quarter_adjusted_sga_allocated_m=ADJ,
 allocation_note='24m SBC removed from compensation; 39m D&A allocated proportionally across occupancy, logistics, other, an assumption. Category forecast is calibrated to 742m total.',
 labor_note='Normal direct labor is a memorandum component already embedded in baseline GPU, never subtracted again. Only inflation and incremental ramp/preopening premium are subtracted. Hours, pay and ramp penalties are unverified; FTE equivalents are not actual technician counts or gross hires. Existing baseline ramp penalty is not identified, so incremental penalties are conservative overlays, not a clean historical normalization.',
 capex_note='Linear spending before production; 2026 allocations are modeled, not actual spend. Nominal budgets held flat. Nonproject capex excludes modeled project construction, but public aggregate capex does not validate that separation. No post-2035 projects are scheduled; 2035 spending drops mechanically and is not terminal normalized capex.',
 working_capital_note='Retains preliminary $4200 net working capital per incremental annual unit; separate from capex, unvalidated. Vehicle inventory, receivables, payable offsets and financing need separate calibration.',
 annual=rows,projects=projects,sensitivities=sens)
(P/'cost-layer-2026-11-01.json').write_text(json.dumps(out,indent=2)+'\n')
print('year units sga_m labor_premium_m standard_capex major_capex other_capex total_capex EBITDA_m')
for r in rows:print(r['year'],round(r['retail_units']),*[round(r[k],1) for k in ['adjusted_sga_m','incremental_labor_cost_vs_flat_GPU_m','standard_project_capex_m','major_project_capex_m','nonproject_capex_m','total_capex_m','adjusted_ebitda_m']])
print('All project budgets:',sum(p['mid'] for p in projects),'Allocated through2026:',sum(p['cash_by_year_m'][str(y)]['mid'] for p in projects for y in [2025,2026]))
print('2030 sensitivities:',{k:{x:round(v[3][x],1) for x in ['adjusted_ebitda_m','total_capex_m']} for k,v in sens.items()})
