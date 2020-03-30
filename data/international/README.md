# International data

## Getting started
If you are beginning international data analysis, an excellent place to start is `aggregated_our_world_in_data.csv`, which includes COVID-19 data per country and helpful related variables (demographics, health, etc.) all cleaned and organized with ISO variables.

If you are beginning a case study of a country that faced the pandemic earlier than the U.S., a good place to start is `italy/covid-regions.csv` for region-level COVID-19 data and `italy/aggregate_italy.csv` for related demographic, economic, and health variables.

Summary:
* `aggregated_our_world_in_data.csv` collects all relevant data from Our World in Data (compiled by quantummind and thohoff).
* `countries_regional_codes.csv` gives a mapping between country names and their respective alpha and numeric country codes. Standard protocol is to use `alpha-3` as the key (i.e United States of America -> USA). Source: https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes. 


## `covid`

### `corona_data_scraper`

`geopop.csv` is a very comprehensive file! Contains latitude and longitude coordinates as well as international and state populations (in US), in to a running tally by day of number of total cases, number of deaths, number of recovered patients, number of active cases, number of tested cases, growthFactor in total cases from last day's number, in addition to the source for each item. Note that the `geopop.csv` dataset is awaiting to get new county information (for US states). This dataset will get refreshed daily using the daily refresh scripts, and we will update this page once the data is updated.
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

Italian case study at the regional level. The daily refresh script updates `COVID-19` and translates it from https://github.com/pcm-dpc/COVID-19.

Summary:
* `aggregate_italy.csv`: Everything except COVID: health, demographics, doctors, and more.
* `covid/dpc-covid19-ita-province.csv`: COVID-19 cases, deaths, testing, etc. at the province level (smaller than region).
* `covid/dpc-covid19-ita-regioni.csv`: COVID-19 cases, deaths, testing, etc. at the region level (larger than province).
* `demographics/region-populations.csv`: Population data.

Sources of demographics and aggregate data: http://dati-censimentopopolazione.istat.it/Index.aspx?lang=en, https://www.istat.it/en/health-statistics?data-and-indicators, https://www.istat.it/en/archivio/16271

Compiled by quantummind


## `policies`

So far, these datasets are very new and it is unclear what future filenames will be. Once we know consistent formats, scripts to add ISO codes and regularly refresh the download. These datasets provide some aggregation of common policies governments undertake and the dates at which those policies occurred.

Summary:
* `international.csv`: Last updated March 23. Puts together all the measures implemented by governments worldwide in response to the Coronavirus pandemic, assembled by ACAPS (non-profit). The researched information available falls into five categories: social distancing, movement restrictions, public health measures, social and economic measures, human rights implications. https://data.humdata.org/dataset/acaps-covid19-government-measures-dataset
* `regional.csv`: Last updated March 25. Crowdsourced but curated by The Machine Learning for Social Science Lab, Center for Peace and Security Studies, University of California San Diego. https://github.com/rexdouglass/TIGR/tree/master/data_out

Compiled by quantummind


## `sk`

Data pulled directly from [Kaggle DS4C South Korea](https://www.kaggle.com/kimjihoo/coronavirusdataset/metadata) dataset.