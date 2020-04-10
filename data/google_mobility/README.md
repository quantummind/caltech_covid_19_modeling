# Google COVID-19 Community Mobility Reports
See https://www.google.com/covid19/mobility/

The reports chart movement trends over time by geography, across different categories of places such as retail and recreation, groceries and pharmacies, parks, transit stations, workplaces, and residential.

Since Google only provides PDFs (see most recent set of PDF mobility reports in pdfs subfolder), we have a scraper that aggregates these PDFs into CSV files.

We only save the most recent set of PDF files, since each new set of data is 50MB. You can look at the commit history to retrieve past physical PDF files. However, the CSV files should contain all cumulative data from 3/29/2020. 

Looks like data is refreshed on Google every 4 or 5 days.

Also please don't move the `report_source.txt` file, it needs to be there for the aggregation script to work correctly.

Compiled by Connor Soohoo (connorsoohoo@gmail.com)
