import pandas as pd
import numpy as np
import git

repo = git.Repo("./", search_parent_directories=True)
homedir = repo.working_dir
datadir = f"{homedir}/data/us/"

nyt_us_df = pd.read_csv(datadir + 'covid/nyt_us_counties.csv')
print('Processing NYT Data. Expect to wait up to 30 seconds or more.')

# Manually set the FIPS codes for NYC and Guam as the data does 
# not have those set. 
nyt_us_df.loc[nyt_us_df['county'] == 'New York City', 'fips'] = 36061
nyt_us_df.loc[nyt_us_df['state'] == 'Guam', 'fips'] = 66010

# Remove areas with no FIPS codes.
nyt_us_df = nyt_us_df[nyt_us_df['fips'].isna() == False]

nyt_us_df['fips'] = nyt_us_df['fips'].astype(int)
nyt_us_df['date'] = pd.to_datetime(nyt_us_df['date'])
nyt_us_df = nyt_us_df.set_index('fips')
fips_codes = nyt_us_df.index.unique()

def add_missing_date_rows(df, row, low_date, max_date):
    day_delta = np.timedelta64(1,'D')
    day = low_date + day_delta
    while day < max_date:
        copy_row = row.copy()
        copy_row['date'] = day
        df = df.append(copy_row)
        day = day + day_delta
    return df
def process_fips_df(df):
    # Ensures the data is sorted by date.
    df = df.sort_values('date')

    dates = df['date'].values
    for i in range(1, len(dates)):
        # Fill in missing rows with no new cases/deaths, as it appears that these missing days
        # have no new cases/deaths.
        if(dates[i] > dates[i-1]+np.timedelta64(1,'D')):
            return process_fips_df(add_missing_date_rows(df, df.iloc[i], dates[i-1], dates[i]))
    return df

def difference_fips_df(df):
    # Ensures the data is sorted by date.
    df = df.sort_values('date')

    initial_deaths = df['deaths'].values[0]
    initial_cases = df['cases'].values[0]
    new_cases = df['cases'].diff().values
    new_cases[0] = initial_cases
    # Must be clipped as on occasion negative values appear due to bad data.
    df['cases'] = np.clip(new_cases, 0, np.inf)
    new_deaths = df['deaths'].diff().values
    new_deaths[0] = initial_deaths
    # Must be clipped as on occasion negative values appear due to bad data.
    df['deaths'] = np.clip(new_deaths, 0, np.inf)
    return df
df_list = []
for fips in fips_codes:
    df = nyt_us_df.loc[[fips]]
    df = process_fips_df(df)
    df = difference_fips_df(df)
    df_list.append(df)

pd.concat(df_list).to_csv(datadir + 'covid/nyt_us_counties_daily.csv')
