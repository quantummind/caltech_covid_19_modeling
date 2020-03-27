import numpy as np
import pandas as pd
import git
repo = git.Repo("./", search_parent_directories=True)
homedir = repo.working_dir

# Fetch Corona Data Scraper dataset consisting of
# geolocation/population/testing/active case info
df = pd.read_csv(f"{homedir}/data/international/covid/corona_data_scraper/geopop.csv", parse_dates=['date'])


# the source DataFrame includes three-letter country codes, and separate city, county, state and country fields.
# Combine these into one, with the full country name to make them easy to use
country_code_type = 'alpha-3'
country_codes = pd.read_csv(f"{homedir}/data/international/countries_regional_codes.csv").set_index(country_code_type)['name']
country_codes.name = 'country'

# Override a few names that are too long or awkward
# Note this only changes the pretty printing display name, not the code itself!
country_codes.update(pd.Series({
    'USA': 'USA',
    'GBR': 'UK',
    'KOR': 'South Korea',
}))

# Create a new visual location column that
# lists City/County/State/Country for each row if available
# For plotting and other visual analysis
def get_combined_location(row):
    location_segments = [
        row['city'], row['county'], row['state'], row['country']
    ]
    cleaned_location_segments = [
        segment
        for segment in location_segments
        if type(segment) is str
    ]
    return ', '.join(cleaned_location_segments)

# Join country code column with existing dataset
cleaned_timeseries = (
    df
    .rename(
        {
            'country': 'country_code'
        },
        axis='columns'
    )
    .join(country_codes, 'country_code')
)
# Join visual/pretty plot 'location' column with existing dataset
cleaned_timeseries['location'] = cleaned_timeseries.apply(get_combined_location, axis='columns')

cleaned_timeseries.to_csv(f"{homedir}/data/international/covid/corona_data_scraper/geopop.csv", index=False)

print("Cleaned Corona Data Scraper Data")
