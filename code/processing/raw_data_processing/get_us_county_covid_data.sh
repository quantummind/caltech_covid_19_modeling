#!/bin/bash
cd $(git rev-parse --show-toplevel)
wget https://static.usafacts.org/public/data/covid-19/covid_confirmed_usafacts.csv -O data/us/covid/confirmed_cases.csv
wget https://static.usafacts.org/public/data/covid-19/covid_deaths_usafacts.csv -O data/us/covid/deaths.csv
wget http://covidtracking.com/api/states/daily.csv -O data/us/covid/daily_state_tests.csv