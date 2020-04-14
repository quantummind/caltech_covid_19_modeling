#!/bin/bash
cd $(git rev-parse --show-toplevel)
wget https://data.cdc.gov/api/views/hc4f-j6nb/rows.csv -O data/us/covid/cdc_all_deaths.csv