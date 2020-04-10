#!/bin/bash

cd $(git rev-parse --show-toplevel)
cd processing/raw_data_processing
python3 get_JH_data.py
python3 get_JH_daily.py
./get_us_county_covid_data.sh
./get_coronadatascraper_data.sh
./get_ECDC_data.sh
./clean_italy.sh
./get_nyt_data.sh
./get_mobility_data.sh
sh get_aq_daily.sh
./get_latimes_data.sh
python3 get_google_mobility_data.py
