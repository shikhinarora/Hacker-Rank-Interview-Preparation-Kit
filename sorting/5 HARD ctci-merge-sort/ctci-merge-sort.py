#!/bin/python2

import math
import os
import random
import re
import sys

count = 0


# Complete the countInversions function below.
def countInversions(arr):
    mergeSort(arr)

    return count


def mergeSort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr) / 2
        return merge(mergeSort(arr[:mid]), mergeSort(arr[mid:]))


def merge(a1, a2):
    comb = []

    i, j, k = 0, 0, 0

    la1 = len(a1)
    la2 = len(a2)

    while i < la1 and j < la2:
        elemA = a1[i]
        elemB = a2[j]

        if elemA > elemB:
            comb.append(elemB)
            j += 1
            global count
            count += la1 - i
        else:
            comb.append(elemA)
            i += 1

    while i < la1:
        comb.append(a1[i])
        i += 1

    while j < la2:
        comb.append(a2[j])
        j += 1

    # while len(comb) != la1+la2:
    #     if len(a1) == 0:
    #         comb.extend(a2)
    #         a2 = []
    #     elif len(a2) == 0:
    #         comb.extend(a1)
    #         a1 = []
    #     else:
    #         elemA = a1[0]
    #         elemB = a2[0]
    #
    #         if elemA > elemB:
    #             comb.append(elemB)
    #             del a2[0]
    #             global count
    #             count += len(a1)
    #         else:
    #             comb.append(elemA)
    #             del a1[0]

    return comb


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        arr = map(int, raw_input().rstrip().split())

        global count
        count = 0

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
