#!/bin/python2

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    moves = 0
    for i in range(len(q), 0, -1):
        for j in range(i-3, i):
            if q[j] == i:
                number = i
                position = j + 1

                diff = abs(number - position)

                if diff > 2:
                    return "Too chaotic"
                else:
                    if diff == 1:
                        q[j] = q[j + 1]
                        q[j + 1] = i
                        moves += 1
                    elif diff == 2:
                        q[j] = q[j + 1]
                        q[j + 1] = q[j + 2]
                        q[j + 2] = number
                        moves += 2
            elif j == i-1:
                return "Too chaotic"
            
    return moves
            

if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        print minimumBribes(q)
