import csv
import pandas as pd

link = 'https://covid.ourworldindata.org/data/ecdc/full_data.csv'
pd.read_csv(link).to_csv('our_world_in_data.csv', index=False)
