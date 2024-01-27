#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    hh = int(s[0:2])
    mm = int(s[3:5])
    ss = int(s[6:8])
    time_format = s[8:10]

    if (time_format == "PM" and hh <12):
        hh = hh+12
        if (hh > 24 or (hh == 24 and mm > 0) or (hh == 24 and mm == 0 and ss >= 0)):
            hh = hh % 24
    elif time_format == "AM" and hh == 12:
        hh = 0

    if (hh < 10):
        hh = "0"+str(hh)
    if (mm < 10):
        mm = "0"+str(mm)
    if (ss < 10):
        ss = "0"+str(ss)

    s = str(hh)+":"+str(mm)+":"+str(ss)
    print( str(s) )


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    # fptr.write(result + '\n')

    # fptr.close()
