import numpy as np
import utils


def score_all_predictions(pred_file, date, mse=False):
    true_data = utils.get_processed_df('nyt_us_counties_daily.csv')
    proc_score_date = utils.process_date(date, true_data)
    raw_pred_data = np.genfromtxt(pred_file, delimiter=',', skip_header=1, dtype=np.str)
    date_preds = np.array([row for row in raw_pred_data if date in row[0]])
    all_fips = np.array([row[0].split('-')[-1] for row in date_preds])
    all_preds = date_preds[:, 1:].astype(np.float)

    # all_preds = np.zeros(all_preds.shape)

    tot_loss = 0
    for fips, preds in zip(all_fips, all_preds):
        true_number = utils.get_region_data(true_data, fips, proc_date=proc_score_date)
        if mse:
            tot_loss += (preds[4] - true_number) ** 2
        else:
            tot_loss += pinball_loss(preds, true_number)
    return tot_loss / len(all_preds)


def pinball_loss(preds, true_val, p_vals=np.arange(0.1, 1.0, 0.1)):
    loss = 0
    for pred, p in zip(preds, p_vals):
        delta = np.abs(true_val - pred)
        if pred < true_val:
            loss += p * delta
        else:
            loss += (1 - p) * delta
    return loss / len(p_vals)


if __name__ == '__main__':
    pred_file = 'C:\\Users\\dyurk\\Repos\\caltech_covid_19_modeling\\benchmark_models\\erf_model_predictions.csv'
    #Boundary 2020-03-29: 0.1622
    #Boundary 2020-04-09: 0.142797
    #Boundary 2020-04-10: 0.131404
    print((score_all_predictions(pred_file, '2020-04-11') + score_all_predictions(pred_file, '2020-04-12'))/2)
