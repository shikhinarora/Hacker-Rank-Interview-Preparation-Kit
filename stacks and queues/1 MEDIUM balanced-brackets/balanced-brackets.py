#!/bin/python2

import math
import os
import random
import re
import sys


# Complete the isBalanced function below.
def isBalanced(s):
    stack = []

    for _ in s:
        if len(stack) >= 1:
            prev = stack[len(stack) - 1]
        else:
            prev = None

        if _ is '[' or _ is '{' or _ is '(':
            stack.append(_)

        if _ is ']' and prev is '[':
            stack.pop()

        if _ is '}' and prev is '{':
            stack.pop()

        if _ is ')' and prev is '(':
            stack.pop()

    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        s = raw_input()

        result = isBalanced(s)

        print result
