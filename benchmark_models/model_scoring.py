import numpy as np

np.set_printoptions(precision=4)
import utils
from matplotlib import pyplot as plt


# Bet fit preds, fixed % error
# Best fit preds, globally optimize % error
# Best fit preds, optimize % error in bins
# Sampled preds, sampling error
# Sampled preds, globally scale sampling error
# Sampled preds, scale sampling error in bins


def score_all_predictions(pred_file, date, mse=False, stretch_fac=1.0, key='deaths'):
    true_data = utils.get_processed_df('nyt_us_counties_daily.csv')
    cum_data = utils.get_processed_df('nyt_us_counties.csv')
    proc_score_date = utils.process_date(date, true_data)
    raw_pred_data = np.genfromtxt(pred_file, delimiter=',', skip_header=1, dtype=np.str)
    date_preds = np.array([row for row in raw_pred_data if date in row[0]])
    all_fips = np.array([row[0].split('-')[-1] for row in date_preds])
    all_preds = date_preds[:, 1:].astype(np.float)

    for i, row in enumerate(all_preds):
        row_stretch = row[4] + stretch_fac * (row - row[4])
        all_preds[i] = np.maximum(np.zeros(row.shape), row_stretch)
    # all_preds = np.round(all_preds)

    # all_preds = np.zeros(all_preds.shape)

    tot_loss = 0
    small_loss, mid_loss, large_loss = 0, 0, 0
    small_count, mid_count, large_count = 0, 0, 0
    for fips, preds in zip(all_fips, all_preds):
        true_number = utils.get_region_data(true_data, fips, proc_date=proc_score_date, key=key)
        if mse:
            loss = (preds[4] - true_number) ** 2
        else:
            loss = pinball_loss(preds, true_number)
        tot_loss += loss
        cum_number = utils.get_region_data(cum_data, fips, proc_date=proc_score_date, key=key)
        if cum_number < 20:
            small_loss += loss
            small_count += 1
        elif cum_number < 1000:
            mid_loss += loss
            mid_count += 1
        else:
            large_loss += loss
            large_count += 1
    return np.array(
        [tot_loss / len(all_preds), small_loss / small_count, mid_loss / mid_count, large_loss / large_count])


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
    pred_file = 'C:\\Users\\dyurk\\Repos\\caltech_covid_19_modeling\\benchmark_models\\erf_model_case_predictions_dvar_0329.csv'
    print(score_all_predictions(pred_file, '2020-04-12', key='cases'))
    print(score_all_predictions(pred_file, '2020-04-12', key='cases', stretch_fac=0.75))
    print(score_all_predictions(pred_file, '2020-04-12', key='cases', stretch_fac=0.5))
    print(score_all_predictions(pred_file, '2020-04-12', key='cases', stretch_fac=0.25))
    # Boundary 2020-03-29: 0.16222992725893742
    #        w/ rounding: 0.1613920777743304
    #      w/ truncating: 0.16475678284551995
    #     w/ stretch 2.0: 0.1722
    #     w/ stretch 0.5: 0.1623276881442411
    #    w/ stretch 0.75: 0.16179737218602422
    #             +round: 0.16030268555865831
    # Boundary 2020-04-09: 0.1428
    # Boundary 2020-04-10: 0.1314
    # stretch_vals = np.arange(0.3, 1.55, 0.1)
    # scores = np.zeros((4, len(stretch_vals)))
    # for i, sv in enumerate(stretch_vals):
    #     print(sv)
    #     score = score_all_predictions(pred_file, '2020-04-11', stretch_fac=sv)
    #     scores[:, i] = score
    # plt.yscale('log')
    # plt.plot(stretch_vals, scores[0], label='total score', c='black')
    # plt.plot(stretch_vals, scores[1], label='low death score', c='blue')
    # plt.plot(stretch_vals, scores[2], label='mid death score', c='red')
    # plt.plot(stretch_vals, scores[3], label='high death score', c='green')
    # plt.legend()
    # plt.tight_layout()
    # plt.savefig('loss_graph.png', bbox_inches='tight')

# Case Pred Baseline:           [ 3.1096  0.1233  2.8409 85.5501]
# Case Pred DataVar:            [ 4.28    0.124   2.991  129.97 ]



# Loss Baseline:                 [ 0.1622  0.016   10.1678]
# Stretch 0.75:                  [ 0.1618  0.0165  9.9904]
# Stretch 0.5:                   [ 0.1623  0.0169  9.9179]
# Stretch 0.25:                  [ 0.1678  0.0173  10.3842]
# Rounding:                      [ 0.1614  0.0148  10.1856]
# Stretch 0.75 + Rounding:       [ 0.1603  0.0148  10.0255]
