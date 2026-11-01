"""Conditional light-integration ramp; rolling years since first production."""
import json
capacity = 13000
mature_fraction = 0.9

def cumulative(month, ramp_months):
    t = min(month, ramp_months)
    return capacity * mature_fraction / 12 * (t*t/(2*ramp_months) + max(0, month-ramp_months))

rows=[]
for label, months in [('fast',6),('base',12),('slow',18)]:
    first=cumulative(12,months)
    second=cumulative(24,months)-first
    rows.append(dict(case=label,ramp_months=months,first_12_months=first,second_12_months=second,mature_annual=capacity*mature_fraction))
assert [r['first_12_months'] for r in rows]==[8775,5850,3900]
assert [r['second_12_months'] for r in rows]==[11700,11700,10725]
print(json.dumps(dict(capacity=capacity,mature_fraction=mature_fraction,cases=rows),indent=2))
