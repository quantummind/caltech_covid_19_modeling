#!/bin/bash

cd $(git rev-parse --show-toplevel)
cd code/processing/raw_data_processing
python get_JH_data.py
python get_JH_daily.py
./get_us_county_covid_data.sh