import function
from env import time_resolution,pair_list
for pair in pair_list:
    function.historical_data(pair,time_resolution)