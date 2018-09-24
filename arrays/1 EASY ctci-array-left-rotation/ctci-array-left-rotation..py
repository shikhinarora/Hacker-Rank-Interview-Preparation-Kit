#!/bin/python2

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    temp = a[0:d]
    
    for i in range(len(a) - d):
        a[i] = a[i+d]
    a[len(a) - d:len(a)] = temp
        
        
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, raw_input().rstrip().split())

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
