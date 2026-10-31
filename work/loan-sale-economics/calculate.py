"""Reproduce disclosed-amount bridges and explicitly hypothetical sensitivities.

All company amounts are USD millions. Channel principal is rounded in filings.
Residuals reconcile disclosed numbers, not independent purchase-price valuation.
"""
from pathlib import Path
import json

periods = {
    'FY2023': dict(ally=3600, securitization=2800, fixed_pool=0,
                   gain=434, cash_proceeds=6594, retained_received=194, ebitda=339),
    'FY2024': dict(ally=3000, securitization=3800, fixed_pool=1500,
                   gain=755, cash_proceeds=8805, retained_received=272, ebitda=1378),
    'FY2025': dict(ally=4700, securitization=3500, fixed_pool=4200,
                   gain=1193, cash_proceeds=13315, retained_received=240, ebitda=2237),
    '9M2025': dict(ally=3200, securitization=2600, fixed_pool=3100,
                   gain=878, cash_proceeds=9583, retained_received=173, ebitda=1726),
    '9M2026': dict(ally=5700, securitization=3700, fixed_pool=4500,
                   gain=1084, cash_proceeds=14722, retained_received=266, ebitda=2241),
    'Q3_2025': dict(ally=1200, securitization=1000, fixed_pool=1100, gain=331, ebitda=637),
    'Q3_2026': dict(ally=2000, securitization=1550, fixed_pool=1600, gain=381, ebitda=800),
}
for p in periods.values():
    p['principal_total'] = p['ally'] + p['securitization'] + p['fixed_pool']
    p['gain_per_principal_pct'] = 100 * p['gain'] / p['principal_total']
    p['gain_divided_by_total_ebitda_pct_not_segment_contribution'] = 100*p['gain']/p['ebitda']
    p['fixed_pool_share_pct'] = 100*p['fixed_pool']/p['principal_total']
    if 'cash_proceeds' in p:
        p['cash_minus_rounded_principal'] = p['cash_proceeds']-p['principal_total']
        p['cash_above_rounded_principal_pct'] = 100*p['cash_minus_rounded_principal']/p['principal_total']
        p['retained_received_per_principal_pct'] = 100*p['retained_received']/p['principal_total']
        p['unallocated_bridge_residual'] = p['gain']-p['cash_minus_rounded_principal']-p['retained_received']
        p['gain_minus_all_new_retained_fv_stress_not_cash_profit'] = p['gain']-p['retained_received']

def price_scenarios(p):
    return {channel: {str(points)+'pt': p[channel]*points/100 for points in (1,2,3)}
            for channel in ('principal_total','ally','securitization','fixed_pool')}

old,new = periods['9M2025'],periods['9M2026']
rate_change = new['gain']/new['principal_total']-old['gain']/old['principal_total']
volume_effect = (new['principal_total']-old['principal_total'])*old['gain']/old['principal_total']
rate_mix_effect = new['principal_total']*rate_change
assert abs(volume_effect+rate_mix_effect-(new['gain']-old['gain'])) < 1e-9

offered_faces = [116166000,307325000,307325000,202701000,42854000,46521000,22477000]
offered_net_prices = [99.75,99.74605,99.73692,99.74533,99.74014,99.71028,99.70572]
net_proceeds = sum(f*p/100 for f,p in zip(offered_faces,offered_net_prices))
assert abs(net_proceeds-1042661118) < 1
p2pool=1100395400.20
retention_2025 = 464+240-217+12-13
retention_9m2026 = 486+266-178+12-29
assert retention_2025 == 486 and retention_9m2026 == 557

output = {
    'units':'USD millions except transaction dollar amounts and percentages',
    'caveats':[
        'Loan gains/principal are blended realization ratios, not matched-loan bid prices or buyer returns.',
        'Cash proceeds minus rounded principal is an aggregate cash-premium proxy; accrued interest, timing, capitalized origination costs, prior allowances, other consideration and rounding are not separately allocated.',
        'Cash plus initial retained FV minus gain implies a net basis residual; it does not independently prove carrying values or fair prices.',
        'Loan gains/EBITDA is scale only; origination/funding/servicing/overhead allocation is not a segment contribution bridge.',
        'Sensitivity assumes same volume, carrying basis, costs and other consideration; it is not an estimate of subsidy.',
        'ABS note proceeds are not the whole-loan purchase price. Private N/XS/certificate sale prices and retained allocation remain unknown.',
    ],
    'periods':periods,
    '9m_yoy':{
        'principal_growth_pct':100*(new['principal_total']/old['principal_total']-1),
        'gain_growth_pct':100*(new['gain']/old['gain']-1),
        'blended_gain_ratio_change_bps':10000*rate_change,
        'volume_effect_at_old_ratio':volume_effect,
        'ratio_mix_effect_at_new_volume_not_proven_repricing':rate_mix_effect,
    },
    'hypothetical_price_reductions':{k:price_scenarios(periods[k]) for k in ['FY2025','9M2026']},
    'FY2025_price_points_needed_for_100_200m':{
        c:{str(a)+'m':100*a/periods['FY2025'][c] for a in (100,200)}
        for c in ['principal_total','fixed_pool']},
    'retained_fv_rollforwards':{'FY2025':retention_2025,'9M2026':retention_9m2026},
    '9m2026_receivables_balance_crosscheck':{
        'opening_net_receivables':813,
        'originations':14187,
        'implied_net_sale_basis_cash_plus_retained_minus_gain':14722+266-1084,
        'principal_collections':201,
        'derived_closing_before_unallocated_changes':813+14187-(14722+266-1084)-201,
        'reported_closing_net_receivables':896,
        'difference_rounding_and_unallocated_changes':1,
        'caveat':'Accounting consistency check only, not independent price validation.',
    },
    'hypothetical_20pct_lower_initial_retained_fv':{'FY2025':48,'9M2026':53.2},
    'cvna_2026_p2':{
        'pool_principal_dollars':p2pool,
        'publicly_offered_note_face_dollars':sum(offered_faces),
        'net_underwriting_proceeds_computed_dollars':net_proceeds,
        'net_underwriting_proceeds_disclosed_dollars':1042661118,
        'net_note_proceeds_divided_by_pool_principal_pct':100*net_proceeds/p2pool,
        'estimated_expenses_excluded_dollars':1000000,
        'reserve_account_dollars':5501977,
        'class_N_reserve_dollars':2750988.50,
        'private_N_XS_certificate_proceeds_and_retained_fv':'unknown',
    },
    'blast_2026_2':{
        'pool_principal_dollars':759931706.70,
        'affiliated_acquisition_share_pct':7.97,
        'derived_affiliated_slice_dollars_approx':759931706.70*0.0797,
        'management_estimated_notes_and_certificates_fv_dollars':735437922,
        'management_estimated_certificate_fv_dollars':93297922,
        'management_assumed_residual_discount_pct':16,
        'management_assumed_cnl_pct':27.70,
        'management_assumed_monthly_ABS_prepayment_pct':0.60,
        'caveat':'Management pool valuation for risk retention; not a price paid Carvana or a realized equity return. The acquired slice is not traced to Carvana.',
    },
    'gofi_2024':{
        'reported_sold_balance_dollars':167553902,
        'gain_dollars':7185702,
        'derived_proceeds_dollars':167553902+7185702,
        'gain_over_reported_balance_pct':100*7185702/167553902,
        'caveat':'GoFi resale to affiliated BAC, not CVNA sale. Sold-balance FV rollforward basis is not independently established as par.',
    },
}
Path(__file__).with_name('calculations.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({'9m_yoy':output['9m_yoy'],'FY2025':periods['FY2025'],
                  '9M2026':periods['9M2026'],'P2':output['cvna_2026_p2']},indent=2))
