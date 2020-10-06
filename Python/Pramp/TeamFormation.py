#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'teamFormation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY score
#  2. INTEGER team_size
#  3. INTEGER k
#

def teamFormation(score, team_size, k):
    
    # keep array of selected employees
    selected = []
    
    while len(selected) < team_size:
        
        max_score_employee = score[0]
        max_idx = 0
        
        for i in range(len(score)):
            
            if i < k or i >= (len(score) - k):
                
                score_value = score[i]
                
                # find max within bound of k
                if score_value > max_score_employee:
                    
                    max_score_employee = score_value
                    max_idx = i
        
        # remove the element from the list
        score.pop(max_idx)
        
        # add max score to list
        selected.append(max_score_employee)
            
        
    # return sum score of selected employees
    return sum(selected)

if __name__ == '__main__':