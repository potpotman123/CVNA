from pathlib import Path
import json,gzip
import model
P=Path(__file__).parent
# Analytic check: without losses/fees, discounting at the contractual effective yield gives par.
coupon=.1054
a=model.asset_run(0,fee=0,groups=[dict(id=1,balance=100,apr=coupon,original=75,remaining=74)])
y=(1+coupon/12)**12-1
analytic=model.pv([r['asset_cash']+r['admin'] for r in a],y)
assert abs(analytic-100)<1e-8
# Independent observed September distribution arithmetic; USD actual.
begin=983157618.45;end=956172043.53;note_begin=973254059.85;oc=9903558.60
available=35243998.85;strip=begin*.01/12;admin=1000+83.33+2483.35+2750
interest=3327312.97+195100.75+236688.33+121849
priority=note_begin-end;regular=oc;ninterest=50983.15
remaining=available-strip-admin-interest-priority-regular-ninterest
np=remaining*.65;residual=remaining*.35
assert abs(np-2275568.77)<.03 and abs(residual-1225306.26)<.03
roll=begin-137049.07-26441426.44-407099.41-end
assert abs(roll)<.01
rows=json.load(gzip.open(P.parent.parent/'apr-decomposition/2026-p2-rows.json.gz','rt'))
num=sum(float(x['originalLoanAmount'])*float(x['originalInterestRatePercentage']) for x in rows);den=sum(float(x['originalLoanAmount']) for x in rows)
r=json.loads((P/'results.json').read_text());c=r['central'];s=r['sensitivities']
assert s['loss4']['asset_price_at_yield']['0.07']<c['asset_price_at_yield']['0.07']
assert s['fast_attrition']['asset_price_at_yield']['0.07']<c['asset_price_at_yield']['0.07']
assert abs(s['servicing_1pct']['residual_m_at_18_5pct']-c['residual_m_at_18_5pct'])<1e-8
assert s['funding_plus1']['asset_price_at_yield']==c['asset_price_at_yield']
checks={'cohort_count':len(model.coh),'cohort_principal_sum_dollars':sum(x['balance'] for x in model.coh)*model.POOL/100,'analytic_par_check':analytic,'observed_september_rollforward_error_dollars':roll,'observed_september_recomputed_N_principal_dollars':np,'observed_september_recomputed_residual_dollars':residual,'loan_record_count':len(rows),'original_amount_weighted_contract_rate_pct':num/den*100,'original_amount_total_dollars':den,'loan_data_limitation':'Original principal differs from final cutoff balance; does not establish loan-level APR equals contractual interest on every loan. Weighted contract rate rounds to 10.54%, supporting use as proxy. Final prospectus 67 cohorts reconcile exactly to final cutoff pool.','scenario_monotonicity':'pass','waterfall_reserve_ownership_check':'Class N reserve released to depositor, not R; main reserve belongs to R following liabilities. Model tracks separately.','known_model_limits':['Regular monthly timing; no actual closing stub or day count','No optional clean-up call or exact legal acceleration; no modeled note shortfalls in scenarios shown','CNL/default timing calibrated assumptions, not forecast or observed buyer Case 2','First-period cash and APR/rate basis affect exact residual value','No taxes, investor fund leverage, deal hedges, unexpected indemnity or transition costs','No independent corroboration of reported servicer collections']}
(P/'checks.json').write_text(json.dumps(checks,indent=2));print(json.dumps(checks,indent=2))
