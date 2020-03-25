#!/bin/bash
cd $(git rev-parse --show-toplevel)
wget https://coronadatascraper.com/timeseries.csv -O data/international/covid/corona_data_scraper/geopop.csv
