#!/bin/bash
cd $(git rev-parse --show-toplevel)
wget https://github.com/descarteslabs/DL-COVID-19/blob/master/DL-us-m50.csv -O data/us/mobility/DL-us-m50.csv
wget https://github.com/descarteslabs/DL-COVID-19/blob/master/DL-us-m50_index.csv -O data/us/mobility/DL-us-m50_index.csv
wget https://github.com/descarteslabs/DL-COVID-19/blob/master/DL-us-mobility-daterow.csv -O data/us/mobility/DL-us-mobility-daterow.csv
wget https://github.com/descarteslabs/DL-COVID-19/blob/master/DL-us-samples.csv -O data/us/mobility/DL-us-samples.csv
