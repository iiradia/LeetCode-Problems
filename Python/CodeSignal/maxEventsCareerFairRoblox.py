#!/bin/python

import math
import os
import random
import re
import sys


#
# Complete the 'maxEvents' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arrival
#  2. INTEGER_ARRAY duration
#

def maxEvents(arrival, duration):
    # Write your code here

    events=0
    times = [(arrival[i], arrival[i] + duration[i]) for i in range(len(arrival))]

    times = sorted(times, key=lambda x:(x[0], x[1]))
    curr_time = times[0][1]
    invalid = []

    for time in times[1:]:

        if time[0] < curr_time:
            invalid.append(0)
        else:
            curr_time = time[1]
    
    events = len(arrival) - len(invalid)
    return events

if __name__ == '__main__':