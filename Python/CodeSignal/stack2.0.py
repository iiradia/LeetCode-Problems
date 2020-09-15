#!/bin/python

import sys



# Complete the function below.

def superStack(operations):

    stack = []

    for op in operations:

        if 'push' in op:
            stack.append(int(op.split(' ')[1]))
        elif 'pop' in op:
            stack.pop()
        elif 'inc' in op:
            command = op.split(' ')
            i = int(command[1])
            v = int(command[2])

            for j in range(0,i):
                stack[j] += v
        
        if len(stack) > 0:
            print(stack[-1])
        else:
            print('EMPTY')

if __name__ == "__main__":