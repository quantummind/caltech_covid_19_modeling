#!/bin/bash
cd $(git rev-parse --show-toplevel)
cd data/us/air_quality
python ../../../processing/raw_data_processing/get_aq_daily.py
cd $(git rev-parse --show-toplevel)
