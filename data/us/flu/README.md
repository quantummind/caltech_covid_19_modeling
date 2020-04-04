# US Influenza Data

## Cases

Influenza cases nationally and statewide for the past 5+ years, including the 2019-2020 Flu Season up to Week 11 (of 2020). Right now these are fixed, but feel free to use the interactive source links below to pull more recent weeks of data as the  challenge progresses.

**Most of these report not in years but in Flu, especially in earlier years**. For instance, the 2019-2020 flu reasons runs from like September/October of 2019 through spring of 2020. Flu season typically runs from around Week 40 of the previous year up until Week 20. It would be best to incorporate seasonality into any flu models you create. **Each item in the table represents a week's worth of data, as denoted by the week number in that calendar year.** 

Age ranges are usually grouped by 0-4, 5-24, 25-49, 25-64, 50-64, 65+

* `ILI_Ages.csv`: Percentage of visits for Influenza-Like-Illness (ILI) reported by Sentinal Providers, for the past 23 years from 1997 up to 2020. Patients with ILI are also grouped by age range. Definition of what a sentinal provider is is given here: http://dhhr.wv.gov/oeps/disease/flu/documents/sentinel-providers/sentinel-%20provider-factsheet.pdf. Essentially a sentinal provider can be a provider of any specialty (e.g., family physicians, internists, pediatricians) in any type of practice (e.g., private practice, public health clinic, urgent care center, emergency room, student health center). This means that patients with mild flu-like symptoms can be surveyed without having to send samples to a national lab.

* `WHO_cases_age_groupings_virus_strains.csv`: Influenza cases grouped by age range and by virus strain. Details on virus strains given below. **Useful for looking at spread of H1N1**

* `WHO_NREVSS_Clinical_Labs.csv`:  Gives number of specimens tested per week and number and percent of specimens that tested positive for Influenza A and B, respectively. Only from 2015 - 2020. Note that beginning for the 2015-16 season, reports from public health and clinical laboratories are presented separately in the weekly influenza update.

* `WHO_NREVSS_Combined_prior_to_2015_16.csv`: 1997 - 2015 data. Gives number of specimens tested per week and number and percent of specimens that tested positive for Influenza A and B, respectively. Also differentiates based on strain. Combined data from public health and clinical labs.  **Very comprehensive, Useful for looking at spread of H1N1 (2009)**

* `WHO_NREVSS_Public_Health_Labs.csv`:  Gives counts of number of speciments tested per week and number  of specimens that tested positive. Also differentiates based on strain of A and B. Only from 2015-2020. Note that beginning for the 2015-16 season, reports from public health and clinical laboratories are presented separately in the weekly influenza update.


### Interactive Sources

View these interactive sources below to  visualize / play with the data or to download other data yourself  (i.e. if you wanted to pull a more current week's worth of data).

Interactive Source for Statewide and National Flu case statistics (including H1N1):  https://gis.cdc.gov/grasp/fluview/fluportaldashboard.html

Interactive Source for viewing Flu Cases Grouped by Age and Virus Type Past 12 Flu Seasons (i.e. years): https://gis.cdc.gov/grasp/fluview/flu_by_age_virus.html

US Weekly Influenza Surveillance Report: https://www.cdc.gov/flu/weekly/#ClinicalLaboratories

## Deaths

**Shows deaths by influenza and by pneumonia nationwide and statewide from 2012-2013 up to 2020. Also shows total death numbers (nationwide and by state).**

`national_pi_deaths_2013_2020.csv` and `statewide_pi_deaths_2012_2020.csv` are the pertinent filenames.

### Interactive Sources

National and Statewide Flu Mortality Statistics:  
https://gis.cdc.gov/grasp/fluview/mortality.html

## County

County related information. Only for NY and CA at this time.

* `ny_flu_cases_by_county_2009_2020.csv`: Comprehensive record of public health lab confirmed flu cases in New York from 2009 to 2020. Also discriminates based on strain of influenza beyond just A and B.
* `ca_flu_cases_byregion_2009_2018.csv`: *California flu cases not by county, but by region  (i.e. Bay Area, Central, e.t.c)*, so might need do some extrapolation to map back to counties if you want to use this data.

### Sources:

* CA Health Care Influenza Vaccination: https://data.ca.gov/dataset/health-care-personnel-influenza-vaccination

* CA Influenza Surveillance: https://data.ca.gov/dataset/influenza-surveillance

* NY Influenza Cases By County: https://healthdata.gov/dataset/influenza-laboratory-confirmed-cases-county-beginning-2009-10-season

## Virus Strain Details

CDC antigenically characterizes a subset of influenza viruses by hemagglutination inhibition (HI) or neutralization based Focus Reduction assays (FRA). Antigenic drift is evaluated by comparing antigenic properties of cell-propagated reference viruses representing currently recommended vaccine components with those of cell-propagated circulating viruses. CDC antigenically characterized 446 influenza viruses collected in the United States from September 29, 2019, to March 14, 2020. These data are not used to make calculations about vaccine effectiveness (VE). CDC conducts VE studies each year to measure the benefits of flu vaccines in people.

### Influenza A Viruses

#### A (H1N1)pdm09:

177 A(H1N1)pdm09 viruses were antigenically characterized by HI with ferret antisera, and 143 (80.8%) were antigenically similar (reacting at titers that were within 4-fold of the homologous virus titer) to cell-propagated A/Brisbane/02/2018-like reference viruses representing the A(H1N1)pdm09 component for the 2019-20 Northern Hemisphere influenza vaccines. The decrease in the percent of A(H1N1)pdm09 viruses similar to A/Brisbane/02/2018 is due to some of the recent viruses selected for testing having a single amino acid change that is antigenically distinguishable in antigenic assays using ferret sera. Similar viruses were observed last season as well and these represented a small proportion of virus circulating. We have observed an increase in the proportion of H1N1pdm09 viruses with this change late in the US season.

#### A (H3N2):

76 A(H3N2) viruses were antigenically characterized by FRA with ferret antisera, and 31 (40.8%) were antigenically similar to cell-propagated A/Kansas/14/2017-like reference viruses representing the A(H3N2) component for the 2019-20 Northern Hemisphere influenza vaccines.

### Influenza B Viruses

#### B/Victoria:

165 B/Victoria lineage viruses, including viruses from both co-circulating sub-clades, were antigenically characterized by HI with ferret antisera, and 106 (64.2%) were antigenically similar to cell-propagated B/Colorado/06/2017-like reference viruses representing the B/Victoria component for the 2019-20 Northern Hemisphere influenza vaccines.

#### B/Yamagata:

28 B/Yamagata lineage viruses were antigenically characterized by HI with ferret antisera, and all 28 (100%) were antigenically similar to cell-propagated B/Phuket/3073/2013-like reference viruses representing the B/Yamagata component for the 2019-20 Northern Hemisphere influenza vaccines.

**Compiled By Connor Soohoo (connorsoohoo@gmail.com)**
