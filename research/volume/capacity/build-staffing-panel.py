"""Reproduce the staffing panel from official OSHA downloads; no network access."""
import csv, hashlib, io, json, re, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOWNLOADS = Path('/Users/kwu/Downloads')
FILES = {
    2021: 'ITA-data-cy2021.zip',
    2022: 'ITA-data-cy2022.zip',
    2023: 'ITA_300A_Summary_Data_2023_through_12-31-2024.zip',
    2024: 'ITA_300A_Summary_Data_2024_through_12-31-2025.zip',
    2025: 'ITA_300A_Summary_Data_2025_through_08-31-2026.csv',
}
IDS = ['940853','1010782','1010878','1010912','1010981','1011012',
       '1011025','1011155','1011185','1011274','1012465','1012613','1012681','1012758']
FIELDS = ['id','establishment_id','establishment_name','company_name','street_address',
          'city','state','zip_code','naics_code','industry_description',
          'annual_average_employees','total_hours_worked','year_filing_for']
records, manifest = [], []
for year, filename in FILES.items():
    path = DOWNLOADS / filename
    manifest.append({'year':year,'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                     'url':'https://www.osha.gov/sites/default/'+('largefiles/' if year==2025 else 'files/')+filename})
    if path.suffix == '.zip':
        archive = zipfile.ZipFile(path)
        member = next(n for n in archive.namelist() if n.lower().endswith('.csv'))
        stream = io.TextIOWrapper(archive.open(member), encoding='utf-8-sig')
    else:
        stream = path.open(encoding='utf-8-sig')
    for row in csv.DictReader(stream):
        r = {k.lower():v for k,v in row.items()}
        name = (r.get('company_name','')+' '+r.get('establishment_name','')).lower()
        if 'carvana' not in name and 'adesa' not in name:
            continue
        records.append({'source_year':year, **{k:r.get(k) for k in FIELDS}})
    stream.close()

panel = []
for eid in IDS:
    obs = [r for r in records if r['establishment_id']==eid and r['source_year']>=2022]
    assert sorted(r['source_year'] for r in obs)==[2022,2023,2024,2025], (eid,obs)
    panel.append({'establishment_id':eid,'site':obs[0]['establishment_name'],
                  'observations':obs})
totals = []
for year in range(2022,2026):
    obs = [r for p in panel for r in p['observations'] if r['source_year']==year]
    employees = sum(int(r['annual_average_employees']) for r in obs)
    hours = sum(int(r['total_hours_worked']) for r in obs)
    totals.append({'year':year,'sites':len(obs),'annual_average_employees':employees,
                   'reported_hours':hours,'hours_per_employee':hours/employees})
sensitivities = {}
for label, excluded in {
    'ten_sites_listed_in_2021_10k':['Oklahoma City','San Antonio','Chesterfield','Rocklin'],
    'eight_sites_without_material_street_address_changes':['Tolleson','Indianapolis','Concord','Heath','Blue Mound','Chesterfield']
}.items():
    cohort = [p for p in panel if not any(n in p['site'] for n in excluded)]
    sensitivities[label] = {
        'sites':[p['site'] for p in cohort],
        'employees':{y:sum(int(r['annual_average_employees']) for p in cohort for r in p['observations'] if r['source_year']==y) for y in range(2022,2026)}
    }
output = {'retrieved':'2026-10-30','manifest':manifest,'method':'14 original IRC IDs present in every year 2022–2025; no imputation; annual average employees, not FTE. Source hours unadjusted. Some reporting addresses expand; sensitivity excludes six ambiguous cases.',
          'sensitivities':sensitivities,
          'matched_panel':panel,'matched_totals':totals,'all_name_matches':records}
(ROOT/'staffing-panel-data.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(totals,indent=2))
for p in panel:
    e = [int(r['annual_average_employees']) for r in p['observations']]
    print(p['site'],e,'2023–25',round(100*(e[-1]/e[1]-1),1),'2022–25',round(100*(e[-1]/e[0]-1),1))
print('Matched address variants:')
for p in panel:
    addresses=set((r['street_address'],r['city'],r['state']) for r in p['observations'])
    if len(addresses)>1: print(p['site'],addresses)

# Standalone research figure; no spreadsheet workbook is authored.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig, (ax, bx) = plt.subplots(1,2,figsize=(13,6),gridspec_kw={'width_ratios':[1,1.25]})
years = [t['year'] for t in totals]
values = [t['annual_average_employees'] for t in totals]
ax.plot(years,values,color='#146b8c',marker='o',linewidth=3)
for y,v in zip(years,values): ax.annotate(f'{v:,}',(y,v),xytext=(0,12),textcoords='offset points',ha='center')
ax.set(xticks=years,ylim=(0,8200),title='14 matched IRC establishments',ylabel='Reported annual average employees')
ax.spines[['top','right']].set_visible(False)
ax.grid(axis='y',alpha=.2)
labels = [p['site'].replace('Carvana ','') for p in panel]
before = [int(p['observations'][0]['annual_average_employees']) for p in panel]
after = [int(p['observations'][-1]['annual_average_employees']) for p in panel]
positions = list(range(len(panel)))
bx.barh([i-.18 for i in positions],before,height=.34,color='#b6c2cb',label='2022')
bx.barh([i+.18 for i in positions],after,height=.34,color='#146b8c',label='2025')
bx.set(yticks=positions,yticklabels=labels,xlabel='Reported annual average employees',title='Recovery differs across facilities')
bx.invert_yaxis(); bx.legend(frameon=False,loc='lower right'); bx.spines[['top','right']].set_visible(False)
fig.suptitle('Carvana IRC staffing: recovery within existing facilities',fontsize=17,x=.05,ha='left')
fig.text(.05,.035,'Source: employer-filed OSHA ITA annual summaries. Fixed 14-ID sample, not the whole network.\nAll establishment employees, not technicians alone. Address/scope changes remain a comparability limitation.',fontsize=9,color='#444444')
fig.tight_layout(rect=[0,.11,1,.94],w_pad=3)
fig.savefig(ROOT/'charts'/'staffing-recovery-panel.png',dpi=160)
