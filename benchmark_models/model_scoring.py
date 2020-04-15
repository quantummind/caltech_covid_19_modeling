import numpy as np
from benchmark_models import utils

def score_all_predictions(pred_file, date):
    true_data = utils.get_processed_df('nyt_us_counties_daily.csv')
    proc_score_date = utils.process_date(date, true_data)
    raw_pred_data = np.genfromtxt(pred_file, delimiter=',', skip_header=1, dtype=np.str)
    date_preds = np.array([row for row in raw_pred_data if date in row[0]])
    all_fips = np.array([row[0].split('-')[-1] for row in date_preds])
    all_preds = date_preds[:, 1:].astype(np.float)

    tot_loss = 0
    for fips, preds in zip(all_fips, all_preds):
        true_number = utils.get_region_data(true_data, fips, proc_date=proc_score_date)
        print(fips, true_number)

if __name__ == '__main__':
    score_all_predictions('C:\\Users\\dyurk\\Repos\\caltech_covid_19_modeling\\benchmark_models\\erf_model_predictions.csv', '2020-04-12')