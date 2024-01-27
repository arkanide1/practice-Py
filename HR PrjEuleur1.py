#!/bin/python3

import sys


def evenSumFibo(N):
    a = 1
    b = 2
    s = 0
    while (b < N):
        if (b % 2 == 0):
            s += b
        a, b = b, a+b
    print(s)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    evenSumFibo(n)
