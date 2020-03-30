#!/bin/bash
cd $(git rev-parse --show-toplevel)
wget https://github.com/pcm-dpc/COVID-19/raw/master/dati-province/dpc-covid19-ita-province.csv -O data/international/italy/covid/dpc-covid19-ita-province.csv
wget https://github.com/pcm-dpc/COVID-19/raw/master/dati-regioni/dpc-covid19-ita-regioni.csv -O data/international/italy/covid/dpc-covid19-ita-regioni.csv

cd $(git rev-parse --show-toplevel)
cd processing/raw_data_processing
python3 clean_italy.py