#!/bin/python2

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglass_sum(array):
    sum_arr = []

    for i in range(0, 4):
        for j in range(0, 4):
            sum_arr.append(hg_sum_individual(i, j, array))

    print(sum_arr)

    return max(sum_arr)


def hg_sum_individual(row, column, array):
    s = 0
    s += array[row][column]
    s += array[row][column + 1]
    s += array[row][column + 2]
    s += array[row + 1][column + 1]
    s += array[row + 2][column]
    s += array[row + 2][column + 1]
    s += array[row + 2][column + 2]
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    result = hourglass_sum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
