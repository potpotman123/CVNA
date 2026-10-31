import gzip,json,re,collections,math
from pathlib import Path
P=Path(__file__).parent

def f(d,k):
 try:return float(d[k])
 except:return None

def prepare(name,weight='end',used_only=False):
 raw=json.load(gzip.open(P/(name+'-rows.json.gz'),'rt'));out=[]
 for d in raw:
  if used_only and d.get('vehicleNewUsedCode')!='2':continue
  score=d.get('obligorCreditScore') or ''
  if name=='2026-p2':
   m=re.search(r'FICO\s+(\d+)',score);fico=float(m.group(1)) if m else None
  else:fico=f(d,'obligorCreditScore')
  bal=f(d,'reportingPeriodActualEndBalanceAmount') if weight=='end' else f(d,'originalLoanAmount')
  apr=f(d,'originalInterestRatePercentage')
  if not bal or apr is None:continue
  term=f(d,'originalLoanTerm');amt=f(d,'originalLoanAmount');value=f(d,'vehicleValueAmount')
  month,year=map(int,d['originationDate'].split('/'))
  out.append(dict(w=bal,apr=apr,fico=fico,term=term,amount=amt,ltv=amt/value if value else None,age=year-int(d['vehicleModelYear']),new=d.get('vehicleNewUsedCode'),origin=d.get('originatorName'),pti=f(d,'paymentToIncomePercentage'),date=d['originationDate']))
 return out

def mean(rows,key):
 v=[r for r in rows if r[key] is not None];return sum(r['w']*r[key] for r in v)/sum(r['w'] for r in v)
def bucket(v,edges):
 if v is None:return 'missing'
 return str(next((i for i,x in enumerate(edges) if v<=x),len(edges)))
def key(r,kind):
 b=bucket(r['fico'],[450,500,550,600,650,700,750,800])
 if kind=='fico':return b
 if kind=='fico25':return bucket(r['fico'],list(range(450,851,25)))
 a=[b,bucket(r['term'],[60,72,75,78])]
 if kind=='fico_term':return '|'.join(a)
 a += [bucket(r['ltv'],[.8,1.,1.2]),bucket(r['age'],[2,5,8])]
 if kind=='fico_term_ltv_age':return '|'.join(a)
 a += [bucket(r['amount'],[20000,30000,40000])]
 return '|'.join(a)
def agg(rows,kind):
 a={}
 for r in rows:
  k=key(r,kind);v=a.setdefault(k,[0.,0.,0]);v[0]+=r['w'];v[1]+=r['w']*r['apr'];v[2]+=1
 return a

def decomp(r0,r1,kind,minn=1):
 a,b=agg(r0,kind),agg(r1,kind);common={k for k in a.keys()&b.keys() if min(a[k][2],b[k][2])>=minn}
 t0=sum(x[0] for x in a.values());t1=sum(x[0] for x in b.values());s0=sum(a[k][0] for k in common);s1=sum(b[k][0] for k in common)
 mix=within=0;details=[]
 for k in sorted(common):
  w0=a[k][0]/s0;w1=b[k][0]/s1;p0=a[k][1]/a[k][0];p1=b[k][1]/b[k][0]
  mix+=(w1-w0)*(p0+p1)/2;within+=(w1+w0)/2*(p1-p0)
  details.append(dict(bucket=k,share0=w0,share1=w1,apr0=p0,apr1=p1,n0=a[k][2],n1=b[k][2]))
 m0=sum(a[k][1] for k in common)/s0;m1=sum(b[k][1] for k in common)/s1
 assert abs(mix+within-(m1-m0))<1e-10
 return dict(kind=kind,min_count_each=minn,coverage0=s0/t0,coverage1=s1/t1,apr0=m0,apr1=m1,total_bps=(m1-m0)*10000,mix_bps=mix*10000,within_bps=within*10000,groups=len(common),details=details if kind=='fico' else None)
result={}
for weight,used in [('end',False),('original',False),('end',True)]:
 a,b=prepare('2025-p2',weight,used),prepare('2026-p2',weight,used)
 label=weight+('_used' if used else '_all')
 result[label]={'summary':[{'count':len(x),'balance':sum(r['w'] for r in x),'apr':mean(x,'apr'),'fico':mean(x,'fico'),'term':mean(x,'term'),'ltv_salesprice_proxy':mean(x,'ltv'),'vehicle_age':mean(x,'age'),'pti':mean(x,'pti'),'originations':dict(collections.Counter(r['date'] for r in x))} for x in [a,b]],'decompositions':[decomp(a,b,k,10 if k not in ['fico','fico25','fico_term'] else 1) for k in ['fico','fico25','fico_term','fico_term_ltv_age','fico_term_ltv_age_amount']]}
(P/'results.json').write_text(json.dumps(result,indent=2))
for k,v in result.items():
 print(k,json.dumps(v['summary']))
 for d in v['decompositions']:print({k:v for k,v in d.items() if k!='details'})
print('FICO detail',json.dumps(result['end_all']['decompositions'][0]['details'],indent=2))
