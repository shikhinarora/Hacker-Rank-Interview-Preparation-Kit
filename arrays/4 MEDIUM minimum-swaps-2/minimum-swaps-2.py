#!/bin/python2

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0

    for i in range(len(arr)):
        while arr[i] != i + 1:
            pos1 = i
            pos2 = arr[i] - 1
            temp = arr[pos1]
            arr[pos1] = arr[pos2]
            arr[pos2] = temp
            swaps += 1

    return swaps
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
