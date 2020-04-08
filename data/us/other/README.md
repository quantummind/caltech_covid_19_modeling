## Other data

Random tidbits that could be useful for a detailed analysis of COVID-19.

Summary:
* `air_traffic.csv`: Data on 2019 US air traffic. Includes origin and destination airports. https://www.transtats.bts.gov/DL_SelectFields.asp
* `policies.csv`: Interventions at the county level, compiled by Johns Hopkins University researchers. Contains the dates that counties (or states governing them) took measures to mitigate the spread by restricting gatherings, given as the proleptic Gregorian ordinal of the date, where January 1 of year 1 has t = 1. This convention is chosen for consistency with the python datetime library. A date in this format can be converted to year, month, date with: `date = datetime.date.fromordinal(ordinal_date)`. https://github.com/JieYingWu/COVID-19_US_County-level_Summaries/tree/master/data
* `transit.csv`: Connectivity and frequency of transit per county. Data found by AllTransit using available General Transit Feed Specification data from transit agencies and publicly available schedules. https://alltransit.cnt.org/rankings/

Compiled by quantummind and thohoff