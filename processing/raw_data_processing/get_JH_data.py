#%%
import pandas as pd
import numpy as np
import requests
from datetime import datetime as dt
from io import StringIO
import os
import us
import git

#%%
def clean_df(df, val_name="Cases"):
    """Cleans up dataframe"""
    # convert to longform
    df = df.melt(
        value_vars=df.columns[4:],
        id_vars=df.columns[0:4],
        var_name="Date",
        value_name=val_name
    )

    # clean datatypes
    df['Province/State'] = df['Province/State'].astype('string')
    df['Country/Region'] = df['Country/Region'].astype('string')
    for i in range(len(df['Date'])):
        row = df['Date'][i]
        if '202' in row:
            df['Date'][i] = row.replace('202', '20') # they had 3/21/202 instead of 3/21/20 in their dataset
    df['Date'] = df['Date'].astype('datetime64')

    return df

# def tidy_provinces(df):
#     """Split complex state/province names (US only so far)"""
#     # Clean so DC appears as a single 'state'
#     df.loc[df['Province/State'].str.contains('Washington, D.C.'),
#            'Province/State'] = 'Washington DC'
#     df['City/County'] = pd.Series(np.repeat(pd.NA, len(df)), dtype='string')

#     # Select Province/State combinations with a comma
#     comma_filter = df['Province/State'].str.contains(',')
#     # Extract city or county name
#     cities_counties = (df[comma_filter]['Province/State']
#                        .apply(lambda string: string.split(',')[0].strip())
#                        .astype('string'))
#     # Extract state abbreviation and fix as fullname
#     states = (df[comma_filter]['Province/State']
#               .apply(lambda string: string.split(',')[1].strip())
#               .apply(lambda state: us.states.lookup(state).name)
#               .astype('string'))
#     # Assign into data frame
#     df.loc[comma_filter, 'City/County'] = cities_counties
#     df.loc[comma_filter, 'Province/State'] = states

#     return df[['City/County'] +  df.columns[df.columns != 'City/County'].to_list()]

#%%
# Pull data and clean

# urls for data in Johns Hopkins github repository
urls = {'Confirmed' : "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv",
        'Deaths' : "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv",
}

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
    output_dfs[condition] = clean_df(df, val_name=condition)

# Merge dataframes into single one
df = (output_dfs['Confirmed']
      .merge(output_dfs['Deaths'])
    )

# Find home directory for repo
repo = git.Repo("./", search_parent_directories=True)
homedir = repo.working_dir
datadir = f"{homedir}/data/international/covid/Johns_Hopkins_data/"

# Store new tidy data-frames
df.to_csv(
    f"{datadir}jhu_csse_processed.csv",
    index=False
)