#!/bin/python2

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    array = [0]*n

    for i in range(len(queries)):
        l = queries[i]
        start = l[0] - 1
        end = l[1] - 1
        ad = l[2]

        array[start] += ad
        if end < n-1: array[end + 1] -= ad

    total = 0
    m = 0
    for i in range(n):
        total += array[i]
        if total > m: m = total

    return m

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in xrange(m):
        queries.append(map(int, raw_input().rstrip().split()))
        #start, end, ad = map(int, raw_input().rstrip().split())

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
