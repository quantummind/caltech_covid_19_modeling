# International data

Data should be standardized with ISO codes. **If you add data, update both this README and the README in that directory!**

`aggregated_our_world_in_data.csv` collects all relevant data from Our World in Data (compiled by quantummind and thohoff).

`countries_regional_codes.csv` gives a mapping between country names and their respective alpha and numeric country codes. Standard protocol is to use `alpha-3` as the key (i.e United States of America -> USA). Source: https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes. 

## `covid`

### `corona_data_scraper`

`geopop.csv` is a very comprehensive file! Contains latitude and longitude coordinates as well as international and state populations (in US), in to a running tally by day of number of total cases, number of deaths, number of recovered patients, number of active cases, number of tested cases, growthFactor in total cases from last day's number, in addition to the source for each item. Note that the `geopop.csv` dataset is awaiting to get new county information (for US states). This dataset will get refreshed daily using the daily refresh scripts, and we will update this page once the data is updated.
**EDIT: County data is starting to come in. It is not complete, but it does have geolocation coordinates for all US counties!!! `geopop.csv` should primarily be used for geolocation first and then as it is refreshed county data should become more robust**
Source: https://coronadatascraper.com/#home. This site is very robust, tracking daily updates in active and recovered cases as well as tested cases. It also binds this data with geolocation and population data as well. I'd (@connorsoohoo) highly suggest you check out the website.

Compiled by Connor Soohoo (connorsoohoo@gmail.com)

### `Johns_Hopkins_data`
These data are pulled from the [JHY CSSE github repo](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data) and updated regularly. They are reformatted for one observation per line, with the following columns:

- **City/County**: Where provided (mostly the US), the highest geographical resolution
- **Province/State**: Non-abbreviated province or state listing, where provided.
- **Country/Region**: Currently uses JHU provided country names until a canonical list can be declared
- **Lat**: JHU provided latitude of geographic center of region
- **Long**: JHU provided longitude of geographic center of region
- **Date**: Date of observation, as YYYY-MM-DD
- **Confirmed**: No. of cumulative confirmed cases for the region on date of observation
- **Deaths**: No. of cumulative deaths for the region on date of observation

Compiled by Manuel, Zara, and Boris

### `our_world_in_data`

`full_data.csv` contains data from the ECDC scraped from https://ourworldindata.org/coronavirus.

Compiled by thohoff


## `demographics`

Country-level 1960-now demographic data on age.

Source: UN Population Division, scraped from https://ourworldindata.org/age-structure.
Summary:
* `age-dependency-ratio-old.csv`: ratio of people over 64 to people 15-64 years
* `age-dependency-ratio-young-of-working-age-population.csv`: ratio of people under 15 to people 15-64 years
* `median-age.csv`: median age
* `share-of-the-population-that-is-70-years-and-older.csv`: population >=70 years old

Compiled by quantummind


## `health`

Country-level 1960-now data of conditions related to COVID-19 deaths and hospitals.

Source: World Bank, Global Burden of Disease Study 2017.
Summary:
* `hospital-beds-per-1000-people.csv`: hospital beds per 1000 people. https://ourworldindata.org/coronavirus
* `physicians-per-1000-people.csv`: physicians per 1000 people. https://ourworldindata.org/coronavirus
* `pneumonia-death-rates-age-standardized.csv`: pneumonia death rates per 100,000 individuals. https://ourworldindata.org/pneumonia
* `share-deaths-heart-disease.csv`: share of deaths caused by heart disease. https://ourworldindata.org/grapher/share-deaths-heart-disease
* `share-of-adults-who-smoke.csv`: share of adults who smoke. https://ourworldindata.org/smoking

Compiled by quantummind


## `italy`

Italian case study, so far only COVID-19 data from the Italian government. The daily refresh script updates and translates it from https://github.com/pcm-dpc/COVID-19.

## `policies`

So far, these datasets are very new and it is unclear what future filenames will be. Once we know consistent formats, scripts to add ISO codes and regularly refresh the download. These datasets provide some aggregation of common policies governments undertake and the dates at which those policies occurred.

Summary:
* `international.csv`: Last updated March 23. Puts together all the measures implemented by governments worldwide in response to the Coronavirus pandemic, assembled by ACAPS (non-profit). The researched information available falls into five categories: social distancing, movement restrictions, public health measures, social and economic measures, human rights implications. https://data.humdata.org/dataset/acaps-covid19-government-measures-dataset
* `regional.csv`: Last updated March 25. Crowdsourced but curated by The Machine Learning for Social Science Lab, Center for Peace and Security Studies, University of California San Diego. https://github.com/rexdouglass/TIGR/tree/master/data_out

Compiled by quantummind
