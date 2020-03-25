# International data

Data should be standardized with ISO codes. **If you add data, update both this README and the README in that directory!**


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


## `policies`

So far, these datasets are very new and it is unclear what future filenames will be. Once we know consistent formats, scripts to add ISO codes and regularly refresh the download. These datasets provide some aggregation of common policies governments undertake and the dates at which those policies occurred.

Summary:
* `international.csv`: Last updated March 23. Puts together all the measures implemented by governments worldwide in response to the Coronavirus pandemic, assembled by ACAPS (non-profit). The researched information available falls into five categories: social distancing, movement restrictions, public health measures, social and economic measures, human rights implications. https://data.humdata.org/dataset/acaps-covid19-government-measures-dataset
* `regional.csv`: Last updated March 25. Crowdsourced but curated by The Machine Learning for Social Science Lab, Center for Peace and Security Studies, University of California San Diego. https://github.com/rexdouglass/TIGR/tree/master/data_out

Compield by quantummind