#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'prison' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER_ARRAY h
#  4. INTEGER_ARRAY v
#

def prison(n, m, h, v):
    
    # create array for vertical and horizontal bars
    gate_horiz = [1 for i in range(n)]
    gate_vertical = [1 for j in range(m)]
    
    # set gates such that 0 indicates a hole
    for index in h:
        gate_horiz[index-1] = 0
    for index in v:
        gate_vertical[index-1] = 0
    
    # now find the largest hole in each gate
    max_hole_horiz = 0
    curr = 0
    for num in gate_horiz:
        if num == 0:
            curr += 1
            max_hole_horiz = max(curr, max_hole_horiz) 
        else:
            curr = 0
    
    # find the largest hole in vertical gate
    max_hole_vertical = 0
    curr = 0
    for num in gate_vertical:
        if num == 0:
            curr += 1
            max_hole_vertical = max(curr, max_hole_vertical) 
        else:
            curr = 0
    
    # return area of largest overall hole
    return (max_hole_horiz + 1) * (max_hole_vertical + 1)

if __name__ == '__main__':


prison break max hole