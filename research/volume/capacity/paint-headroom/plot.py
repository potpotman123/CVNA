"""Publication plot of conditional requirements; never labels assumptions as CVNA estimates."""
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
ROOT=Path(__file__).resolve().parent
r=json.loads((ROOT/'results.json').read_text())
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(1,2,figsize=(12,5.2),gridspec_kw={'width_ratios':[1,1.35]})
g=[x['growth'] for x in r['target_requirements']]
w=[x['required_workload_reduction_if_hours_constant'] for x in r['target_requirements']]
axs[0].bar([f'{x:.0%}' for x in g],w,color='#267c92',width=.55)
for i,y in enumerate(w):axs[0].text(i,y+.006,f'{y:.1%}',ha='center',fontweight='bold')
axs[0].set_ylim(0,.29);axs[0].yaxis.set_major_formatter(PercentFormatter(1))
axs[0].set_xlabel('Target increase in acceptable output')
axs[0].set_ylabel('Required reduction in binding workload')
axs[0].set_title('Same productive hours',loc='left',fontweight='bold',pad=16)
q=r['rework_sensitivities'];vals=[x['stage_capacity_gain'] for x in q]
labels=[f"{x['current_extra_rework_hours_over_first_pass']:.0%} to {x['future_extra_rework_hours_over_first_pass']:.0%}" for x in q]
axs[1].barh(labels,vals,color='#ca8754',height=.55)
for i,y in enumerate(vals):axs[1].text(y+.006,i,f'{y:.1%}',va='center',fontweight='bold')
axs[1].invert_yaxis();axs[1].set_xlim(0,.33);axs[1].xaxis.set_major_formatter(PercentFormatter(1))
axs[1].set_xlabel('Potential output gain at that stage')
axs[1].set_ylabel('Extra repeat-work hours / first-pass hours')
axs[1].set_title('Rework reduction: assumed cases',loc='left',fontweight='bold',pad=16)
fig.suptitle('Paint headroom: requirements, not a Carvana forecast',fontsize=16,fontweight='bold',x=.05,ha='left',y=.98)
fig.text(.05,.025,'Assumes unchanged repair mix and no other binding stage. Realized whole-site gains can be smaller.\nSource: reproducible arithmetic in model.py; no measured Carvana rework rate is assumed.',fontsize=10,color='#555555')
fig.subplots_adjust(top=.80,bottom=.24,left=.09,right=.97,wspace=.62)
fig.savefig(ROOT/'headroom-requirements.png',dpi=180)
plt.close(fig)
