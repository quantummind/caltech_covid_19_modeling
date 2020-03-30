## `italy`

Italian case study at the regional level. The daily refresh script updates `COVID-19` and translates it from https://github.com/pcm-dpc/COVID-19.

Summary:
* `aggregate_italy.csv`: Everything except COVID: health, demographics, doctors, and more.
* `covid/dpc-covid19-ita-province.csv`: COVID-19 cases, deaths, testing, etc. at the province level (smaller than region).
* `covid/dpc-covid19-ita-regioni.csv`: COVID-19 cases, deaths, testing, etc. at the region level (larger than province).
* `demographics/region-populations.csv`: Population data.

Sources of demographics and aggregate data: http://dati-censimentopopolazione.istat.it/Index.aspx?lang=en, https://www.istat.it/en/health-statistics?data-and-indicators, https://www.istat.it/en/archivio/16271

Compiled by quantummind