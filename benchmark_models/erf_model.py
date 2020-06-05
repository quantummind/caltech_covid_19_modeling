from scipy.special import erf
from scipy.optimize import curve_fit
import numpy as np
import time

import utils

SPICY_ERF = False


def erf_curve(t, log_max, slope, center):
    '''
    t: array of time values to input to the erf function
    log_max, slope, center: parameters of the erf curve
    '''
    # Using log(max) as the input rather than just max makes it easier for a curve fitter to match exponential data
    max_val = 10 ** log_max
    deaths = max_val * (1 + erf(slope * (t - center))) / 2
    return deaths


def erf2_curve(t, log_max1, log_max2, slope1, slope2, center):
    curve_1 = (10 ** log_max1) * (1 + erf(slope1 * (t - center))) / 2
    curve_2 = ((10 ** log_max1) / 2) + (10 ** log_max2) * erf(slope2 * (t - center)) / 2
    deaths = curve_1 * (t <= center) + curve_2 * (t > center)
    return deaths


def lin_curve(t, slope, intercept):
    '''
    t: array of time values to input to the linear function
    slope, intercept: parameters of the line
    '''
    ret = t * slope + intercept
    return ret


def get_time_list(data, future=0):
    '''
    data: general dataframe, used to find the first date in history
    future: number of days to extend the time values past present day
    '''
    t = data['date_processed'].values
    t = np.arange(np.min(t), np.max(t) + 1)  # Fill in any potential missing days
    if future > 0:  # Add on days in the future
        extrapolation = np.arange(future)
        t = np.concatenate((t, extrapolation + t[-1] + 1))
    return t


def run_model(func, params, t):
    '''
    func: method handle being run
    params: parameters to feed to the model
    t: input time values to the model
    '''
    preds = func(t, *params)
    preds[preds < 0] = 0  # Remove spurious negative death predictions

    return preds


def sample_bootstrap_err(t, fit_func, fit_bounds, popt, errors, num_samples=100, fixed_params=None):
    all_samples = []
    if fixed_params is None:
        fixed_params = [False] * len(popt)
    # To bootstrap error bars, we run 100 models with randomly sampled parameters and measure their spread
    for i in range(num_samples):
        sample = np.random.normal(loc=popt, scale=errors)
        for ind, param in enumerate(sample):
            if fixed_params[ind]:
                sample[ind] = popt[ind]
            # Make sure the randomly selected parameters fall within our bounds
            if param < fit_bounds[0][ind]:
                sample[ind] = fit_bounds[0][ind]
            elif param > fit_bounds[1][ind]:
                sample[ind] = fit_bounds[1][ind]
        y = run_model(fit_func, sample, t)
        all_samples.append(np.diff(y))

    all_samples = np.array(all_samples)
    # Get decile levels by taking the 10th through 90th percentile levels of our sample curves at each date
    all_deciles = np.transpose(np.array([np.percentile(all_samples, per, axis=0) for per in np.arange(10, 100, 10)]))
    # Remove any spurious negative values
    all_deciles[all_deciles < 0] = 0
    return all_deciles


def make_erf_quant_predictions(df, county_fips, key='deaths', last_date_pred='2020-06-30', start_date='2020-03-31',
                               boundary_date=None):
    '''
    df: main nyt data frame
    county_fips: fips code of the county to be fit
    key: 'deaths' for COVID-19 deaths, 'cases' for COVID-19 confirmed cases
    last_date_pred: last day to make predictions for. If 'None', stop at current day
    start_date: first date to list fitted values for. If 'None', start at beginning of dataframe. If do_diff is True,
        this should be one day before the first day you want difference values for
    boundary_date: date at which to cut off data used for fitting
    do_diff: if true, report the daily increase in cases/deaths rather than cumulative values
    '''
    num_days = int(utils.process_date(last_date_pred, df) - utils.process_date(start_date, df))
    data = utils.get_region_data(df, county_fips)
    if len(data) == 0:  # If there's no data for this FIPS, just return zeroes
        return np.zeros((num_days, 9))
    first_date_obv_proc = np.min(data['date_processed'].values)
    boundary = None if boundary_date is None else int(utils.process_date(boundary_date, df) - first_date_obv_proc + 1)

    x = data['date_processed'].values[:boundary]
    if len(x) == 0:  # If there's no data for this FIPS, just return zeroes
        return np.zeros((num_days, 9))
    if start_date is None:
        start_date_proc = first_date_obv_proc
    else:
        start_date_proc = utils.process_date(start_date, df)
    last_date_obv_proc = np.max(x)
    if last_date_pred is None:
        last_date_pred_proc = last_date_obv_proc
    else:
        last_date_pred_proc = utils.process_date(last_date_pred, df)

    y = data[key].values[:boundary]
    if np.max(y) == 0:  # If all data we have for this FIPS is zeroes, just return zeroes
        return np.zeros((num_days, 9))
    thresh_y = y[y >= 10]  # Isolate all days with at least 10 cases/deaths
    # If we have fewer than 5 days with substantial numbers of cases/deaths there isn't enough information to do an
    # erf fit, so just do a simple linear fit instead
    do_lin_model = len(thresh_y) < 5
    if do_lin_model:
        fit_func = lin_curve
        # Perform a linear fit on the latest 5 days of data
        fit_x, fit_y = x[-5:], y[-5:]
        # Pad with zeroes if we have fewer than 5 days of data
        if len(fit_x) < 5:
            fit_x = np.concatenate((np.zeros(5 - len(fit_x)), fit_x))
            fit_y = np.concatenate((np.zeros(5 - len(fit_y)), fit_y))
        fit_params0 = [0, 0]
        # The slope should be at least 0 and at most the largest 1-day increase
        # The intercept can be very low but shouldn't be above the minimum data value
        fit_bounds = [[0, -100 * np.max(y)], [max(1, np.max(np.diff(fit_y))), np.min(y)]]
    else:
        fit_func = erf_curve
        fit_x, fit_y = x, y
        fit_params0 = [np.log10(2 * np.max(data[key])), 0.1, 30]
        # The max value should be between the current max and 100x the current max
        # The slope was given a wide range around common values
        # The infection shouldn't peak before the data started or after the end of ~July
        fit_bounds = [bnd for bnd in zip(*[[np.log10(np.max(data[key])), np.log10(100 * np.max(data[key]))],
                                           [0.001, 10],
                                           [0, 200]])]
    # Use scipy to fit either a linear or erf model to the data
    popt, pcov = curve_fit(fit_func, fit_x, fit_y,
                           p0=fit_params0, bounds=fit_bounds)
    fixed_params = None
    if SPICY_ERF and (not do_lin_model) and popt[2] < np.max(x) - 10 and np.max(y) > 100:
        try:
            print('Erf2!', '%.1f' % popt[2], np.max(x), np.max(y))
            fit_func = erf2_curve
            fit_x, fit_y = x, y
            fit_params0 = [np.log10(2 * np.max(data[key])), np.log10(2 * np.max(data[key])), 0.1, 0.1, 80]
            fit_bounds = [bnd for bnd in zip(*[[np.log10(0.5 * np.max(data[key])), np.log10(3 * np.max(data[key]))],
                                               [np.log10(np.max(data[key])), np.log10(3 * np.max(data[key]))],
                                               [0.001, 10], [0.001, 10],
                                               [0, 200]])]
            popt, pcov = curve_fit(fit_func, fit_x, fit_y,
                                   p0=fit_params0, bounds=fit_bounds)
            fixed_params = [True, False, True, False, False]
        except RuntimeError as e:
            print(e)
            fit_func = erf_curve

    # Get error bars on the fitted parameters
    errors = np.sqrt(np.diag(pcov))

    # if all_deciles is None:
    t = np.arange(max(start_date_proc, first_date_obv_proc), last_date_pred_proc + 1)
    all_deciles = sample_bootstrap_err(t, fit_func, fit_bounds, popt, errors, fixed_params=fixed_params)

    # If data didn't start for this FIPS until after our start date, pad the beginning with zeroes
    if len(all_deciles) < num_days:
        all_deciles = np.concatenate((np.zeros((num_days - len(all_deciles), 9)), all_deciles))
    return all_deciles


def make_erf_point_predictions(df, county_fips, key='deaths', last_date_pred='2020-06-30', start_date='2020-03-31',
                               boundary_date=None, do_diff=True):
    '''
    df: main nyt data frame
    county_fips: fips code of the county to be fit
    key: 'deaths' for COVID-19 deaths, 'cases' for COVID-19 confirmed cases
    last_date_pred: last day to make predictions for. If 'None', stop at current day
    start_date: first date to list fitted values for. If 'None', start at beginning of dataframe. If do_diff is True,
        this should be one day before the first day you want difference values for
    boundary_date: date at which to cut off data used for fitting
    do_diff: if true, report the daily increase in cases/deaths rather than cumulative values
    '''
    num_days = int(utils.process_date(last_date_pred, df) - utils.process_date(start_date, df))
    data = utils.get_region_data(df, county_fips)
    if len(data) == 0:  # If there's no data for this FIPS, just return zeroes
        return np.zeros(num_days)
    first_date_obv_proc = np.min(data['date_processed'].values)
    boundary = None if boundary_date is None else int(utils.process_date(boundary_date, df) - first_date_obv_proc + 1)

    x = data['date_processed'].values[:boundary]
    if len(x) == 0:  # If there's no data for this FIPS, just return zeroes
        return np.zeros(num_days)
    if start_date is None:
        start_date_proc = first_date_obv_proc
    else:
        start_date_proc = utils.process_date(start_date, df)
    last_date_obv_proc = np.max(x)
    if last_date_pred is None:
        last_date_pred_proc = last_date_obv_proc
    else:
        last_date_pred_proc = utils.process_date(last_date_pred, df)

    y = data[key].values[:boundary]
    if np.max(y) == 0:  # If all data we have for this FIPS is zeroes, just return zeroes
        return np.zeros(num_days)
    thresh_y = y[y >= 10]  # Isolate all days with at least 10 cases/deaths
    # If we have fewer than 5 days with substantial numbers of cases/deaths there isn't enough information to do an
    # erf fit, so just do a simple linear fit instead
    do_lin_model = len(thresh_y) < 5
    if do_lin_model:
        fit_func = lin_curve
        # Perform a linear fit on the latest 5 days of data
        fit_x, fit_y = x[-5:], y[-5:]
        # Pad with zeroes if we have fewer than 5 days of data
        if len(fit_x) < 5:
            fit_x = np.concatenate((np.zeros(5 - len(fit_x)), fit_x))
            fit_y = np.concatenate((np.zeros(5 - len(fit_y)), fit_y))
        fit_params0 = [0, 0]
        # The slope should be at least 0 and at most the largest 1-day increase
        # The intercept can be very low but shouldn't be above the minimum data value
        fit_bounds = [[0, -100 * np.max(y)], [max(1, np.max(np.diff(fit_y))), np.min(y)]]
    else:
        fit_func = erf_curve
        fit_x, fit_y = x, y
        fit_params0 = [np.log10(2 * np.max(data[key])), 0.1, 30]
        # The max value should be between the current max and 100x the current max
        # The slope was given a wide range around common values
        # The infection shouldn't peak before the data started or after the end of ~July
        fit_bounds = [bnd for bnd in zip(*[[np.log10(np.max(data[key])), np.log10(100 * np.max(data[key]))],
                                           [0.001, 10],
                                           [0, 200]])]
    # Use scipy to fit either a linear or erf model to the data
    popt, pcov = curve_fit(fit_func, fit_x, fit_y,
                           p0=fit_params0, bounds=fit_bounds)
    t = np.arange(start_date_proc, last_date_pred_proc + 1)
    if do_diff:
        return np.diff(run_model(fit_func, popt, t))
    return run_model(fit_func, popt, t)


def predict_all_counties(df, last_date_pred='2020-06-30', out_file='erf_model_predictions.csv', boundary_date=None,
                         key='deaths'):
    out_dates = utils.all_output_dates()
    out_fips, all_row_starts = utils.all_output_fips('sample_submission.csv')
    num_dates, num_fips = len(out_dates), len(out_fips)
    out = np.zeros((num_dates * num_fips, 9))
    # Go through each county one by one, perform our fit, and record predictions
    for fi, fips in enumerate(out_fips):
        print('Processing FIPS', fips)
        preds = make_erf_quant_predictions(df, fips, last_date_pred=last_date_pred, boundary_date=boundary_date,
                                           key=key)
        # Indices are disjointed because we're recording a single FIPS on many different dates
        out[np.arange(fi, out.shape[0], num_fips)] = preds
    # Add in the header line
    out_lines = [','.join(['id'] + ['%d' % x for x in np.arange(10, 91, 10)]) + '\n']
    # Add in all other lines one at a time
    for row_head, row in zip(all_row_starts, out):
        out_lines.append(','.join([row_head] + ['%.2f' % val for val in row]) + '\n')
    with open(out_file, 'w') as f:
        f.writelines(out_lines)
    f.close()


if __name__ == '__main__':
    start = time.time()
    df = utils.get_processed_df()
    predict_all_counties(df, boundary_date='2020-05-15', out_file='erf_model_predictions_0515.csv',
                         key='deaths')
    print('Runtime: %.1f seconds' % (time.time() - start))
