#!/bin/python3

import sys


def SumMulti3_5(n):
    s = 0
    for i in range(n):
        if (i % 3 == 0 or i % 5 == 0):
            s += i
    print(s)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    SumMulti3_5(n)
