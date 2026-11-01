"""Reproduce exploratory chat DCF; assumptions, not investment recommendation."""
import json
from pathlib import Path
P=Path(__file__).resolve().parent
volume=json.loads((P.parent/'volume/capacity/volume-bridge-2026-11-01.json').read_text())['annual']
base_units=217385*4
market_equity_bn=76.2
price=68.29
exit_multiple=78.29/3
net_debt_bn=5.228-3.049
tra_bn=2.130
shares_bn=market_equity_bn/price

def operating(fixed_share=.30,gross_profit_loss_per_unit=0):
    rows=[];previous=base_units
    for t,r in enumerate(volume,1):
        year=r['year'];units=r['total_production'];scale=units/base_units
        revenue=8040*4*scale
        gross_profit=1542*4*scale-gross_profit_loss_per_unit*units/1e6
        sga=742*4*((1-fixed_share)*scale+fixed_share*1.03**t)
        ebitda=gross_profit-sga
        sbc=100*scale;da=.008*revenue
        taxes=max(0,ebitda-sbc-da)*.25
        recurring_capex=.01*revenue
        buildout_capex=97.5 if year<=2034 else 0
        integration_capex=17.5 if year<=2029 else 15 if year==2030 else 0
        working_capital=(units-previous)*4200/1e6
        capex=recurring_capex+buildout_capex+integration_capex
        fcf=ebitda-sbc-taxes-capex-working_capital
        rows.append(dict(year=year,retail_units=units,retail_revenue_m=6144*4*scale,total_revenue_m=revenue,adjusted_ebitda_m=ebitda,ebitda_margin=ebitda/revenue,stock_compensation_m=sbc,depreciation_m=da,taxes_m=taxes,recurring_capex_m=recurring_capex,buildout_capex_m=buildout_capex,integration_capex_m=integration_capex,incremental_working_capital_m=working_capital,unlevered_fcf_m=fcf))
        previous=units
    return rows

def value(rows,wacc,multiple):
    cash_pv=sum(r['unlevered_fcf_m']/1000/(1+wacc)**t for t,r in enumerate(rows,1))
    terminal_pv=rows[-1]['adjusted_ebitda_m']/1000*multiple/(1+wacc)**9
    ev=cash_pv+terminal_pv;equity=ev-net_debt_bn-tra_bn
    return dict(discount_rate=wacc,exit_multiple=multiple,enterprise_value_bn=ev,equity_value_bn=equity,indicative_value_per_share=equity/shares_bn,upside=equity/market_equity_bn-1,terminal_fraction=terminal_pv/ev)
rows=operating()
result=dict(status='Exploratory scenario, not final DCF; see companion note for assumptions and limitations',units='USD millions unless suffix indicates otherwise',annual=rows,valuations=[value(rows,w,m) for w in [.10,.12,.14] for m in [15,20,exit_multiple]],operating_sensitivities={'no_fixed_cost_leverage':value(operating(0),.12,exit_multiple),'gross_profit_500_lower_per_unit':value(operating(.3,500),.12,exit_multiple)},market_inputs=dict(date='2026-10-30',price=price,equity_value_bn=market_equity_bn,enterprise_value_bn=78.29,adjusted_ebitda_2026_guidance_upper_bn=3,net_debt_bn=net_debt_bn,tra_liability_bn=tra_bn,implied_economic_shares_bn=shares_bn))
assert len(rows)==9
assert abs(rows[-1]['retail_units']-2350631.740700982)<1
assert abs(value(rows,.12,exit_multiple)['indicative_value_per_share']-96.2)<.1
(P/'preliminary-dcf-2026-11-01.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(value(rows,.12,exit_multiple),indent=2))
