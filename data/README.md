## `data`

This directory houses all small (< 50 MB) data sets that are a result of individual experiments and/or simulations. Depending on the type of data collected, you may want to split them up based on file type.

If possible, data sets from individual experiments should be compiled in a long-form tidy format. This is important not only for your analysis, but for others who wish to reproduce your work. While you may have an intimate knowledge of your data and experimental structure, it may not be obvious to anyone else. It is much easier if you can combine the individual data sets into as few files as possible so only one or two files have to be read to perform the analysis and generate the figures. 

This is **not** a place to store all of your large (> 50 MB) data files, such as images. For accessibility of these large data sets, there are myriad online data repositories such as [Zenodo](https://zenodo.org) which provide free storage and DOI generation. In addition, you should have all of your data backed up locally with redundancy.

US datasets must all have a column named "FIPS" and international datasets must all have a column named "ISO" code.

US data:
* `icu_county.csv`: Hospitals and ICU beds per county; also population over the age of 60. https://khn.org/wp-content/uploads/sites/2/2020/03/KHN\_ICU\_bed\_county\_analysis.zip
* `transit.csv`: Connectivity and frequency of transit per county. https://alltransit.cnt.org/rankings/
* `JHU_daily_US.csv`: COVID-19 case and death counts per county. https://github.com/CSSEGISandData/COVID-19/tree/master/csse\_covid\_19\_data
* `education.csv`: Education level per county. https://www.ers.usda.gov/data-products/county-level-data-sets/download-data/
* `poverty.csv`: Urbanization and poverty rates per county. https://www.ers.usda.gov/data-products/county-level-data-sets/download-data/
* `unemployment.csv`: Urbanization, metro areas, unemployment, and income per county. https://www.ers.usda.gov/data-products/county-level-data-sets/download-data/
* `fips_key.csv`: FIPS to county/state name conversion. https://www.dol.gov/owcp/regs/feeschedule/fee/Effective\_May\_16\_2004\_County\_and\_State\_FIPS.htm

International data:
* `Johns_Hopkins_data/jhu_csse_processed.csv`: COVID-19 case and death data per country with some regional breakdown. https://github.com/CSSEGISandData/COVID-19/tree/master/csse\_covid\_19\_data