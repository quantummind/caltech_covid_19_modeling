# US data

US datasets are (usually) encoded with a column named "FIPS" denoting the county code. Translations to county names are in `processing_data/fips_key.csv`.

## Getting started

For the most curated dataset of COVID-19 cases, see `covid/nyt_us_counties.csv`. Additional variables can be merged in from the appropriate subdirectories, but we also provide useful aggregate datasets of relevant variables (demographics, health, etc.) in `aggregate_berkeley.csv` and `aggregate_jhu.csv`.

Summary:
* `aggregate_berkeley.csv`: Demographic, health, and other information compiled by Bin Yu's group at UC Berkeley. A few columns are selected from a few thousand by feature selection done by Berkeley. The full dataset includes data on number of icu beds and hospitals per county prevalance of chronic diseases, number of total deaths (from any cause), mortality rate from respiratory diseases, voting history, and impact from smoking at the county level. You can download full dataset: `df_county_level_cached.csv` file at https://drive.google.com/open?id=1EHqZxbTVPO5RDxDvJntZMNBjhxGeE2bU. You can regenerate the full dataset and view the original sources at https://github.com/Yu-Group/covid-19-ventilator-demand-prediction.
* `aggregate_jhu.csv`: Demographic, health, and other information compiled by Johns Hopkins University. https://github.com/JieYingWu/COVID-19_US_County-level_Summaries

## `covid`

County-level from USAFacts (aggregated from the CDC, state- and local-level public health agencies, and academic institutions), which is claimed to have been confirmed with individual counties. County-level data from JHU.

Summary:
* `cdc_all_deaths.csv`: Recent mortality due to COVID-19 and due to all causes, grouped by state, age, and place of death. https://data.cdc.gov/NCHS/Provisional-Death-Counts-for-Coronavirus-Disease-C/hc4f-j6nb
* `confirmed_cases.csv`: Confirmed COVID cases per county, USAFacts. https://static.usafacts.org/public/data/covid-19/
* `daily_state_tests.csv`: COVID-19 positive and negative test counts per state from the [COVID-19 Tracking project](https://covidtracking.com/) http://covidtracking.com/api/states/daily.csv
* `deaths.csv`: Confirmed COVID deaths per county, USAFacts. https://static.usafacts.org/public/data/covid-19/
* `JHU_daily_US.csv`: COVID-19 case and death counts per county from JHU, merged from daily updates since 3/23/2020. https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data
* `daily_state_tests.csv`: COVID-19 positive and negative test counts per state from the [COVID-19 Tracking project](https://covidtracking.com/) http://covidtracking.com/api/states/daily.csv
* `nyt_us_states.csv` : Time series data on confirmed cases and deaths of COVID-19 at the state level in the US reported by the New York Times. [github link](https://github.com/nytimes/covid-19-data)
* `nyt_us_counties.csv` : Time series data on confirmed cases and deaths of COVID-19 at the county level in the US reported by the New York Times. [github link](https://github.com/nytimes/covid-19-data)

Compiled by quantummind, Alex Cui (alexcdot)

## `demographics`

This includes age/gender, education, and economic information of the US population at the county level, and aggregated populations at the state level.

Summary:
* `acs_2018.csv`: Number of households, age and ethnicity breakdowns. American Community Survey (ACS) 2018, US Census Bureau (data.census.gov).
* `county_populations.csv`: Total population and population over the age of 60 per county from the 2017 American Community Survey. Data dictionary and more details available at. https://khn.org/wp-content/uploads/sites/2/2020/03/KHN_ICU_bed_county_analysis.zip
* `county_land_areas.csv`: Total area, population per sq mile, and households per sq mile for each county from the 2010 census. https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?src=bkmk
* `countypres_2000-2016.csv`: Number of votes for each presidential candidate by county for the 2000 - 2016 presidential elections. https://dataverse.harvard.edu/dataset.xhtml;jsessionid=49aac8aa6c3b5b267543f901b568?persistentId=doi:10.7910/DVN/VOQCHQ
* `education.csv`: Education level per county. https://www.ers.usda.gov/data-products/county-level-data-sets/download-data/
* `households.csv.zip` (compressed): Household data from the ACS 2018 survey (5% of households in the US) showing the number of generations in a household. 2018 5-year American Community Survey.
* `poverty.csv`: Urbanization and poverty rates per county, columns described in `poverty-key.txt`. https://www.ers.usda.gov/data-products/county-level-data-sets/download-data/
* `state_populations.csv`: Statewide populations from the corona data scraper. https://coronadatascraper.com/#sources
* `unemployment.csv`: Urbanization, metro areas, unemployment, and income per county. https://www.ers.usda.gov/data-products/county-level-data-sets/download-data/

Compiled by quantummind

## `flu`

Statewide and national flu cases and deaths, as well as region/county-level data for CA and NY.

Summary:
* `ILI_Ages.csv`: Percentage of visits for Influenza-Like-Illness (ILI) reported by Sentinal Providers, for the past 23 years from 1997 up to 2020. Patients with ILI are also grouped by age range.
* `WHO_cases_age_groupings_virus_strains.csv`: Influenza cases grouped by age range and by virus strain. Details on virus strains given below. **Useful for looking at spread of H1N1**
* `WHO_NREVSS_Clinical_Labs.csv`:  Gives number of specimens tested per week and number and percent of specimens that tested positive for Influenza A and B, respectively. Only from 2015 - 2020. Note that beginning for the 2015-16 season, reports from public health and clinical laboratories are presented separately in the weekly influenza update.
* `WHO_NREVSS_Combined_prior_to_2015_16.csv`: 1997 - 2015 data. Gives number of specimens tested per week and number and percent of specimens that tested positive for Influenza A and B, respectively. Also differentiates based on strain. Combined data from public health and clinical labs.  **Very comprehensive, Useful for looking at spread of H1N1 (2009)**
* `WHO_NREVSS_Public_Health_Labs.csv`:  Gives counts of number of speciments tested per week and number  of specimens that tested positive. Also differentiates based on strain of A and B. Only from 2015-2020. Note that beginning for the 2015-16 season, reports from public health and clinical laboratories are presented separately in the weekly influenza update.
* `ny_flu_cases_by_county_2009_2020.csv`: Comprehensive record of public health lab confirmed flu cases in New York from 2009 to 2020. Also discriminates based on strain of influenza beyond just A and B.
* `ca_flu_cases_byregion_2009_2018.csv`: California flu cases not by county, but by region  (i.e. Bay Area, Central, e.t.c), so might need do some extrapolation to map back to counties if you want to use this data.
* `national_pi_deaths_2013_2020.csv`: deaths nationwide.
* `statewide_pi_deaths_2012_2020.csv`: deaths statewide.

Compiled By Connor Soohoo (connorsoohoo@gmail.com)

## `geolocation`

Geographic data of counties from https://github.com/btskinner/spatial.

Summary:
* `county_centers.csv`: This wide file gives the latitude and longitude for the spatial and population centers of every county in the United States for the Census years 2000 and 2010.
* `nearest_hei.csv`: This long file gives the nearest highest education institution (HEI) to each county population center across a number of years and higher education sectors.
* `neighborcounties.csv`: This long file links every county in the United States (as of the 2010 Census) with all of its contiguous counties.

Compiled By Connor Soohoo (connorsoohoo@gmail.com)

## `mobility`

Anonymized mobility metrics to analyze efficacy of social distancing, from Descartes Labs: https://github.com/descarteslabs/DL-COVID-19.

The data is available in CSV format with each date as a row in the
[DL-us-mobility-daterow.csv](DL-us-mobility-daterow.csv) file.

```csv
date,country_code,admin_level,admin1,admin2,fips,samples,m50,m50_index
2020-03-26,US,2,"New Mexico","Santa Fe County","35049",1331,0.095,1
...
```

An alternate arrangement of the same data in CSV format with dates in
the header, which may be preferable for some users, is in the
[DL-us-m50.csv](DL-us-m50.csv),
[DL-us-m50_index.csv](DL-us-m50_index.csv) and
[DL-us-samples.csv](DL-us-samples.csv) files.

```csv
country_code,admin_level,admin1,admin2,fips,2020-03-24,2020-03-25,2020-03-26
US,2,"New Mexico","Santa Fe County","35049",2,4,1
...
```

### Field description

For more `m50` and `m50_index` detailed metric descriptions, see the following paper: https://www.descarteslabs.com/wp-content/uploads/2020/03/mobility-v097.pdf

- **country_code**: ISO 3166-1 alpha-2 code.
- **admin_level**: 0 for country, 1 for admin1, 2 for admin2 granularity.
- **admin1**: [GeoNames](https://www.geonames.org/) ADM1 feature name for the first-order administrative division, such as a state in the United States.
- **admin2**: [GeoNames](https://www.geonames.org/) ADM2 feature name for the second-order administrative division, such as a county or borough in the United States.
- **fips**: [FIPS code](https://www.census.gov/quickfacts/fact/note/US/fips), a
standard geographic identifier, to make it easier to combine this data
with other data sets.
- **samples**: The number of samples observed in the specified region.
- **m50**: The median of the max-distance mobility for all samples in the specified region.
- **m50_index**: The percent of normal m50 in the region, with normal m50 defined during 2020-02-17 to 2020-03-07.

Compiled By Connor Soohoo (connorsoohoo@gmail.com)

## `hospitals`
Includes beds, ICU beds, staffed beds, etc. at the county level nationwide. Also more information on staff preparedness for CA.

Summary:
* `bed_densities.csv`: Number of hospital beds per mile for each US state.
* `beds_by_county.csv`: Initial (pre-virus) Numbers of staffed hospital beds, licensed hospital beds, and ICU beds for each county in each US state.
* `ca_county_hospital_statistics.csv`: Number of hospitals as well as their working staff, contractors, and students for each county in California. Also notes whether these staff were flu-vaccinated or not, and if masks were required or not. Essentially evaluates preparedness of each county's hospitals. Consult `ca_county_hospital_statistics-key.tsv` for the meaning behind each column value. https://www.cdph.ca.gov/Programs/CHCQ/HAI/Pages/HealthcarePersonnelInfluenzaVaccinationReportingInCA_Hospitals.aspx
* `icu_county.csv`: ICU beds at the county level from the Healthcare Cost Report Information System (HCRIS at cms.gov) and hospital general information (data.medicare.gov). Data dictionary and more details available at. https://khn.org/wp-content/uploads/sites/2/2020/03/KHN_ICU_bed_county_analysis.zip

Compiled By Connor Soohoo (connorsoohoo@gmail.com) and quantummind

## `other`

Random tidbits that could be useful for a detailed analysis of COVID-19.

Summary:
* `air_traffic.csv`: Data on 2019 US air traffic. Includes origin and destination airports. https://www.transtats.bts.gov/DL_SelectFields.asp
* `policies.csv`: Interventions at the county level, compiled by Johns Hopkins University researchers. The values indicate the day in March 2020 that the policy was put into action. https://github.com/JieYingWu/COVID-19_US_County-level_Summaries/tree/master/data
* `transit.csv`: Connectivity and frequency of transit per county. Data found by AllTransit using available General Transit Feed Specification data from transit agencies and publicly available schedules. https://alltransit.cnt.org/rankings/

## `processing_data`

Datasets that help in processing. Currently only FIPS codes to county names.

Summary:
* `fips_key.csv`: FIPS to county/state name conversion. https://www.dol.gov/owcp/regs/feeschedule/fee/Effective_May_16_2004_County_and_State_FIPS.htm

Compiled by quantummind

## `berkeley aggregated data`

 This includes data on number of icu beds and hospitals per county prevalance of chronic diseases, number of total deaths (from any cause), mortality rate from respiratory diseases, voting history, and impact from smoking at the county level.

 We have an abridged version here. You can download the full `df_county_level_cached.csv` file [here](https://drive.google.com/open?id=1EHqZxbTVPO5RDxDvJntZMNBjhxGeE2bU)

 You can regenerate this dataset and view the original sources [here](https://github.com/Yu-Group/covid-19-ventilator-demand-prediction)

 Summary:
 * `aggregate_berkeley.csv`: A few columns are selected from a few thousand by feature selection done by Berkeley.
 * `df_county_level_cached.csv`: (Not included in the repo) All of this data in one table. There are 3114 rows (one for each county) and 7180 columns. The FIPS code is in column 'countyFIPS', and the county name is in 'County'.

 Compiled by alexcdot


## `respiratory_disease`

Includes chronic respiratory disease mortality at a county level nationwide.

Summary:
* `IHME_USA_COUNTY_RESP_DISEASE_MORTALITY_1980_2014_NATIONAL_Y2017M09D26.XLSX`: Chronic respiratory disease mortality at a county level nationwide in 4 year increments from 1980 - 2014. Mortality rate is out of 100,000. The notebook that helps you parse this data can be found at `exploratory/alexcui_respiratory_disease.ipynb`

### Sources

* [Institute for Health Metrics and Evaluation](http://ghdx.healthdata.org/record/ihme-data/united-states-chronic-respiratory-disease-mortality-rates-county-1980-2014)

Compiled by Alex Cui (alexcdot)
