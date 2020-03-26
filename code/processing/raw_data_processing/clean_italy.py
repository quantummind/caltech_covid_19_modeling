import pandas as pd
import numpy as np
import glob
import git

repo = git.Repo("./", search_parent_directories=True)
homedir = repo.working_dir
datadir = f"{homedir}/data/international/italy/COVID-19/"

# translate regional files and save in separate folder
sets_reg = []
files_reg = sorted(glob.glob(datadir + 'dati-regioni/dpc-covid19-ita-regioni-2*.csv'))
for i in range(len(files_reg)):
    dfr = pd.read_csv(files_reg[i],)
    dfr.columns = ["Date","Country", "Regional Code", "Region", "Latitude","Longitude","HospitalizedWithSymptoms","IntensiveCare","TotalHospitalized","HomeIsolation","TotalCurrentlyPositive","NewCurrentlyPositive","DischargedHealed","Deaths","TotalCases","Tested","Note_IT","Note_ENG"]
    sets_reg.append(dfr)
    dfr.to_csv(datadir + 'dati-regioni-en/' + files_reg[i][files_reg[i].rfind('/'):], index=False)
    
# translate provincial files and save in separate folder
sets_prov = []
files_prov = sorted(glob.glob(datadir + 'dati-province/dpc-covid19-ita-province-2*.csv'))
for i in range(len(files_reg)):
    dfp = pd.read_csv(files_prov[i])
    dfp.columns = ["Date","Country", "Regional Code", "Region", "Province Code,","Province","ProvinceInitials","Latitude","Longitude","TotalCases","Note_IT","Note_ENG"]
    sets_prov.append(dfp)
    indDrop = dfp[dfp['Latitude'] == 0].index
    dfp.drop(indDrop, inplace=True)
    dfp.to_csv(datadir + 'dati-province-en/' + files_prov[i][files_prov[i].rfind('/'):], index=False)
    
# compile all regional data into one timeseries of cases by region
comp_reg = sets_reg[0][["Country", "Regional Code", "Region", "Latitude","Longitude"]]
for i in range(len(files_reg)):
    time = sets_reg[i]['Date'][0]
    time = time[:time.find('T')]
    time = time.replace("-", "")
    headers = ["HospitalizedWithSymptoms","IntensiveCare","TotalHospitalized","HomeIsolation","TotalCurrentlyPositive","NewCurrentlyPositive","DischargedHealed","Deaths","TotalCases","Tested"]
    for h in range(len(headers)):
        comp_reg[time+headers[h]] = sets_reg[i][headers[h]]
comp_reg.to_csv(datadir + 'dati-regioni-en/dpc-covid19-ita-regioni-total.csv', index=False)

# compile all province data into one timeseries of cases by province
comp_prov = sets_prov[0][["Country","Regional Code", "Region", "Province Code,","Province","ProvinceInitials","Latitude","Longitude"]]
for i in range(len(files_reg)):
    time = sets_prov[i]['Date'][0]
    time = time[:time.find('T')]
    time = time.replace("-", "")
    comp_prov[time+'Cases'] = sets_prov[i]['TotalCases']
comp_prov.to_csv(datadir + 'dati-province-en/dpc-covid19-ita-province-total.csv', index=False)