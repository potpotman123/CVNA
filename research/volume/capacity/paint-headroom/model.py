"""Paint headroom: requirements and a constructed plant illustration, NOT a CVNA forecast.
Run: python3 model.py; outputs results.json and requirements.md. Standard library only.
Resource hours and workload are separated. Rework is expected additional hours relative
 to first-pass work, not a failure probability or an assumed geometric repeat loop.
"""
import copy
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def weighted_workload(categories, shares, extra, work_multipliers=None):
    assert math.isclose(sum(shares.values()), 1, abs_tol=1e-9)
    assert all(p >= 0 for p in shares.values())
    resources = list(next(iter(categories.values())))
    multipliers = work_multipliers or {}
    return {r: sum(shares[c] * categories[c][r] for c in categories)
            * (1 + extra.get(r, 0)) * multipliers.get(r, 1) for r in resources}

def capacity(hours, workload):
    rates = {r: hours[r]/w if w > 0 else None for r,w in workload.items()}
    finite = {r:v for r,v in rates.items() if v is not None}
    q = min(finite.values())
    return {'resource_supported_vehicles_per_week':rates,
            'system_upper_bound_per_week':q,
            'binding_resources':[r for r,v in finite.items() if math.isclose(v,q,rel_tol=1e-9)]}

def run(data):
    demo=data['illustration']
    cats=demo['first_pass_resource_hours_per_vehicle_by_category']
    shares=demo['base_category_shares']
    extra=demo['base_extra_rework_hours_fraction']
    work=weighted_workload(cats,shares,extra)
    # Explicitly constructed reference resource budgets; no fit to any observed site.
    hours={r:work[r]*q for r,q in demo['constructed_base_resource_output_bounds'].items()}
    base=capacity(hours,work)
    scenarios=[]
    for s in demo['scenarios']:
        sh=s.get('category_shares',shares)
        ex={**extra,**s.get('extra_rework_hours_fraction',{})}
        wh=weighted_workload(cats,sh,ex,s.get('work_multipliers'))
        hh={r:h*s.get('resource_hours_multipliers',{}).get(r,1) for r,h in hours.items()}
        out=capacity(hh,wh)
        out.update({'id':s['id'],'description':s['description'],
                    'classification':'ASSUMED CONSTRUCTED EXAMPLE - NOT CARVANA ESTIMATE',
                    'workload_hours_per_vehicle':wh,'available_resource_hours':hh,
                    'change_vs_reference':out['system_upper_bound_per_week']/base['system_upper_bound_per_week']-1,
                    'added_paid_labor_cost_per_week_at_assumed_rate':sum(
                        max(0,hh[r]-hours[r])/demo['productive_share_of_paid_incremental_hours']
                        *demo['loaded_wages_per_paid_hour'][r] for r in demo['loaded_wages_per_paid_hour']),
                    'excluded_costs':s['excluded_costs'],'timing':s['timing'],'falsification':s['falsification']})
        # Costs are resource purchases, even if bottleneck migration prevents their full use.
        dq=out['system_upper_bound_per_week']-base['system_upper_bound_per_week']
        out['added_labor_cost_per_extra_supported_vehicle']=out['added_paid_labor_cost_per_week_at_assumed_rate']/dq if dq>0 else None
        scenarios.append(out)
    req=[]
    for g in data['target_growth_rates']:
        req.append({'growth':g,'resource_hours_multiplier_if_workload_constant':1+g,
                    'required_workload_reduction_if_hours_constant':1-1/(1+g),
                    'max_current_availability_if_target_is_assumed_85pct':0.85/(1+g),
                    'minimum_current_rework_share_of_total_hours_if_eliminating_all_rework':g/(1+g),
                    'maximum_paint_incidence_from_assumed_50pct_equal_job_workload':0.5/(1+g),
                    'elyria_reference_total_output_per_week':1280*(1+g)})
    rework=[{'current_extra_rework_hours_over_first_pass':a,'future_extra_rework_hours_over_first_pass':b,
             'stage_capacity_gain':(1+a)/(1+b)-1} for a,b in [(0.1,0),(0.1,0.05),(0.25,0.1),(0.4,0.1)]]
    cure=[{'curing_share_of_total_occupancy':c,'curing_duration_reduction_assumed':.75,
           'stage_capacity_gain':1/(1-.75*c)-1} for c in [.1,.25,.5]]
    economics=data['economics']
    cost_grid=[{'extra_paid_hours_per_added_vehicle':h,'loaded_wage':w,'labor_cost_per_added_vehicle':h*w,
               'labor_cost_for_100_extra_vehicles_week':100*h*w} for h in [.5,1,2] for w in [30,45,60]]
    # Steady state: operating weeks converted to calendar days for inventory exposure.
    delta_annual=economics['extra_weekly_sales_assumed']*economics['operating_weeks_assumed']
    wc=delta_annual/365*economics['incremental_inventory_days_assumed']*economics['vehicle_carrying_cost_assumed']
    capital=[]
    for c in economics['incremental_contribution_after_all_incremental_operating_costs_assumed']:
        annual=delta_annual*c
        capital.append({'net_incremental_contribution_per_sold_vehicle':c,'annual_incremental_operating_contribution':annual,
                        'inventory_requirement':wc,
                        'max_equipment_and_training_capital_at_assumed_pretax_cash_return_hurdle':annual/economics['cash_return_hurdle_assumed']-wc})
    inventory_release=1280*economics['operating_weeks_assumed']/365*2*economics['vehicle_carrying_cost_assumed']
    return {'classification':'Conditional requirements and constructed examples only. No estimated CVNA headroom.',
            'site_estimates':{s:None for s in ['Tolleson','Elyria','Greenfield','Trenton','Haines City']},
            'target_requirements':req,'reference_workload_hours_per_vehicle':work,'reference_available_hours':hours,
            'reference_capacity':base,'scenarios':scenarios,'rework_sensitivities':rework,'curing_sensitivities':cure,
            'labor_cost_grid':cost_grid,'capital_screen':capital,
            'inventory_release_if_reference_1280_weekly_cars_all_spend_two_fewer_calendar_days':inventory_release,
            'inventory_release_caution':'Assumes 50 operating weeks/year, stable throughput and $22,000 carried cost; cash stock release, not annual profit. Apply affected share for subset queues.'}

def checks(data,result):
    cats=data['illustration']['first_pass_resource_hours_per_vehicle_by_category']
    shares=data['illustration']['base_category_shares']
    w=result['reference_workload_hours_per_vehicle'];h=result['reference_available_hours']
    assert math.isclose(result['reference_capacity']['system_upper_bound_per_week'],400)
    doubled=capacity({r:2*v for r,v in h.items()},w)
    assert math.isclose(doubled['system_upper_bound_per_week'],800)
    # More workers at a nonbinding stage do not improve system throughput.
    hh={**h,'paint_labor':2*h['paint_labor']}
    assert math.isclose(capacity(hh,w)['system_upper_bound_per_week'],400)
    # All workload removed from a resource should not create an infinite JSON value.
    z={**w,'booth_occupancy':0};assert capacity(h,z)['resource_supported_vehicles_per_week']['booth_occupancy'] is None
    # Half the workload at every resource doubles the bound.
    assert math.isclose(capacity(h,{r:v/2 for r,v in w.items()})['system_upper_bound_per_week'],800)
    # No rework must weakly reduce hours, while a shifted mix can increase them.
    clean=weighted_workload(cats,shares,{})
    assert all(clean[r]<=w[r] for r in w)
    assert all(math.isclose((1-t['required_workload_reduction_if_hours_constant'])*(1+t['growth']),1) for t in result['target_requirements'])
    assert next(s for s in result['scenarios'] if s['id']=='C_older_mix')['system_upper_bound_per_week']<400
    for s in result['scenarios']:
        q=s['system_upper_bound_per_week']
        assert all(q*s['workload_hours_per_vehicle'][r]<=s['available_resource_hours'][r]+1e-8 for r in w)
    return ['scale invariance','nonbinding labor no gain','zero-work route bypass','workload reciprocity',
            'rework monotonicity','target inverse arithmetic','mix downside','resource conservation']

def write_markdown(result):
    rows=['# Reproducible results — all scenarios illustrative','',
          'No Carvana site utilization or forecast is estimated. Run `python3 model.py` to reproduce.','',
          '## Growth requirements','',
          '| Target output growth | Required workload reduction at fixed hours | Current availability must be at most, if achievable target is 85% | Elyria 1,280/week reference target |',
          '|---|---:|---:|---:|']
    for t in result['target_requirements']:
        rows.append(f"| {t['growth']:.0%} | {t['required_workload_reduction_if_hours_constant']:.1%} | {t['max_current_availability_if_target_is_assumed_85pct']:.1%} | {t['elyria_reference_total_output_per_week']:,.0f} |")
    rows+=['','The 85% target is assumed. Elyria targets are arithmetic requirements, not expected output.','',
           '## Constructed plant: resource bottlenecks','',
           '| Case | Supported units/week | Change | Binding resource | Added weekly labor cost* |',
           '|---|---:|---:|---|---:|']
    for s in result['scenarios']:
        rows.append(f"| {s['id']} | {s['system_upper_bound_per_week']:.1f} | {s['change_vs_reference']:+.1%} | {', '.join(s['binding_resources'])} | ${s['added_paid_labor_cost_per_week_at_assumed_rate']:,.0f} |")
    rows+=['','*Labor-only at assumed wages and 80% productive share of paid incremental hours; excludes materials, training, capex, facilities and nonpaint costs. Zero does not mean zero implementation cost.','',
           '## Rework requirements','', '| Additional rework hours / first-pass work: before → after | Stage output gain |','|---|---:|']
    for r in result['rework_sensitivities']:rows.append(f"| {r['current_extra_rework_hours_over_first_pass']:.0%} → {r['future_extra_rework_hours_over_first_pass']:.0%} | {r['stage_capacity_gain']:.1%} |")
    rows+=['','## Capital screen','', '| Net incremental contribution / sold vehicle | Annual incremental contribution | Extra inventory | Maximum equipment + training capital* |','|---|---:|---:|---:|']
    for r in result['capital_screen']:rows.append(f"| ${r['net_incremental_contribution_per_sold_vehicle']} | ${r['annual_incremental_operating_contribution']:,.0f} | ${r['inventory_requirement']:,.0f} | ${r['max_equipment_and_training_capital_at_assumed_pretax_cash_return_hurdle']:,.0f} |")
    rows+=['','*100 additional weekly sales × 50 operating weeks, 10 calendar inventory days, $22k carrying value, 20% pretax cash return hurdle, all assumed. Not a project cost estimate or DCF; deduct other incremental capital and account separately for taxes, depreciation, maintenance and ramp losses.']
    (ROOT/'requirements.md').write_text('\n'.join(rows)+'\n')

if __name__=='__main__':
    data=json.loads((ROOT/'inputs.json').read_text())
    result=run(data);result['arithmetic_checks_passed']=checks(data,result)
    (ROOT/'results.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    write_markdown(result)
    print('Wrote results.json and requirements.md; 8 arithmetic checks passed. No calibration or independent validation claimed.')
