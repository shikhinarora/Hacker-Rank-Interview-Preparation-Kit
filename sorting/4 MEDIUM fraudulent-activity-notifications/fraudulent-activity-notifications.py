#!/bin/python2

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    med = []
    count = [0] * 201
    total = 0

    for index, elem in enumerate(expenditure):
        if len(med) >= d:
            total += sendNote(count, d, elem)

        addnMed(count, med, d, elem)

    return total


def addnMed(count, med, d, number):
    med.append(number)
    count[number] += 1

    if len(med) > d:
        count[med[0]] -= 1
        del med[0]


def sendNote(count, d, number):
    a = d/2
    b = a + 1
    first = 0
    second = 0

    pos = 0
    for index, elem in enumerate(count):
        pos += elem

        if pos >= a and first == 0:
            first = index

        if pos >= b:
            second = index
            break

    if d % 2 == 0:
        med = (first + second) / 2
        limit = first + second
    else:
        med = second
        limit = 2 * second

    if number >= limit:
        return 1
    else:
        return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = map(int, raw_input().rstrip().split())

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
