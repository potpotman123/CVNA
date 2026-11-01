"""Agreed 9-month linear ramp to 13k; calculations only, not observed output."""
from pathlib import Path
from datetime import date
from calendar import monthrange
import json
P=Path(__file__).resolve().parent
roster=json.loads((P.parent/'adesa-21-site-candidate-roster.json').read_text())
CAP=13000; RAMP=9
# Equal calendar-month units: every full calendar year has exactly 12 units.
def month(d): return d.year*12+d.month-1+(d.day-1)/monthrange(d.year,d.month)[1]
def cumulative(age):
    age=max(0,age); t=min(age,RAMP)
    return CAP/12*(t*t/(2*RAMP)+max(0,age-RAMP))
def production(start,a,b): return cumulative(b-start)-cumulative(a-start)
def rate(start,t): return CAP*min(1,max(0,(t-start)/RAMP))
cut=month(date(2026,10,1))
rows=[]
for s in roster['sites']:
    ds=s['evidence_date']; ds=ds+'-15' if len(ds)==7 else ds
    d=date.fromisoformat(ds); m=month(d)
    done_m=d.year*12+d.month-1+9; y,mo=divmod(done_m,12);mo+=1
    done=date(y,mo,min(d.day,monthrange(y,mo)[1]))
    r=dict(site=s['site'],source=s['source'],evidence_date=s['evidence_date'],date_meaning=s['date_meaning'],start_proxy=ds,start_status='operating month; assumed midpoint' if s['site']=='ADESA Buffalo' else 'announcement-date proxy, not verified first production',mature_date_proxy=done.isoformat(),bin_at_q3='mature_ADESA' if cut-m>=RAMP else 'ramping_ADESA',annual_capacity=CAP,q3_exit_annualized_rate=rate(m,cut))
    r['annual_production']={str(y):production(m,12*y,12*(y+1)) for y in range(2025,2029)}
    r['growth_2027_vs_2026']=r['annual_production']['2027']-r['annual_production']['2026']
    r['growth_2028_vs_2027']=r['annual_production']['2028']-r['annual_production']['2027']
    r['q4_2026']=production(m,cut,12*2027)
    r['extra_2027_vs_q3_exit_rate']=r['annual_production']['2027']-r['q3_exit_annualized_rate']
    rows.append(r)
def summarize(rs):
    return dict(sites=len(rs),capacity=sum(r['annual_capacity'] for r in rs),annual_production={str(y):sum(r['annual_production'][str(y)] for r in rs) for y in range(2025,2029)},growth_2027_vs_2026=sum(r['growth_2027_vs_2026'] for r in rs),growth_2028_vs_2027=sum(r['growth_2028_vs_2027'] for r in rs),q3_exit_annualized_rate=sum(r['q3_exit_annualized_rate'] for r in rs),extra_2027_vs_q3_exit_rate=sum(r['extra_2027_vs_q3_exit_rate'] for r in rs))
summaries={b:summarize([r for r in rows if r['bin_at_q3']==b]) for b in ['mature_ADESA','ramping_ADESA']};summaries['all']=summarize(rows)
sens=[]
for shift in [-3,0,3]:
    totals={str(y):sum(production(month(date.fromisoformat(r['start_proxy']))+shift,12*y,12*(y+1)) for r in rows if r['bin_at_q3']=='ramping_ADESA') for y in [2026,2027,2028]}
    sens.append(dict(start_shift_months=shift,annual_production=totals,growth_2027_vs_2026=totals['2027']-totals['2026']))
assert len(rows)==21 and summaries['mature_ADESA']['sites']==16 and summaries['ramping_ADESA']['sites']==5
assert abs(cumulative(12)-8125)<1e-6
assert all(abs(r['annual_production']['2028']-13000)<1e-6 for r in rows)
assert abs(summaries['all']['capacity']-273000)<1e-6
out=dict(method='Equal calendar-month time; exact integration of linear 9-month ramp. Q3 exit at 2026-10-01. Proxy dates as labeled. Fixed Q3 bins.',scope='21 candidate Q3 integrations; Orlando and future integrations excluded',assumptions=dict(annual_capacity=CAP,ramp_months=RAMP,mature_fraction=1),rows=rows,summaries=summaries,ramping_start_date_sensitivity=sens)
(P/'adesa-cohort-build-2026-11-01.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(summaries,indent=2))
for r in rows:
 if r['bin_at_q3']=='ramping_ADESA':print(r['site'],r['start_proxy'],r['mature_date_proxy'],*[round(r['annual_production'][str(y)]) for y in [2026,2027,2028]],round(r['growth_2027_vs_2026']))
print(json.dumps(sens,indent=2))
