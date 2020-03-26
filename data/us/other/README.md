## Other data

Random tidbits that could be useful for a detailed analysis of COVID-19. Currently only includes transit information.

Summary:
* `air_traffic.csv`: Data on 2019 US air traffic. Includes origin and destination airports. https://www.transtats.bts.gov/DL_SelectFields.asp
* `transit.csv`: Connectivity and frequency of transit per county. Data found by AllTransit using available General Transit Feed Specification data from transit agencies and publicly available schedules. https://alltransit.cnt.org/rankings/

Compiled by quantummind and thohoff

### `berkeley_aggregate_`
This includes data on number of icu beds and hospitals per county prevalance of chronic diseases, number of total deaths (from any cause), mortality rate from respiratory diseases, voting history, and impact from smoking at the county level.

Download the `df_county_level_cached.csv` file [here](https://drive.google.com/open?id=1EHqZxbTVPO5RDxDvJntZMNBjhxGeE2bU)

You can regenerate this dataset and view the original sources [here](https://github.com/Yu-Group/covid-19-ventilator-demand-prediction)

Summary:
* `df_county_level_cached.csv`: All of this data in one table. There are 3114 rows (one for each county) and 7180 columns. The FIPS code is in column 'countyFIPS', and the county name is in 'County'.
* `berkeley_agg_columns.csv`: Just a list of the all the column names in `df_county_level_cached.csv`. You can observe that some of the columns end with a four digit year YYYY, or a year and month YYYY-MM.

Compiled by alexcdot