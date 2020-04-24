import numpy as np

np.set_printoptions(precision=5)
import utils
from matplotlib import pyplot as plt


def score_all_predictions(pred_file, date, model_date, mse=False, key='cases', bin_cutoffs=[20, 1000]):
    true_data = utils.get_processed_df('nyt_us_counties_daily.csv')
    cum_data = utils.get_processed_df('nyt_us_counties.csv')
    proc_score_date = utils.process_date(date, true_data)
    proc_model_date = utils.process_date(model_date, true_data)
    raw_pred_data = np.genfromtxt(pred_file, delimiter=',', skip_header=1, dtype=np.str)
    date_preds = np.array([row for row in raw_pred_data if date in row[0]])
    all_fips = np.array([row[0].split('-')[-1] for row in date_preds])
    all_preds = date_preds[:, 1:].astype(np.float)
    true_data = np.array([utils.get_region_data(true_data, fips, proc_date=proc_score_date, key=key) for fips in all_fips])
    cum_data = np.array([utils.get_region_data(cum_data, fips, proc_date=proc_model_date, key=key) for fips in all_fips])
    return get_scores(all_fips, all_preds, true_data, cum_data, mse=mse, bin_cutoffs=bin_cutoffs)


def get_scores(all_fips, all_preds, true_data, cum_data, bin_cutoffs=[20, 1000], mse=False):
    # stretch_fac = 0.5
    # for i, row in enumerate(all_preds):
    #     row_stretch = row[4] + stretch_fac * (row - row[4])
    #     all_preds[i] = np.maximum(np.zeros(row.shape), row_stretch)
    # all_preds = np.round(all_preds)
    all_preds[all_preds < 0.75] = 0.0

    # all_preds = np.zeros(all_preds.shape)

    tot_loss = 0
    bin_losses, bin_counts = np.zeros(len(bin_cutoffs) + 1), np.zeros(len(bin_cutoffs) + 1)
    for fips, preds, true_number, cum_number in zip(all_fips, all_preds, true_data, cum_data):
        if mse:
            loss = (preds[4] - true_number) ** 2
        else:
            loss = pinball_loss(preds, true_number)
        tot_loss += loss
        done = False
        for i, bc in enumerate(bin_cutoffs):
            if cum_number <= bc:
                bin_losses[i] += loss
                bin_counts[i] += 1
                done = True
                break
        if not done:
            bin_losses[-1] += loss
            bin_counts[-1] += 1

    return tot_loss / len(all_preds), bin_losses / bin_counts


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
    bin_cutoffs = [1, 10, 50, 100, 500]
    bin_x = [1, 5, 30, 75, 250, 750]
    pred_file = 'C:\\Users\\dyurk\\Repos\\caltech_covid_19_modeling\\benchmark_models\\erf_model_predictions_0413.csv'
    scores = score_all_predictions(pred_file, '2020-04-14', '2020-04-13', key='deaths', bin_cutoffs=bin_cutoffs)
    scores_mse = score_all_predictions(pred_file, '2020-04-14', '2020-04-13', key='deaths', bin_cutoffs=bin_cutoffs, mse=True)
    print(scores, scores_mse)
    plt.plot(bin_x, scores[1], label='erf model', c='r')
    plt.plot(bin_x, np.sqrt(scores_mse[1]), label='erf model rmse', ls='--', c='r')
    pred_file = 'C:\\Users\\dyurk\\Repos\\caltech_covid_19_modeling\\benchmark_models\\rona_szn_0414_sub.csv'
    scores = score_all_predictions(pred_file, '2020-04-14', '2020-04-13', key='deaths', bin_cutoffs=bin_cutoffs)
    scores_mse = score_all_predictions(pred_file, '2020-04-14', '2020-04-13', key='deaths', bin_cutoffs=bin_cutoffs, mse=True)
    print(scores, scores_mse)
    plt.plot(bin_x, scores[1], label='rona szn model', c='b')
    plt.plot(bin_x, np.sqrt(scores_mse[1]), label='rona szn model rmse', ls='--', c='b')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Cumulative Deaths on 0413')
    plt.ylabel('Pinball Score in Bin')
    plt.title('Comparing Models at Different Death Counts')
    plt.legend()
    plt.tight_layout()
    plt.savefig('model_comp_0413.png', bbox_inches='tight')
    # print(score_all_predictions(pred_file, '2020-04-12', key='cases', stretch_fac=0.75))
    # print(score_all_predictions(pred_file, '2020-04-12', key='cases', stretch_fac=0.5))
    # print(score_all_predictions(pred_file, '2020-04-12', key='cases', stretch_fac=0.25))
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
