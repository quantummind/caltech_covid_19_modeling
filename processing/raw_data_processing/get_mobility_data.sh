#!/bin/bash
cd $(git rev-parse --show-toplevel)
wget https://raw.githubusercontent.com/descarteslabs/DL-COVID-19/master/DL-us-m50.csv -O data/us/mobility/DL-us-m50.csv
wget https://raw.githubusercontent.com/descarteslabs/DL-COVID-19/master/DL-us-m50_index.csv -O data/us/mobility/DL-us-m50_index.csv
wget https://raw.githubusercontent.com/descarteslabs/DL-COVID-19/master/DL-us-mobility-daterow.csv -O data/us/mobility/DL-us-mobility-daterow.csv
wget https://raw.githubusercontent.com/descarteslabs/DL-COVID-19/master/DL-us-samples.csv -O data/us/mobility/DL-us-samples.csv
