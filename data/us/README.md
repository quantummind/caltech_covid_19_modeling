# US data

US datasets are (usually) encoded with a column named "FIPS" denoting the county code. Translations to county names are in `processing_data/fips_key.csv`. **If you add data, update both this README and the README in the directory of the new data!**

## `covid`

County-level from USAFacts (aggregated from the CDC, state- and local-level public health agencies, and academic institutions), which is claimed to have been confirmed with individual counties. County-level data from JHU.

Summary:
* `confirmed_cases.csv`: Confirmed COVID cases per county, USAFacts. https://static.usafacts.org/public/data/covid-19/
* `deaths.csv`: Confirmed COVID deaths per county, USAFacts. https://static.usafacts.org/public/data/covid-19/
* `JHU_daily_US.csv`: COVID-19 case and death counts per county from JHU, merged from daily updates since 3/23/2020. https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data

Compiled by quantummind

## `demographics`

This includes age/gender, education, and economic information of the US population at the county level, and aggregated populations at the state level.

Summary:
* `acs_2018.csv`: Number of households, age and ethnicity breakdowns. American Community Survey (ACS) 2018, US Census Bureau (data.census.gov).
* `county_populations.csv`: Total population and population over the age of 60 per county from the 2017 American Community Survey. Data dictionary and more details available at. https://khn.org/wp-content/uploads/sites/2/2020/03/KHN_ICU_bed_county_analysis.zip
* `education.csv`: Education level per county. https://www.ers.usda.gov/data-products/county-level-data-sets/download-data/
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
* `national_pi_deaths_2013_2020.csv`: deaths nationwide.
* `statewide_pi_deaths_2012_2020.csv`: deaths statewide.
* `ny_flu_cases_by_county_2009_2020.csv`: Comprehensive record of public health lab confirmed flu cases in New York from 2009 to 2020. Also discriminates based on strain of influenza beyond just A and B.
* `ca_flu_cases_byregion_2009_2018.csv`: California flu cases not by county, but by region  (i.e. Bay Area, Central, e.t.c)*, so might need do some extrapolation to map back to counties if you want to use this data.

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

Random tidbits that could be useful for a detailed analysis of COVID-19. Currently only includes transit information.

Summary:
* `transit.csv`: Connectivity and frequency of transit per county. Data found by AllTransit using available General Transit Feed Specification data from transit agencies and publicly available schedules. https://alltransit.cnt.org/rankings/

Compiled by quantummind

## `processing_data`

Datasets that help in processing. Currently only FIPS codes to county names.

Summary:
* `fips_key.csv`: FIPS to county/state name conversion. https://www.dol.gov/owcp/regs/feeschedule/fee/Effective_May_16_2004_County_and_State_FIPS.htm

Compiled by quantummind