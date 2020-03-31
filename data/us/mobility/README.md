## `mobility`

Anonymized mobility metrics to analyze efficacy of social distancing, from Descartes Labs: https://github.com/descarteslabs/DL-COVID-19.

The data is available in CSV format with each date as a row in the
[DL-us-mobility-daterow.csv](DL-us-mobility-daterow.csv) file.

```csv
date,country_code,admin_level,admin1,admin2,fips,samples,m50,m50_index
2020-03-26,US,2,"New Mexico","Santa Fe County","35049",1331,0.095,1
...
```

An alternate arrangement of the same data in CSV format with dates in
the header, which may be preferable for some users, is in the
[DL-us-m50.csv](DL-us-m50.csv),
[DL-us-m50_index.csv](DL-us-m50_index.csv) and
[DL-us-samples.csv](DL-us-samples.csv) files.

```csv
country_code,admin_level,admin1,admin2,fips,2020-03-24,2020-03-25,2020-03-26
US,2,"New Mexico","Santa Fe County","35049",2,4,1
...
```

### Field description

For more `m50` and `m50_index` detailed metric descriptions, see the following paper: https://www.descarteslabs.com/wp-content/uploads/2020/03/mobility-v097.pdf

- **country_code**: ISO 3166-1 alpha-2 code.
- **admin_level**: 0 for country, 1 for admin1, 2 for admin2 granularity.
- **admin1**: [GeoNames](https://www.geonames.org/) ADM1 feature name for the first-order administrative division, such as a state in the United States.
- **admin2**: [GeoNames](https://www.geonames.org/) ADM2 feature name for the second-order administrative division, such as a county or borough in the United States.
- **fips**: [FIPS code](https://www.census.gov/quickfacts/fact/note/US/fips), a
standard geographic identifier, to make it easier to combine this data
with other data sets.
- **samples**: The number of samples observed in the specified region.
- **m50**: The median of the max-distance mobility for all samples in the specified region.
- **m50_index**: The percent of normal m50 in the region, with normal m50 defined during 2020-02-17 to 2020-03-07.

Compiled By Connor Soohoo (connorsoohoo@gmail.com)
