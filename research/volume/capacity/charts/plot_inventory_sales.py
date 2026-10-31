from pathlib import Path
import os,json
os.environ.setdefault('MPLCONFIGDIR','/private/tmp/cvna-chart-mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
p=Path(__file__).resolve().parent
d=json.loads((p/'inventory-sales-data.json').read_text())['series']
x=list(range(len(d)))
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(2,1,figsize=(12,7.4),sharex=True)
fig.subplots_adjust(left=.09,right=.96,top=.84,bottom=.20,hspace=.36)
fig.suptitle('Carvana: quarterly sales and quarter-end website inventory',x=.09,ha='left',y=.97,fontsize=18,weight='bold')
fig.text(.09,.918,'Q1 2024–Q3 2026  •  Flows and stocks shown separately; panel scales differ',fontsize=11,color='#555555')
for ax,key,title,color,lim in [(axs[0],'sales','RETAIL SALES  |  vehicles sold during each quarter','#17678b',245000),(axs[1],'website_units','WEBSITE LISTINGS  |  vehicles listed at quarter-end','#b06a20',100000)]:
 vals=[r[key] for r in d]
 ax.plot(x,vals,color=color,lw=2.4,marker='o',ms=5)
 ax.set_title(title,loc='left',fontsize=11,pad=12,weight='bold')
 ax.set_ylim(0,lim);ax.set_xlim(-.35,10.45)
 ax.set_ylabel('Vehicles (000s)')
 ax.yaxis.set_major_formatter(FuncFormatter(lambda v,pos:f'{v/1000:.0f}'))
 ax.grid(axis='y',color='#dddddd',linewidth=.6)
 ax.set_axisbelow(True)
 for i,v in enumerate(vals):ax.annotate(f'{v/1000:.1f}k',(i,v),xytext=(0,10),textcoords='offset points',ha='center',fontsize=9,color=color)
axs[1].set_xticks(x,[r['quarter'].replace(' ','\n') for r in d],fontsize=9)
fig.text(.09,.095,'Listings include reserved cars and vehicles awaiting reconditioning—not just immediately sale-ready cars.',fontsize=10)
fig.text(.09,.064,'Production: exact quarterly series unavailable. Q3 2026 exceeded 200k; management said it slightly exceeded sales.',fontsize=10)
fig.text(.09,.029,'Sources: Carvana 10-K / 10-Q operating metrics, shareholder letters and calls. See accompanying data for provenance.',fontsize=9,color='#555555')
fig.savefig(p/'inventory-sales.png',dpi=180,facecolor='white')
print('Saved',p/'inventory-sales.png')
print('Q3 YoY sales:',d[-1]['sales']/d[6]['sales']-1,'website units:',d[-1]['website_units']/d[6]['website_units']-1)
