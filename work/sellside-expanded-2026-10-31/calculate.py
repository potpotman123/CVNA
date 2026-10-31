"""Reproduce selected calculations; source IDs refer to manifest.json. No network access."""
from pathlib import Path
import json
from statistics import mean
ROOT=Path(__file__).resolve().parent
loans=[
 ('2025-P1',14.06,4.62,24146,702,73),('2025-P2',12.80,4.66,25042,701,73),
 ('2025-P3',12.11,4.18,26426,702,73),('2025-P4',11.24,4.26,26188,702,73),
 ('2026-P1',10.67,4.29,26589,713,75),('2026-P2',10.54,4.69,28441,708,75),
 ('2026-P3',10.77,4.75,29620,702,75)]
pools=['2022-P3','2024-P2','2024-P3','2024-P4','2025-P1']
jun=[2.82,1.35,1.63,1.36,1.26]
jul=[3.29,1.47,1.60,1.46,1.41]
jul_new=[.84]+jul[1:]
results={
 'prime_pools':{'source':'10.pdf PDF p3','status':'analyst-reported deal characteristics, not companywide realized returns','rows':[dict(zip(['deal','apr_pct','note_coupon_pct','average_principal_usd','fico','term_months'],r),spread_pct=r[1]-r[2]) for r in loans]},
 'july_delinquency_bridge':{'source':'11.pdf PDF p2','unit':'percentage points unless marked bp','method':'equal-weight means reproduce reported rounded headline; original-pool hold-constant check, not age-adjusted underwriting test','original_pools':pools,'june_rates':jun,'july_original_rates':jul,'replacement_pool':'2025-P2','replacement_rate':.84,'june_mean':mean(jun),'july_original_mean':mean(jul),'july_new_mean':mean(jul_new),'within_original_bp':(mean(jul)-mean(jun))*100,'replacement_bp':(mean(jul_new)-mean(jul))*100,'headline_bp':(mean(jul_new)-mean(jun))*100},
 'prime_endpoint_change':{'apr_bp':(loans[-1][1]-loans[0][1])*100,'spread_bp':((loans[-1][1]-loans[-1][2])-(loans[0][1]-loans[0][2]))*100,'principal_pct':(loans[-1][3]/loans[0][3]-1)*100},
 'q3_actual':{'source':'cvna-q3-2026-letter.pdf quarterly results and Adjusted EBITDA reconciliation','units_2025':155941,'units_2026':217385,'ebitda_m_2025':637,'ebitda_m_2026':800,'unit_growth_pct':(217385/155941-1)*100,'ebitda_growth_pct':(800/637-1)*100,'ebitda_per_unit_2025':637e6/155941,'ebitda_per_unit_2026':800e6/217385,'per_unit_change_pct':((800/217385)/(637/155941)-1)*100,'loan_gain_per_retail_unit_2025':331e6/155941,'loan_gain_per_retail_unit_2026':381e6/217385},
 'stephens_fy26_estimate_revision':{'sources':['16.pdf front/model tables','10.pdf front/model tables'],'dates':['2026-01-29','2026-08-24'],'revenue_m':[25750.4,29070.0],'ebitda_m':[2951.0,2906.2],'revenue_revision_pct':(29070/25750.4-1)*100,'ebitda_revision_pct':(2906.2/2951-1)*100,'implied_margins_pct':[2951/25750.4*100,2906.2/29070*100],'caveat':'analyst forecast snapshots, not outcomes; later revenue rounded to nearest $10m from front page'},
 'capacity_capex':{'source':'31.pdf p3; analyst estimates','light_usd_per_annual_unit':[2e6/13000,3e6/13000],'full_usd_per_annual_unit':[30e6/40000,35e6/40000],'caveat':'incremental project spending / stated incremental annual capacity; excludes acquired property cost and working capital; not marginal cash cost per car'},
 'ms_irc_model':{'source':'31.pdf p4; hypothetical analyst model','gpu_retail':3300,'gpu_other':2800,'operating_cost_per_unit':1620,'modeled_operating_profit_per_unit':4480,'other_share_of_modeled_operating_profit_pct':2800/4480*100,'year1_units':21000,'runrate_units':51000,'year1_op_m':4480*21000/1e6,'runrate_op_m':4480*51000/1e6,'sensitivity_500_less_gpu_year1_m':500*21000/1e6,'sensitivity_500_less_gpu_runrate_m':500*51000/1e6},
 'servicing_denominator':{'source':'36.pdf p3 rounded table inputs','annual_fee_m':10,'origination_denominator_m':8888,'average_receivable_denominator_m':461,'incorrect_flow_rate_pct':10/8888*100,'rounded_stock_rate_pct':10/461*100,'analyst_printed_rate_pct':2.3,'caveat':'rounded inputs give 2.17%, not exactly printed 2.3%; average of year-end balances not verified time-weighted balance; different servicing populations remain incomparable without contracts'}
}
(ROOT/'calculations.json').write_text(json.dumps(results,indent=2)+'\n')
try:
 import matplotlib
 matplotlib.use('Agg')
 import matplotlib.pyplot as plt
 fig,axs=plt.subplots(1,2,figsize=(13,5),layout='constrained')
 ax=axs[0];x=list(range(len(loans)))
 ax.plot(x,[r[1] for r in loans],marker='o',label='Borrower APR')
 ax.plot(x,[r[2] for r in loans],marker='o',label='Weighted note coupon')
 ax.plot(x,[r[1]-r[2] for r in loans],marker='o',label='Difference before losses and costs')
 ax.set_xticks(x,[r[0] for r in loans],rotation=40);ax.set_ylabel('%');ax.set_title('Prime ABS: narrower financing spread');ax.legend(fontsize=8);ax.grid(alpha=.2)
 ax=axs[1];v=[mean(jun),mean(jul),mean(jul_new)]
 bars=ax.bar(['June\noriginal five pools','July\nsame five pools','July\nnew basket'],v,color=['#577590','#e09f3e','#43aa8b'])
 for b,z in zip(bars,v):ax.text(b.get_x()+b.get_width()/2,z+.025,f'{z:.3f}%',ha='center')
 ax.set_ylim(0,2.2);ax.set_ylabel('61+ day delinquency, equal-weight mean (%)');ax.set_title('July credit improvement depends on pool selection')
 fig.suptitle('Carvana: two findings from the supplied research',fontsize=15)
 fig.text(.01,-.035,'Sources: Stephens, Aug 24 2026 p3 and Aug 21 2026 p2. Calculations from rounded report values. Same-pool check is not age-adjusted.',fontsize=8)
 fig.savefig(ROOT/'evidence-chart.png',dpi=160,bbox_inches='tight');plt.close(fig)
except ImportError:
 pass
print(json.dumps({k:v for k,v in results.items() if k in ['prime_endpoint_change','q3_actual','stephens_fy26_estimate_revision']},indent=2))
