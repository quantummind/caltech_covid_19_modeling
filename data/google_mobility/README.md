# Google COVID-19 Community Mobility Reports
See https://www.google.com/covid19/mobility/

The reports chart movement trends over time by geography, across different categories of places such as **retail and recreation, groceries and pharmacies, parks, transit stations, workplaces, and residential**.

Since Google only provides PDFs (see most recent set of PDF mobility reports in pdfs subfolder), we have a scraper that aggregates these PDFs into CSV files.

We only save the most recent set of PDF files, since each new set of data is 50MB. You can look at the commit history to retrieve past physical PDF files. However, `mobility_report_regions.csv` and `mobility_report_US.csv` should contain the most accurative data from 3/29/2020 onwards, for both international and the US (state and county-wide), respectively. New county information (i.e. different dates) are reported on different rows.

In addition, we also have a script that extrapolates the trend lines from the Google Mobility graph images for the US counties, in addition to parsing the numbers. The resulting aggregate CSV file is called `extrapolated_mobility_report_US.csv`, and contains trends from 02/23/2020 onwards. In this file the `change` column represents the actual number that Google reported for the most recent date, and the `changecalc` column represents the extrapolated value that was determined from the same day. Note that this discrepancy is less than 3 percent for most if not all of the trends, so we can safely assume that these extrapolated values are fairly accurate and usable. Note that *each row represents a given county and category for all dates*, in contrast to the other csv files.

Looks like data is refreshed on Google every 4 or 5 days.

Also please don't move the `report_source.txt` file, it needs to be there for the aggregation script to work correctly.

Compiled by Connor Soohoo (connorsoohoo@gmail.com)
