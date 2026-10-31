"""Overlay reported series; production shown only as an open-ended lower bound."""
from pathlib import Path
import os,json
os.environ.setdefault('MPLCONFIGDIR','/private/tmp/cvna-chart-mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.lines import Line2D
p=Path(__file__).resolve().parent
d=json.loads((p/'inventory-sales-data.json').read_text())['series']
x=list(range(len(d)))
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,ax=plt.subplots(figsize=(12,6.8))
fig.subplots_adjust(left=.09,right=.96,top=.79,bottom=.24)
fig.suptitle('Carvana: sales, website inventory and disclosed production',x=.09,ha='left',y=.97,fontsize=17,weight='bold')
fig.text(.09,.922,'Same vehicle-count scale • sales are quarterly flows; website inventory is a quarter-end stock',fontsize=11,color='#555555')
blue,orange,green='#17678b','#b06a20','#36845b'
ax.plot(x,[r['sales'] for r in d],color=blue,lw=2.5,marker='o',ms=5,label='Retail sales during quarter')
ax.plot(x,[r['website_units'] for r in d],color=orange,lw=2.5,marker='s',ms=4,label='Website listings at quarter-end')
# Threshold at 200k is reported, not an exact production observation.
ax.plot([9.9,10.1],[200000,200000],color=green,lw=2)
ax.annotate('',xy=(10,252000),xytext=(10,201000),arrowprops={'arrowstyle':'->','color':green,'lw':1.8,'linestyle':'--'})
ax.annotate('Q3 production: >200k\nManagement: slightly above sales\nExact production count unavailable',xy=(10,246000),xytext=(6.05,259000),ha='left',va='top',fontsize=10,color=green)
for key,col,offset in [('sales',blue,(0,-21)),('website_units',orange,(0,12))]:
 for i in [0,3,6,10]:
  v=d[i][key]
  ax.annotate(f'{v/1000:.1f}k',(i,v),xytext=offset,textcoords='offset points',ha='center',fontsize=10,color=col)
ax.set_ylim(0,270000);ax.set_xlim(-.35,10.45)
ax.set_ylabel('Vehicles (thousands)')
ax.yaxis.set_major_formatter(FuncFormatter(lambda v,pos:f'{v/1000:.0f}'))
ax.set_yticks([0,50000,100000,150000,200000,250000])
ax.set_xticks(x,[r['quarter'].replace(' ','\n') for r in d],fontsize=9)
ax.grid(axis='y',color='#dddddd',linewidth=.6);ax.set_axisbelow(True)
handles,labels=ax.get_legend_handles_labels()
handles.append(Line2D([0],[0],color=green,lw=1.8,ls='--'));labels.append('Production: lower bound only')
fig.legend(handles,labels,loc='upper left',bbox_to_anchor=(.085,.884),ncol=3,frameon=False,fontsize=10)
fig.text(.09,.127,'Production is not interpolated: no complete quarterly unit series is disclosed in the reviewed sources.',fontsize=10)
fig.text(.09,.092,'Website listings include reserved and unfinished vehicles. Their level is not directly comparable with quarterly sales.',fontsize=10)
fig.text(.09,.053,'Production growth disclosures: FY2025 >40% YoY; Q2 2026 +36% YoY. These do not establish quarterly unit levels.',fontsize=10)
fig.text(.09,.018,'Sources: Carvana filings and earnings calls; accompanying inventory-sales-data.json records observations and provenance.',fontsize=9,color='#555555')
fig.savefig(p/'inventory-sales-production-overlay.png',dpi=180,facecolor='white')
print(p/'inventory-sales-production-overlay.png')
