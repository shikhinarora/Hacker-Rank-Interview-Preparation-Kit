#!/bin/python2

import math
import os
import random
import re
import sys


# Complete the countSwaps function below.
def countSwaps(a):
    swaps = 0

    for i in range(len(a)):
        for j in range(0, len(a) - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
                swaps += 1

    print 'Array is sorted in', swaps, 'swaps.'
    print 'First Element:', a[0]
    print 'Last Element:', a[-1]


if __name__ == '__main__':
    n = int(raw_input())

    a = map(int, raw_input().rstrip().split())

    countSwaps(a)