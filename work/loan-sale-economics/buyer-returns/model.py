"""CVNA 2026-P2 bounded economic model. Stdlib only; run from any directory.
Outputs are SCENARIOS, not observed buyer returns or reported sale gains.
All normalized amounts are dollars per $100 cutoff principal; yields annual effective.
"""
from pathlib import Path
import json,re,math
P=Path(__file__).parent
T=json.loads((P/'sources/prospectus-tables.json').read_text())
POOL=1100395400.20
coh=[]
for t in T[225:228]:
 for i,b,r,o,n in re.findall(r'(\d+) \$([\d,]+\.\d+) ([\d.]+)% (\d+) (\d+)',t):
  coh.append(dict(id=int(i),balance=float(b.replace(',',''))/POOL*100,apr=float(r)/100,original=int(o),remaining=int(n)))
assert len(coh)==67 and abs(sum(c['balance'] for c in coh)-100)<1e-8
# Rate from loan records is used as an independent definition check in report.
FACE=[122.28,323.5,323.5,213.37,45.11,48.97,23.66]
CPN=[.03915,.044,.0477,.0491,.0519,.058,.0618]
PRICE=[100,99.99605,99.98692,99.99533,99.99014,99.96028,99.95572]
NFACE=16.5/ (POOL/1e6)*100
RPRICE=49.272/(POOL/1e6)*100

def pv(cf,y):return sum(v/(1+y)**((i+1)/12) for i,v in enumerate(cf))
def irr(cf,p):
 lo,hi=-.95,5.
 if pv(cf,lo)<p or pv(cf,hi)>p:return None
 for _ in range(65):
  mid=(lo+hi)/2
  if pv(cf,mid)>p:lo=mid
  else:hi=mid
 return (lo+hi)/2

def asset_run(h,abs_speed=.013,recovery=.35,lag=3,apr_shift=0,fee=.0045,shape=18,groups=None):
 """ABS is total unscheduled attrition including defaults, NOT annual CPR.
 Calibrate shaped default hazard inside total attrition; residual is voluntary prepay.
 Regular monthly annuity schedules, no first-period stub or clean-up call.
 """
 cs=[dict(c) for c in (groups or coh)]; rec={}; rows=[]
 for m in range(1,100):
  begin=sum(c['balance'] for c in cs); d=s=p=it=0.
  for c in cs:
   b=c['balance'];n=c['remaining'];r=max(0,c['apr']+apr_shift)/12
   if b<1e-12 or n<=0:continue
   age=c['original']-n
   total=min(1,abs_speed/max(1e-9,1-abs_speed*age))
   haz=min(total,h*(m/shape)**2*math.exp(2-2*m/shape))
   default=b*haz;alive=b-default
   pay=alive*r/(1-(1+r)**(-n)) if r else alive/n
   interest=alive*r;scheduled=min(alive,max(0,pay-interest))
   voluntary=(alive-scheduled)*(total-haz)/max(1e-12,1-haz)
   c['balance']=max(0,alive-scheduled-voluntary);c['remaining']-=1
   d+=default;s+=scheduled;p+=voluntary;it+=interest
  end=sum(c['balance'] for c in cs)
  if d>1e-12:rec[m+lag]=rec.get(m+lag,0)+d*recovery
  recovered=rec.get(m,0);serv=begin*fee/12
  # recurring fee assumptions: observed Sep recurring + prospectus annual charges.
  admin=(6316.68+(52000 if m%12==0 else 0))/POOL*100 if begin>1e-10 else 0
  cash=s+p+it+recovered-serv-admin
  assert abs(begin-end-d-s-p)<1e-8
  rows.append(dict(month=m,begin=begin,default=d,scheduled=s,prepay=p,interest=it,recovery=recovered,servicing=serv,admin=admin,end=end,asset_cash=cash))
  if end<1e-10 and m>=max(rec.keys(),default=0):break
 return rows

def calibrate(cnl=3,**kw):
 lo,hi=0.,.2
 for _ in range(42):
  mid=(lo+hi)/2;rows=asset_run(mid,**kw)
  loss=sum(r['default']-r['recovery'] for r in rows)
  if loss<cnl:lo=mid
  else:hi=mid
 rows=asset_run((lo+hi)/2,**kw)
 assert abs(sum(r['default']-r['recovery'] for r in rows)-cnl)<1e-7
 return rows

def waterfall(rows,fee=.0045,coupon_shift=0):
 """Normal waterfall: 1% strip, fees, A/B/C/D interest interleaved with parity
 cures; reserve top-up; OC target; N interest, N reserve, 65% N principal; R.
 No legal acceleration or optional call; shortfalls flagged, not interpreted as exact stress pricing.
 """
 bal=[x/(POOL/1e6)*100 for x in FACE];nb=NFACE;res=.5;nr=.25;out=[];short=0
 for a in rows:
  m=a['month'];res0=res;nr0=nr
  # Whole-loan cash already removes base servicing and admin. XS is separate economic interest.
  xs=a['begin']*max(0,.01-fee)/12
  cash=a['asset_cash']-xs
  interest=[0.]*7;principal=[0.]*7;ni=np=rc=depositor=0.
  def use(x,access=False):
   nonlocal cash,res,short
   if access and cash<x:
    draw=min(res,x-cash);res-=draw;cash+=draw
   paid=min(max(0,cash),max(0,x));cash-=paid
   return paid
  def payprincipal(x):
   left=x
   for j in range(7):
    z=min(bal[j],left);bal[j]-=z;principal[j]+=z;left-=z
   assert abs(left)<1e-8
  # A pro rata interest (normal scenarios fully paid), then parity cures at each level.
  for group,last in [([0,1,2,3],3),([4],4),([5],5),([6],6)]:
   dues=[bal[j]*(CPN[j]+coupon_shift)/12 for j in group];tot=sum(dues)
   paid=use(tot,True);short+=max(0,tot-paid)
   for j,due in zip(group,dues):interest[j]=paid*due/tot if tot else 0
   need=max(0,sum(bal[:last+1])-a['end']);payprincipal(use(need,True))
  target=min(.5,sum(bal));top=use(max(0,target-res));res+=top
  if res>target:cash+=res-target;res=target
  regular=min(sum(bal),max(0,sum(bal)+.9-a['end']))
  payprincipal(use(regular))
  if 0<sum(bal)<=cash+res:payprincipal(use(sum(bal),True))
  ndue=nb*(.0537+coupon_shift)/12
  if cash<ndue:
   draw=min(nr,ndue-cash);nr-=draw;cash+=draw
  ni=use(ndue);short+=ndue-ni
  if nb>1e-9:nr+=use(max(0,.25-nr))
  np=min(nb,max(0,cash)*.65);cash-=np;nb-=np
  if nb<1e-9:depositor+=nr;nr=0
  if sum(bal)<1e-9:cash+=res;res=0
  rc=max(0,cash)
  # Conservation includes both accounts. Asset_cash is net of base servicing and admin.
  paid=sum(interest)+sum(principal)+ni+np+rc+xs+depositor
  err=a['asset_cash']+res0+nr0-res-nr-paid
  assert abs(err)<1e-7,(m,err)
  out.append(dict(month=m,xs=xs,residual=rc,depositor_reserve_release=depositor,n_interest=ni,n_principal=np,reserve=res,n_reserve=nr,n_balance=nb,note_balance=sum(bal),note_interest=interest,note_principal=principal,cash_error=err))
 assert sum(bal)+nb<1e-7,'terminal unpaid debt: exact acceleration model required'
 return out,short

def scenario(cnl=3,abs_speed=.013,recovery=.35,lag=3,apr_shift=0,fee=.0045,shape=18,coupon_shift=0,groups=None):
 rows=calibrate(cnl,abs_speed=abs_speed,recovery=recovery,lag=lag,apr_shift=apr_shift,fee=fee,shape=shape,groups=groups)
 w,short=waterfall(rows,fee,coupon_shift)
 cf=[r['asset_cash'] for r in rows];r=[x['residual'] for x in w];xs=[x['xs'] for x in w]
 vals={'cnl_pct':cnl,'total_abs_monthly_pct':abs_speed*100,'recovery_pct':recovery*100,'lag_months':lag,'apr_shift_pp':apr_shift*100,'base_servicing_pct':fee*100,'default_shape_peak_month':shape,
 'asset_price_at_yield':{str(y):pv(cf,y) for y in [.05,.06,.07,.08,.09]},'asset_irr_at_price':{str(p):irr(cf,p) for p in [100,105,107.4,110]},
 'residual_price_per100_at_18_5pct':pv(r,.185),'residual_m_at_18_5pct':pv(r,.185)*POOL/100/1e6,'residual_irr_at_filed_value':irr(r,RPRICE),
 'xs_price_at_10pct':pv(xs,.10),'depositor_reserve_release_pv_at_10pct':pv([x['depositor_reserve_release'] for x in w],.10),'gross_loss_pct':sum(a['default'] for a in rows),'recovered_pct':sum(a['recovery'] for a in rows),
 'principal_wal_years':sum(a['month']/12*(a['scheduled']+a['prepay']+a['recovery']) for a in rows)/sum(a['scheduled']+a['prepay']+a['recovery'] for a in rows),
 'interest_shortfall':short,'note_irr_at_issue_price':{},'n_irr_at_issue_price':irr([x['n_interest']+x['n_principal'] for x in w],NFACE*.9999801),
 'asset_conservation_error':sum(a['scheduled']+a['prepay']+a['default'] for a in rows)-100,'max_waterfall_error':max(abs(x['cash_error']) for x in w)}
 for j,name in enumerate(['A1','A2','A3','A4','B','C','D']):vals['note_irr_at_issue_price'][name]=irr([x['note_interest'][j]+x['note_principal'][j] for x in w],FACE[j]/(POOL/1e6)*PRICE[j])
 return vals,rows,w

def main():
 central,rows,w=scenario()
 cases={}
 for name,kw in {'loss2':{'cnl':2},'loss4':{'cnl':4},'loss6':{'cnl':6},'slow_attrition':{'abs_speed':.008},'fast_attrition':{'abs_speed':.018},'apr_minus1':{'apr_shift':-.01},'apr_plus2':{'apr_shift':.02},'servicing_051':{'fee':.0051},'servicing_1pct':{'fee':.01},'recovery_lag6':{'lag':6},'recovery20':{'recovery':.20},'recovery50':{'recovery':.50},'loss275':{'cnl':2.75},'early_loss':{'shape':9},'late_loss':{'shape':30},'funding_plus1':{'coupon_shift':.01},'average_loan':{'groups':[dict(id=1,balance=100,apr=.1054,original=75,remaining=74)]}}.items():cases[name]=scenario(**kw)[0]
 gross_ad=sum(f*p/100 for f,p in zip(FACE,PRICE));gross_n=16.5*.9999801
 bridge={'pool_m':POOL/1e6,'AD_all_notes_market_value_m':gross_ad,'AD_95pct_gross_m':gross_ad*.95,'AD_net_underwriting_m':1042.661118,'AD_underwriting_discount_m':2.613422,'N_all_notes_pricing_value_m':gross_n,'R_all_pricing_value_m':49.272,'R_95pct_pricing_value_m':46.8084,'total_AD_N_R_pricing_value_m':gross_ad+gross_n+49.272,'reserve_funding_m':8.2529655,'estimated_other_issue_expense_m':1.,'all_class_value_less_reserves_AD_underwriting_and_expense_m':gross_ad+gross_n+49.272-8.2529655-2.613422-1,'unknowns':['XS actual sale price/ownership','N/R private placement fees and final settlement confirmation','transaction carrying basis/accrued interest/capitalized costs','exact retained fair values and deal gain'],'modeled_XS_at10pct_m':central['xs_price_at_10pct']*POOL/100/1e6}
 out={'status':'Sensitivity model; not a fair-value opinion or actual gain reconstruction','central':central,'sensitivities':cases,'transaction_bridge':bridge}
 (P/'results.json').write_text(json.dumps(out,indent=2));(P/'central-monthly-cashflows.json').write_text(json.dumps({'assets':rows,'waterfall':w},indent=2));(P/'cohorts.json').write_text(json.dumps(coh,indent=2))
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
