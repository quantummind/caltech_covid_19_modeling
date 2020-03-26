import csv
import pandas as pd

link_covid = "https://covid.ourworldindata.org/data/ecdc/full_data.csv"

# Our World In Data makes it difficult to download datasets by script for these, so these must be local. 
dir_smoking = "share-of-adults-who-smoke.csv"
dir_heart = "share-deaths-heart-disease.csv"
dir_hospital_beds_per1000 = "hospital-beds-per-1000-people.csv"
dir_median_age = "median-age.csv" 



covid_df = pd.read_csv(link_covid)
smoking_df = pd.read_csv(dir_smoking).rename(
    {"Estimated prevalence (%)" : "Estimated prevalence of smokers (%)"}, axis = 1
)
heart_df = pd.read_csv(dir_heart).rename(
    {"Deaths - Cardiovascular diseases - Sex: Both - Age: All Ages (Percent) (%)" : "Deaths from Heart Disease (%)"}, axis = 1
)
bed_df = pd.read_csv(dir_hospital_beds_per1000).rename(
    {"Hospital beds (per 1,000 people)": "Hospital beds (per 1,000 people)"}, axis = 1
)
age_df = pd.read_csv(dir_median_age).rename(
    {"UN Population Division (Median Age) (2017) (years)": "Median Age"}, axis = 1
)



auxilary_dfs = [smoking_df, heart_df, bed_df, age_df]
action_cols = ["Estimated prevalence of smokers (%)", "Deaths from Heart Disease (%)", "Hospital beds (per 1,000 people)", "Median Age"]


for df in auxilary_dfs:
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
covid_df.to_csv('our_world_in_data.csv', index=False)