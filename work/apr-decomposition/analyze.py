import gzip,xml.etree.ElementTree as ET,json,collections,math
from pathlib import Path
P=Path(__file__).parent

def number(d,key):
 try:return float(d[key])
 except:return None

def parse(name):
 rows=[];first=None
 for event,e in ET.iterparse(gzip.open(P/(name+'-ex102.xml.gz'),'rb'),events=['end']):
  if e.tag.split('}')[-1]!='assets':continue
  d={x.tag.split('}')[-1]:x.text for x in e.iter() if len(x)==0}
  if first is None:first=d
  rows.append(d);e.clear()
 (P/(name+'-fields.json')).write_text(json.dumps(first,indent=2))
 return rows

if __name__=='__main__':
 result={}
 for name in ['2025-p2','2026-p2']:
  rows=parse(name)
  fields=['originalLoanAmount','reportingPeriodBeginningLoanBalanceAmount','reportingPeriodActualEndBalanceAmount','originalInterestRatePercentage','reportingPeriodInterestRatePercentage','obligorCreditScore','originalLoanTerm','vehicleValueAmount','paymentToIncomePercentage']
  stats={}
  for f in fields:
   vals=[number(d,f) for d in rows];vals=[v for v in vals if v is not None]
   stats[f]={'n':len(vals),'min':min(vals) if vals else None,'max':max(vals) if vals else None,'sum':sum(vals)}
  result[name]={'count':len(rows),'stats':stats}
  with gzip.open(P/(name+'-rows.json.gz'),'wt') as out:json.dump(rows,out)
 (P/'field-check.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
