"""Conditional light-integration ramp; rolling years since first production."""
import json
capacity = 13000
mature_fraction = 1.0

def cumulative(month, ramp_months):
    t = min(month, ramp_months)
    return capacity * mature_fraction / 12 * (t*t/(2*ramp_months) + max(0, month-ramp_months))

rows=[]
for label, months in [('fast',6),('base',9),('slow',18)]:
    first=cumulative(12,months)
    second=cumulative(24,months)-first
    rows.append(dict(case=label,ramp_months=months,first_12_months=first,second_12_months=second,mature_annual=capacity*mature_fraction))
assert all(abs(r['first_12_months']-v)<1e-8 for r,v in zip(rows,[9750,8125,13000/3]))
assert all(abs(r['second_12_months']-v)<1e-8 for r,v in zip(rows,[13000,13000,13000*11/12]))
print(json.dumps(dict(capacity=capacity,mature_fraction=mature_fraction,cases=rows),indent=2))
