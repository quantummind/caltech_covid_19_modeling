import csv
import pandas as pd
import git
import glob

repo = git.Repo("./", search_parent_directories=True)
homedir = repo.working_dir
datadir = f"{homedir}/data/international/"

# aggregate Our World in Data files
files = glob.glob(datadir + 'health/*.csv') + glob.glob(datadir + 'demographics/*.csv')
# files = ['health/share-of-adults-who-smoke.csv', 'health/share-deaths-heart-disease.csv', 'health/pneumonia-death-rates-age-standardized.csv', 'health/hospital-beds-per-1000-people.csv', 'health/physicians-per-1000-people.csv', 'demographics/median-age.csv']
# keys = ['Estimated prevalence (%)', 'Deaths - Cardiovascular diseases - Sex: Both - Age: All Ages (Percent) (%)', 'Hospital beds (per 1,000 people)', 'Physicians (per 1,000 people)', 'UN Population Division (Median Age) (2017) (years)']
# vals = ['Estimated prevalence of smokers (%)', 'Deaths from Heart Disease (%)', 'Hospital beds (per 1,000 people)', 'Physicians (per 1,000 people)', 'Median Age']

covid_df = pd.read_csv(datadir + 'covid/our_world_in_data/full_data.csv')

for i in range(len(files)):
    f = files[i]
    df = pd.read_csv(f)
    
    # Filter out projections.
    df = df[df['Year'] < 2020]
    # Then pick the most recent year for each country
    most_recent_year = df.groupby(['Entity'])['Year'].max()
    
    # Filter on most recent year. 
    df = df.set_index(['Entity', 'Year'])
    # Create a list of rows to keep.
    df['keep'] = False
    for idx in most_recent_year.index:
        df.loc[(idx, most_recent_year.loc[idx]), 'keep'] = True
    # Reset index and drop rows not marked keep.
    df = df.reset_index()
    df = df[df['keep']].drop(['keep','Year'], axis = 1).rename({'Entity':'location'}, axis = 1)
    # Merge into the Covid data. 
    covid_df = covid_df.merge(df, on = 'location', how = 'left')

# Join country code columns
code_cols = []
code_mapping = {}
for column in covid_df.columns:
    if('Code_' in column):
        code_cols.append(column)
        mapping = covid_df[['location', column]].values
        for i in range(len(mapping)):
            row = mapping[i]
            # If we have not mapped the country to a code, and we have a code
            # then add it to the mapping

            if(row[0] not in code_mapping and isinstance(row[1], str) and len(row[1]) == 3):
                code_mapping[row[0]] = row[1]

covid_df = covid_df.drop(code_cols, axis = 1)
covid_df['country_code'] = covid_df['location'].map(code_mapping)
covid_df.to_csv(datadir + 'aggregated_our_world_in_data.csv', index=False)