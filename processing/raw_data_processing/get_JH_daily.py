#%%
import pandas as pd
import numpy as np
import requests
from datetime import datetime as dt
from io import StringIO
import os
import us
import git
from functools import reduce
from datetime import datetime, timedelta, date

#%%
def clean_df(df, date):
    """Cleans up dataframe to get only US counties (i.e. things with FIPS)"""
    df.dropna(subset=['FIPS', 'Admin2'], inplace=True)
    pd.options.mode.chained_assignment = None
    df = df[[df.columns[0]] + list(df.columns[-5:-1])]
    df.loc[:, 'Date'] = date
    return df

# list all dates between two dates
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield (start_date + timedelta(n)).strftime('%m-%d-%Y')

# urls for data in Johns Hopkins github repository
urls = {}

# Note that JHU only started reporting county information from this date
# Which is why we start our query from 3/23/2020
start_date = date(2020, 3, 23)
end_date = date.today()
for d in daterange(start_date, end_date):
    urls[d] = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/" + d + ".csv"

# Initialize dictionary to save output dataframes
output_dfs = {}

# Loop urls
for condition, url in urls.items():
    # Obtain data
    request = requests.get(url)
    # Convert into string
    txt = StringIO(request.text)
    # Convert into dataframe
    df = pd.read_csv(txt)
    # Add to dictionary
    output_dfs[condition] = clean_df(df, condition)


# Find home directory for repo
repo = git.Repo("./", search_parent_directories=True)
homedir = repo.working_dir
datadir = f"{homedir}/data/us/covid/"

dfs = list(output_dfs.values())
dfs = pd.concat(dfs)
dfs.to_csv(
    f"{datadir}JHU_daily_US.csv",
    index=False
)
