#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.


def plusMinus(arr):
    m=0
    k=0
    j=0
    # Write your code here
    for i in range(0,n):
        if arr[i]<0:
            m+=1
        elif arr[i]>0:
            k+=1
        else:
            j+=1

    neg=m/n
    pos=k/n
    zero=j/n
    print("{:.6f}".format(pos),"\n","{:.6f}".format(neg),"\n","{:.6f}".format(zero))
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
