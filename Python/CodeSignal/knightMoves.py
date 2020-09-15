#!/bin/python

import math
import os
import random
import re
import sys



#
# Complete the 'minMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER startRow
#  3. INTEGER startCol
#  4. INTEGER endRow
#  5. INTEGER endCol
#
from collections import deque

def minMoves(n, startRow, startCol, endRow, endCol):
    visited_positions = {}
    valid_moves = [(1,2), (1,-2), (-1,2), (-1,-2), (2,-1), (-2,-1), (-2,1), (2,1)]
    moves = deque()
    moves.append((startRow, startCol, 0))

    while len(moves) > 0:

        curr = moves.popleft()
        row = curr[0]
        col = curr[1]
        num = curr[2]

        if row == endRow and col == endCol:
            return num

        if visited_positions.get((row, col)) is None:
            visited_positions[(row,col)] = 1
            
            # add each move to queue
            for move in valid_moves:

                x = row + move[0]
                y = col + move[1]
                if x >= 0 and y >= 0 and y < n and x < n:
                    moves.append((x,y,num+1))

    return -1

if __name__ == '__main__':