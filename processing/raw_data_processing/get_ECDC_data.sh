#!/bin/bash
cd $(git rev-parse --show-toplevel)
wget https://covid.ourworldindata.org/data/ecdc/full_data.csv -O data/international/covid/our_world_in_data/full_data.csv
cd processing/raw_data_processing
python3 aggregate_our_world_in_data.py