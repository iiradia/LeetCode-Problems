#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isPangram' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY pangram as parameter.
#

def isPangram(pangram):
    
    
    # return value
    output = ""
    
    # go through each item in input
    for phrase in pangram:
        
        # get letters in phrase
        curr_letters = {}
        
        # go through each character
        for char in phrase:
            
            if curr_letters.get(char.lower()) is None and char.lower() != ' ':
                curr_letters[char.lower()] = 1
    
        
        # decide whether phrase is pangram
        if len(curr_letters) == 26:
            output += '1'
        else:
            output += '0'
                
    
    return output
