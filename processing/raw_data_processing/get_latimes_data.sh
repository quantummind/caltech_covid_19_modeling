#!/bin/bash
cd $(git rev-parse --show-toplevel)
wget https://github.com/datadesk/california-coronavirus-data/raw/master/cdph-state-totals.csv -O data/us/covid/california/cdph-state-totals.csv
wget https://github.com/datadesk/california-coronavirus-data/raw/master/latimes-agency-totals.csv -O data/us/covid/california/latimes-agency-totals.csv
wget https://github.com/datadesk/california-coronavirus-data/raw/master/latimes-place-totals.csv -O data/us/covid/california/latimes-place-totals.csv

