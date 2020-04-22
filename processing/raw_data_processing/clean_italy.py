import pandas as pd
import numpy as np
import git

repo = git.Repo("./", search_parent_directories=True)
homedir = repo.working_dir
datadir = f"{homedir}/data/international/italy/covid/"

# translate regional file
dfr = pd.read_csv(datadir + "dpc-covid19-ita-regioni.csv")
print(dfr.columns)
dfr.columns = ["Date","Country", "Regional Code", "Region", "Latitude","Longitude","HospitalizedWithSymptoms","IntensiveCare","TotalHospitalized","HomeIsolation","TotalCurrentlyPositive","ChangeTotalPositive","NewCurrentlyPositive","DischargedHealed","Deaths","TotalCases","TestsPerformed","NumberOfPeopleTested","Note_IT","Note_ENG"]
dfr.to_csv(datadir + 'dpc-covid19-ita-regioni.csv', index=False)

# translate provincial file
dfp = pd.read_csv(datadir + "dpc-covid19-ita-province.csv")
dfp.columns = ["Date","Country", "Regional Code", "Region", "Province Code","Province","ProvinceInitials","Latitude","Longitude","TotalCases","Note_IT","Note_ENG"]
dfp.to_csv(datadir + "dpc-covid19-ita-province.csv", index=False)
