#!/bin/bash
cd $(git rev-parse --show-toplevel)
wget https://github.com/nytimes/covid-19-data/raw/master/us-states.csv -O data/us/covid/nyt_us_states.csv
wget https://github.com/nytimes/covid-19-data/raw/master/us-counties.csv -O data/us/covid/nyt_us_counties.csv
cd processing/raw_data_processing
python3 difference_nyt_data.py
