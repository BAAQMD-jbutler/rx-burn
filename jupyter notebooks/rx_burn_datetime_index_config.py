"""
Indexing Datetimes for Prescribed Burn Sampling
April 2021 Blodgett Forest Research Station

Author: James Butler
Email: jdabutler@berkeley.edu
Github: @BAAQMD-jbutler

Usage:
    from date_indices import *
    # or
    import date_indices as dates
    # then use: dates.d1b, dates.d2S, etc.
"""

import pandas as pd

# Day 1 - April 20, 2021
d1be = pd.to_datetime('2021-04-20 11:56')  # day 1 begin with tube error
d1cs = pd.to_datetime('2021-04-20 12:52')  # day 1 cell switch from cell 138 to cell 52
d1b = pd.to_datetime('2021-04-20 13:23')   # day 1 begin with tube error fixed
d1co = pd.to_datetime('2021-04-20 15:01')  # day 1 ABCD and cell 52 turned off
d1s = pd.to_datetime('2021-04-20 16:33')   # day 1 smolder begins at new location after filter changes from UCR sampling team
d1E = pd.to_datetime('2021-04-20 17:45')   # day 1 AE33 sampling end

# Day 2 - April 21, 2021
d2S = pd.to_datetime('2021-04-21 11:07')   # day 2 next day smolder begins and AE33 turned on
d2b = pd.to_datetime('2021-04-21 11:35')   # day 2 next day smolder ends and burn begins
d2b2 = pd.to_datetime('2021-04-21 13:53')  # day 2 new location burn start
d2cs = pd.to_datetime('2021-04-21 14:57')  # day 2 cell switch from cell 133 to cell 138
d2s = pd.to_datetime('2021-04-21 16:00')   # day 2 smolder begins
d2e = pd.to_datetime('2021-04-21 16:57')   # day 2 ABCD turned off
d2E = pd.to_datetime('2021-04-21 19:03')   # day 2 AE33 sampling end

# Day 3 - April 22, 2021
d3S = pd.to_datetime('2021-04-22 10:47')   # day 3 background and AE33 sampling begin
d3c = pd.to_datetime('2021-04-22 11:02')   # day 3 ABCD turned on
d3b = pd.to_datetime('2021-04-22 11:20')   # day 3 burn begins
d3be = pd.to_datetime('2021-04-22 14:35')  # day 3 burn ends
d3s = pd.to_datetime('2021-04-22 15:36')   # day 3 smolder begins
d3e = pd.to_datetime('2021-04-22 23:00')   # day 3 ABCD turned off

# Day 4 - April 23, 2021
d4c = pd.to_datetime('2021-04-23 10:00')   # day 4 ABCD turned on and ABCD sampling begin
d4b1 = pd.to_datetime('2021-04-23 10:34')  # day 4 background sample ends burn begins
d4b1e = pd.to_datetime('2021-04-23 11:55') # day 4 burn 1 location ends
d4b2 = pd.to_datetime('2021-04-23 12:09')  # day 4 new location burn start
d4s = pd.to_datetime('2021-04-23 14:00')   # day 4 smolder emission begin
d4e = pd.to_datetime('2021-04-23 23:00')   # day 4 ABCD turned off


# Create a dictionary for easy lookup
date_dict = {
    # Day 1
    'd1be': d1be, 'd1cs': d1cs, 'd1b': d1b, 'd1co': d1co, 'd1s': d1s, 'd1E': d1E,
    # Day 2
    'd2S': d2S, 'd2b': d2b, 'd2b2': d2b2, 'd2cs': d2cs, 'd2s': d2s, 'd2e': d2e, 'd2E': d2E,
    # Day 3
    'd3S': d3S, 'd3c': d3c, 'd3b': d3b, 'd3be': d3be, 'd3s': d3s, 'd3e': d3e,
    # Day 4
    'd4c': d4c, 'd4b1': d4b1, 'd4b1e': d4b1e, 'd4b2': d4b2, 'd4s': d4s, 'd4e': d4e
}


def print_dates():
    """Print all dates with their descriptions."""
    for key, value in date_dict.items():
        print(f"{key}: {value}")
