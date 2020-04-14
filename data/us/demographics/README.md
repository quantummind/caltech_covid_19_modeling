## Demographics data

This includes age/gender, education, and economic information of the US population at the county level, and aggregated populations at the state level.

Summary:
* `acs_2018.csv`: Number of households, age and ethnicity breakdowns. American Community Survey (ACS) 2018, US Census Bureau (data.census.gov).
* `county_populations.csv`: Total population and population over the age of 60 per county from the 2017 American Community Survey. Data dictionary and more details available at. https://khn.org/wp-content/uploads/sites/2/2020/03/KHN_ICU_bed_county_analysis.zip
* `county_land_areas.csv`: Total area, population per sq mile, and households per sq mile for each county from the 2010 census. https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?src=bkmk
* `countypres_2000-2016.csv`: Number of votes for each presidential candidate by county for the 2000 - 2016 presidential elections. https://dataverse.harvard.edu/dataset.xhtml;jsessionid=49aac8aa6c3b5b267543f901b568?persistentId=doi:10.7910/DVN/VOQCHQ
* `education.csv`: Education level per county. https://www.ers.usda.gov/data-products/county-level-data-sets/download-data/
* `households.csv.zip` (compressed): Household data from the ACS 2018 survey (5% of households in the US). `multigeneration_code` indicates the number of generations in a household: 00 is n/a, 10 is 1 generation, 20 is 1-2 generations, 21 is 2 adjacent generations (all younger generation are <17), 22 is 2 adjacent generations (some in the younger generation are >17), 23 is 2 non adjacent generations, 31 and 32 are 3+ generations. `sample_weight` is the number of households in the general US that are represented by a given household. 2018 5-year American Community Survey.
* `poverty.csv`: Urbanization and poverty rates per county, columns described in `poverty-key.txt`. https://www.ers.usda.gov/data-products/county-level-data-sets/download-data/
* `state_populations.csv`: Statewide populations from the corona data scraper. https://coronadatascraper.com/#sources
* `unemployment.csv`: Urbanization, metro areas, unemployment, and income per county. https://www.ers.usda.gov/data-products/county-level-data-sets/download-data/

Compiled by quantummind, alexcdot