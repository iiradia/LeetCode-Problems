#!/bin/python

import math
import os
import random
import re
import sys



#
# Complete the 'deleteProducts' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ids
#  2. INTEGER m
#

def deleteProducts(ids, m):
    cts = sorted([(i, ids.count(i)) for i in set(ids)], key = lambda x: x[1])
    num = len(cts)

    for item in cts:

        if (m - item[1]) >= 0:
            num -= 1
            m -= item[1]
        else:
            break
    
    return num

if __name__ == '__main__': 