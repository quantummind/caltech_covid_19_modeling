## Hospitals

Includes beds, ICU beds, staffed beds, etc. at the county level nationwide. Also more information on staff preparedness for CA.

Summary:
* `bed_densities.csv`: Number of hospital beds per mille for each US state (i.e. beds per 1000 people).
* `beds_by_county.csv`: Initial (pre-virus) Numbers of staffed hospital beds, licensed hospital beds, and ICU beds for each county in each US state.
* `ca_county_hospital_statistics.csv`: Number of hospitals as well as their working staff, contractors, and students for each county in California. Also notes whether these staff were flu-vaccinated or not, and if masks were required or not. Essentially evaluates preparedness of each county's hospitals. Consult `ca_county_hospital_statistics-key.tsv` for the meaning behind each column value. https://www.cdph.ca.gov/Programs/CHCQ/HAI/Pages/HealthcarePersonnelInfluenzaVaccinationReportingInCA_Hospitals.aspx
* `icu_county.csv`: ICU beds at the county level from the Healthcare Cost Report Information System (HCRIS at cms.gov) and hospital general information (data.medicare.gov). Data dictionary and more details available at. https://khn.org/wp-content/uploads/sites/2/2020/03/KHN_ICU_bed_county_analysis.zip

### Sources

* [American Hospital Directory](https://www.ahd.com/states/hospital_CA.html) (Link is to CA data, but seems to support any state)
* [Medicare Claims for Inpatients](https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Hospital-Service-Area-File)
* [CA Healthcare Facilities](https://data.chhs.ca.gov/dataset/licensed-healthcare-facility-listing/resource/641c5557-7d65-4379-8fea-6b7dedbda40b?inner_span=True)
* [American Hosptial Association](https://www.ahadata.com/aha-hospital-statistics/) (paywalled)
* CA Health Care Influenza Vaccination: https://data.ca.gov/dataset/health-care-personnel-influenza-vaccination

Also check out https://github.com/covid-projections/covid-data-model for more info.

Compiled by Connor Soohoo (connorsoohoo@gmail.com) and quantummind
