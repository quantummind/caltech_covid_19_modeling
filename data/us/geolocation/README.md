## Geospatial

### [`neighborcounties.csv`](https://github.com/btskinner/spatial/blob/master/data/neighborcounties.csv) [[Raw]](https://raw.githubusercontent.com/btskinner/spatial/master/data/neighborcounties.csv)

This long file links every county in the United States (as of the 2010 Census) with all of its contiguous counties. Five-digit county-level [FIPS](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) codes are used to identify the counties. These codes uniquely identify each county and can be used to link with other datasets such as the [American Community Survey](https://www.census.gov/programs-surveys/acs/).

##### COLUMNS

| Name | Description|
|:-----|:-----------|
|`orgfips`|Origin county FIPS code|
|`adjfips`|Adjacent county FIPS code|
|`instate`|==1 if adjacent county is in the same state|

### [`county_centers.csv`](https://github.com/btskinner/spatial/blob/master/data/county_centers.csv) [[Raw]](https://raw.githubusercontent.com/btskinner/spatial/master/data/county_centers.csv)  

This wide file gives the latitude and longitude for the spatial and population centers of every county in the United States for the Census years 2000 and 2010. These coordinates are given by the U.S. Census; this file simply collects them in a single easy-to-use file. Five-digit county-level [FIPS](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) codes are used to identify the counties.

##### COLUMNS

| Name | Description|
|:-----|:-----------|
|`fips`|Unique county-level five-digit FIPS code|
|`clon00`|Longitude of spatial center, 2000|
|`clat00`|Latitude of spatial center, 2000|
|`clon10`|Longitude of spatial center, 2010|
|`clat10`|Latitude of spatial center, 2010|
|`pclon00`|Longitude of population-weighted center, 2000|
|`pclat00`|Latitude of population-weighted center, 2000|
|`pclon10`|Longitude of population-weighted center, 2010|
|`pclat10`|Latitude of population-weighted center, 2010|

### [`nearest_hei.csv`](https://github.com/btskinner/spatial/blob/master/data/nearest_hei.csv) [[Raw]](https://raw.githubusercontent.com/btskinner/spatial/master/data/nearest_hei.csv)  

This long file gives the nearest highest education institution (HEI) to each county population center across a number of years and higher education sectors. Each row gives the nearest institution's [IPEDS](http://nces.ed.gov/ipeds/datacenter/Default.aspx) unique `unitid`, the distance in miles, and indicators for the year and subset of included schools (*e.g.,* nearest public four-year, nearest public two-year, etc.).

##### COLUMNS

| Name | Description|
|:-----|:-----------|
|`fips`|Unique county-level five-digit FIPS code|
|`unitid`|Unique IPEDS identifier for nearest HEI|
|`miles`|Distance in miles between county population center and nearest HEI|
|`limit_instate`|==1 if sample of schools is limited to those in same state as county|
|`year`|Year of match|
|`any`|==1 if any type of HEI is included in sample|
|`limit_fouryr`|==1 if only four-year HEIs are included in sample|
|`limit_twoyr`|==1 if only two-year HEIS are included in sample|
|`limit_pub`|==1 if only public HEIs are included in sample|
|`limit_pnp`|==1 if only private, non-profit HEIs are included in sample|
|`limit_pfp`|==1 if only private, for-profit HEIs are inluced in sample|

##### EXAMPLES

*Absolute nearest HEI (regardless of sector and crossing state lines)*

* Rows in which `limit_instate == 0` and `any == 1`

*Nearest instate public four-year HEI*

* Rows in which `limit_instate == 1` and `limit_fouryr == 1` and `limit_pub == 1`

*Nearest instate private, for-profit two-year HEI*

* Rows in which `limit_instate == 1` and `limit_twoyr == 1` and `limit_pfp == 1`

From https://github.com/btskinner/spatial

Compiled by Connor Soohoo (connorsoohoo@gmail.com)
