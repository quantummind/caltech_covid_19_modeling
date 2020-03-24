#
import pandas as pd
import numpy as np
import requests
from datetime import datetime as dt
from io import StringIO
import os
import us
import git

def clean_df(df, val_name="Cases"):
    """Cleans up dataframe"""

    # convert to longform
    df = df.melt(value_vars=df.columns[4:],id_vars=df.columns[0:4], var_name="Date", value_name=val_name)

    # clean datatypes
    df['Province/State'] = df['Province/State'].astype('string')
    df['Country/Region'] = df['Country/Region'].astype('string')
    df['Date'] = df['Date'].astype('datetime64')
    return df

def tidy_provinces(df):
    """Split complex state/province names (US only so far)"""
    # Clean so DC appears as a single 'state'
    df.loc[df['Province/State'].str.contains('Washington, D.C.'),
           'Province/State'] = 'Washington DC'
    df['City/County'] = pd.Series(np.repeat(pd.NA, len(df)), dtype='string')

    # Select Province/State combinations with a comma
    comma_filter = df['Province/State'].str.contains(',')
    # Extract city or county name
    cities_counties = (df[comma_filter]['Province/State']
                       .apply(lambda string: string.split(',')[0].strip())
                       .astype('string'))
    # Extract state abbreviation and fix as fullname
    states = (df[comma_filter]['Province/State']
              .apply(lambda string: string.split(',')[1].strip())
              .apply(lambda state: us.states.lookup(state).name)
              .astype('string'))
    # Assign into data frame
    df.loc[comma_filter, 'City/County'] = cities_counties
    df.loc[comma_filter, 'Province/State'] = states

    return df[['City/County'] +  df.columns[df.columns != 'City/County'].to_list()]

# Pull data and clean

# urls for data in Johns Hopkins github repository
urls = {'Confirmed' : "https://raw.github.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv",
        'Deaths' : "https://raw.github.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv",
        'Recovered' : "https://raw.github.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv"}

output_dfs = {}

for condition, url in urls.items():
    request = requests.get(url)
    txt = StringIO(request.text)
    df = pd.read_csv(txt)
    output_dfs[condition] = clean_df(df,val_name=condition)

df = (output_dfs['Confirmed']
      .merge(output_dfs['Deaths'])
      .merge(output_dfs['Recovered']))

df = tidy_provinces(df)

# Find home directory for repo
repo = git.Repo("./", search_parent_directories=True)
homedir = repo.working_dir
datadir = f"{homedir}/data/Johns_Hopkins_data/"

# Store new tidy data-frames
df.to_csv(
    f"{datadir}jhu_csse_processed.csv",
    index=False
)
