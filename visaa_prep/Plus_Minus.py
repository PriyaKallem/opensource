import math
import os
import random
import re
import sys
def plusMinus(arr):
    n=len(arr)
    positive=sum(1 for x in arr if x>0)
    negative=sum(1 for x in arr if x<0)
    zero=sum(1 for x in arr if x==0)
    print(f"{positive/n:.6f}")
    print(f"{negative/n:.6f}")
    print(f"{zero/n:.6f}")
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
