#!/bin/bash
cd $(git rev-parse --show-toplevel)
wget https://coronadatascraper.com/timeseries.csv -O data/geolocation_population/geopop.csv
