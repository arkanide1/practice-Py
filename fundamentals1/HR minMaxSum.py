#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min,max=0,0
    arr_sorted = sorted(arr)
    
    count = 0
    while (count < 4):
        min+=arr_sorted[count]
        max+= arr_sorted[len(arr_sorted)-count-1]
        count+=1
    print(arr_sorted)
    print(min, max)




if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
