# Geolocation and Population Data

**Note: `geopop.csv` is a very comprehensive file!  Contains latitude and longitude coordinates as well as international and state populations (in US), in to a running tally by day of number of total cases, number of deaths, number of recovered patients, number of active cases, number of tested cases, growthFactor in total cases from last day's number,  in addition to the source for each item.**

Note that the `geopop.csv` dataset is awaiting to get new county information (for US states). This dataset will get refreshed daily using the daily refresh scripts, and we will update this  page once the data is updated.

This data comes from the Corona Data Scraper, which you can access here:  https://coronadatascraper.com/#home. This site is very robust, tracking daily updates in active and recovered cases as well as tested cases. It also binds this data with geolocation and population data as well. I'd (@connorsoohoo) highly suggest you check out the website.

Note that `county_pops.csv` is a duplicate of `icu_county.csv` in `us` subfolder. Contains number of hospitals and ICU beds for all counties in the US. **Also contains each county's total population and population over 60.** Use this for county population information in the meantime.

Compiled by Connor Soohoo (connorsoohoo@gmail.com)
