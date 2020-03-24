#%%
import pandas as pd
import numpy as np
import requests
from datetime import datetime as dt
from io import StringIO
import os
import git

# Find home directory for repo
repo = git.Repo("./", search_parent_directories=True)
homedir = repo.working_dir

#%%
# # Define function to
# def join_province_country(df):
#     """Join country/region column and province/state column."""
#     my_list = df["Country/Region"].view(dtype='object')
#     for i in range(len(df)):
#         if not pd.isna(df.iloc[i]["Province/State"]):
#             my_list[i] = df.iloc[i]["Country/Region"]+ " ({})".format(df.iloc[i]["Province/State"])
            
#     df["Country/Region"] = my_list
#     return df.drop(columns="Province/State")

#%%
# urls for data in Johns Hopkins github repository
# These links belong to the time-series data.
# CONFIRMED CASES
url_con = "https://raw.github.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"
# DEATHS
url_dea = "https://raw.github.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv"
# RECOVERED CASES
url_rec = "https://raw.github.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv"

#%%
# Get data
r_con = requests.get(url_con)
r_dea = requests.get(url_dea)
r_rec = requests.get(url_rec)

# Read data from request
t_con = StringIO(r_con.text)
t_dea = StringIO(r_dea.text)
t_rec = StringIO(r_rec.text)
# Convert into Pandas Dataframe
df_con = pd.read_csv(t_con)
df_dea = pd.read_csv(t_dea)
df_rec = pd.read_csv(t_rec)

#%%
# # Join province and country
# df_con = join_province_country(df_con)
# df_dea = join_province_country(df_dea)
# df_rec = join_province_country(df_rec)

#%%
# Define function to find dates in column names
def find_date_cols(df):
    '''
    Function to find which column names of the dataframe contain dates.
    Parameters
    ----------
    df : pandas Dataframe
        Dataframe of time series form the Jonhs Hopkins website
    Returns
    -------
    date_bool : array-like
        Boolean array indicating if a column contains a date or not
    '''
    # Count number of slashes in each column name
    slash_num = [x.count('/') for x in df.columns]
    # Return boolean array of all column names with == 2 slashes
    return np.equal(slash_num, 2)


#%%

# Make tidy data frame (one observation per column)
df_con_melt = df_con.melt(
    value_vars=df_con.loc[:, find_date_cols(df_con)],
    id_vars=df_con.columns[~find_date_cols(df_con)],
    var_name="date",
    value_name="cases"
)
df_dea_melt = df_dea.melt(
    value_vars=df_dea.loc[:, find_date_cols(df_dea)],
    id_vars=df_dea.columns[~find_date_cols(df_dea)],
    var_name="date",
    value_name="cases"
)
df_rec_melt = df_rec.melt(
    value_vars=df_rec.loc[:, find_date_cols(df_rec)],
    id_vars=df_rec.columns[~find_date_cols(df_rec)],
    var_name="date",
    value_name="cases"
)
#%%
# Locate directory where to save data
# NOTE: gitpython module allows for global paths within the repo
datadir = f"{homedir}/data/Johns_Hopkins_data/time_series"

# Store new tidy data-frames
df_con.to_csv(
    f"{datadir}time_series_19-covid-Confirmed_processed.csv",
    index=False
)
df_dea.to_csv(
    f"{datadir}time_series_19-covid-Deaths_processed.csv",
    index=False
)
df_rec.to_csv(
    f"{datadir}time_series_19-covid-Recovered_processed.csv", 
    index=False
)