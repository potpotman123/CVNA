"""Finite 35-property integration pool; anonymous future slots, no invented site order."""
import json
from pathlib import Path
from datetime import date
from calendar import monthrange
P=Path(__file__).resolve().parent
geo=json.loads((P/'geography/comparison.json').read_text())['rows']
pool=[r for r in geo if r['group']=='Other ADESA' and not r['excluded']]
assert len(pool)==35
assert sum(r['name']=='ADESA Orlando' for r in pool)==1
CAP=13000;RAMP=9
orlando=2026*12+9+5/31 # Oct 6 announcement proxy

def cumul(age):
    age=max(0,age);t=min(age,RAMP)
    return CAP/12*(t*t/(2*RAMP)+max(0,age-RAMP))
def units(s,y):return cumul(12*(y+1)-s)-cumul(12*y-s)
existing=json.loads((P/'adesa-cohort-build-2026-11-01.json').read_text())['summaries']['all']['annual_production']
scenarios={}
for name,pace in [('slow',6),('base',7),('fast',8)]:
    slots=[dict(id='ADESA Orlando',start_month_index=orlando,year=2026,timing='2026-10-06 announcement proxy')]
    left=34;y=2027
    while left:
        n=min(left,pace)
        for j in range(n):
            # Maintain normal year's cadence even in final partial year.
            s=12*y+(j+.5)*12/pace
            slots.append(dict(id=f'Unassigned future slot {len(slots)}',start_month_index=s,year=y,timing='assumed evenly spaced; not a named site forecast'))
        left-=n;y+=1
    annual=[]
    for yr in range(2026,2035):
        output=sum(units(s['start_month_index'],yr) for s in slots)
        prior=sum(units(s['start_month_index'],yr-1) for s in slots)
        old=existing[str(yr)] if str(yr) in existing else 273000
        annual.append(dict(year=yr,new_integrations=sum(s['year']==yr for s in slots),future_pool_production=output,growth_vs_prior_year=output-prior,existing_21_production=old,all_56_standard_production=old+output,integration_capex_low=sum(s['year']==yr for s in slots)*2e6,integration_capex_high=sum(s['year']==yr for s in slots)*3e6))
    assert len(slots)==35
    assert abs(annual[-1]['future_pool_production']-455000)<1e-4
    assert abs(annual[-1]['all_56_standard_production']-728000)<1e-4
    scenarios[name]=dict(annual_pace=pace,slots=slots,annual=annual)
out=dict(as_of='2026-11-01',baseline='Q3 2026 21 candidate integrations',assumptions=dict(standard_capacity=13000,ramp_months=9,endpoint=1,all_35_suitable=True,orlando_announcement_proxy='2026-10-06',no_other_unannounced_Q4_2026_openings=True),properties=[dict(name=r['name'],address=r['address'],standard_capacity=13000,major_buildout_eligible_assumption=True,status='October announcement proxy' if r['name']=='ADESA Orlando' else 'unassigned future slot; suitability assumed') for r in pool],scenarios=scenarios,ceilings=dict(standard_all_56=728000,standard_remaining_35=455000,remaining_standard_project_budget=[70e6,105e6],mechanical_all_56_plus_40k=56*53000,mechanical_full_buildout_increment=56*40000,mechanical_full_buildout_project_budget=[56*30e6,56*35e6],company_ADESA_approx_reference=2000000,company_network_approx_reference=3000000,ADESA_headroom_over_all_standard_using_company_reference=2000000-728000,unreconciled_excess_of_mechanical_vs_company_ADESA=56*53000-2000000))
(P/'adesa-future-pipeline-2026-11-01.json').write_text(json.dumps(out,indent=2)+'\n')
for r in scenarios['base']['annual']:print(r['year'],r['new_integrations'],round(r['future_pool_production']),round(r['growth_vs_prior_year']),round(r['all_56_standard_production']))
print('SCENARIOS',[(k,round(v['annual'][1]['future_pool_production']),round(v['annual'][2]['future_pool_production'])) for k,v in scenarios.items()])
