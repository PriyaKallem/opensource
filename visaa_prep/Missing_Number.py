import math
import os
import random
import re
import sys
from collections import Counter
def missingNumbers(arr, brr):
    arr_count=Counter(arr)
    brr_count=Counter(brr)
    missing=[]
    for num in brr_count:
        if brr_count[num]>arr_count[num]:
            missing.append(num)
    return sorted(missing)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    m = int(input().strip())
    brr = list(map(int, input().rstrip().split()))
    result = missingNumbers(arr, brr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
