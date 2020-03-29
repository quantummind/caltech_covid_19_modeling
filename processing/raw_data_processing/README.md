## `raw_data_processing`

Run `./daily_refresh.sh` to update COVID data.

Some common errors:

1. Earliest date that can be fetched from JHU data is YESTERDAY's date, not today's.

2. Be sure the scripts are running Python 3. `./daily_refresh.sh` calls `python` on the python scripts. In cases where your `python` is binded to Python 2, you might need to explicitly specify `python3` and `pip3` instead of the respective python or pip calls in order for Python 3 to see the packages.

3. Need to install us and git python packages: `pip install us` and `pip install GitPython`. 

4. Pandas error where `TypeError: data type "string" not understood` : Need to upgrade your version of Pandas to latest version: `pip install pandas --upgrade`
