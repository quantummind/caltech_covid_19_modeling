import git
import numpy as np
import pandas as pd


def get_processed_df(file_name='nyt_us_counties.csv'):
    repo = git.Repo("./", search_parent_directories=True)
    homedir = repo.working_dir
    datadir = f"{homedir}/data/us/covid/"
    df = pd.read_csv(datadir + file_name)
    df['date_processed'] = pd.to_datetime(df['date'].values)
    # Convert YYYY-MM-DD date format into integer number of days since the first day in the data set
    df['date_processed'] = (df['date_processed'] - df['date_processed'].min()) / np.timedelta64(1, 'D')
    # Special correction for the NYT data set
    df.loc[df['county'] == 'New York City', 'fips'] = 36061.
    return df


def process_date(date_str, df):
    return (pd.to_datetime(date_str) - pd.to_datetime(df['date'].values).min()) / np.timedelta64(1, 'D')


def get_region_data(df, county_fips, proc_date=None, key='deaths'):
    county_fips = float(county_fips)
    d = df.loc[df['fips'] == county_fips]
    if proc_date is not None:
        vals = d.loc[d['date_processed'] == proc_date][key].values
        if len(vals) == 0:
            return 0.0
        return vals[0]
    return d


def all_output_dates():
    ret = ['2020-04-%02d' % x for x in range(1, 31)]
    ret += ['2020-05-%02d' % x for x in range(1, 32)]
    ret += ['2020-06-%02d' % x for x in range(1, 31)]
    return ret


def all_fips_in_df(df):
    # Get a sorted list of all FIPS string codes in a dataframe
    return sorted(list(set(['%d' % x for x in df['fips'].values if not np.isnan(x)])))


def all_output_fips(sample_out_file):
    # Get a sorted list of all FIPS codes in the sample output file
    repo = git.Repo("./", search_parent_directories=True)
    homedir = repo.working_dir
    datafile = f"{homedir}/" + sample_out_file
    all_data = np.genfromtxt(datafile, delimiter=',', dtype='str')
    all_fips = set([x.split('-')[-1] for x in all_data[1:, 0]])
    return sorted(list(all_fips)), all_data[1:, 0]


def fill_missing_dates(t, y):
    # If a time series is missing days, fill those missing days with a copy of the most recent value
    ret_t = np.arange(np.min(t), np.max(t) + 1)
    ret_y = np.zeros(len(ret_t))
    dat_ind = 0
    for ret_ind in range(len(ret_t)):
        if ret_t[ret_ind] in t:
            ret_y[ret_ind] = y[dat_ind]
            dat_ind += 1
        else:
            ret_y[ret_ind] = ret_y[ret_ind - 1]
    return ret_t, ret_y
