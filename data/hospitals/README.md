# Hospitals

## National/Statewide Statistics

## County Statistics

* `ca_county_hospital_statistics.csv`: Number of hospitals as well as their working staff, contractors, and students for each county in California. Also notes whether these staff were flu-vaccinated or not, and if masks were required or not. Essentially evaluates preparedness of each county's hospitals. Consult `ca_county_hospital_statistics_datadict.xlsx` for the meaning behind each column value. *County names are given, not FIPS codes,
so this table might have to be joined with the FIPS code csv file in the `us` subfolder.*
 **EDIT: FIPS data now in table**

* `beds.csv`: Number of hospital beds per mile for each US state.

* `hospital_beds_by_county.csv`: Initial (pre-virus) Numbers of staffed hospital beds, licensed hospital beds, and ICU beds for each county in each US state.

## Sources:

### Hospital Capacity Data

* [American Hospital Directory](https://www.ahd.com/states/hospital_CA.html) (Link is to CA data, but seems to support any state)
* [Medicare Claims for Inpatients](https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Hospital-Service-Area-File)
* [CA Healthcare Facilities](https://data.chhs.ca.gov/dataset/licensed-healthcare-facility-listing/resource/641c5557-7d65-4379-8fea-6b7dedbda40b?inner_span=True)
* [American Hosptial Association](https://www.ahadata.com/aha-hospital-statistics/) (paywalled)

* CA Health Care Influenza Vaccination: https://data.ca.gov/dataset/health-care-personnel-influenza-vaccination

Also checkout https://github.com/covid-projections/covid-data-model for more info.

Compiled by Connor Soohoo (connorsoohoo@gmail.com)
