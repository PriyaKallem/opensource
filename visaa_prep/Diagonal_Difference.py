import math
import os
import random
import re
import sys 
def diagonalDifference(arr):
    primary_diagonal=0
    secondary_diagonal=0
    n=len(arr)
    for i in range(n):
        primary_diagonal+=arr[i][i]
        secondary_diagonal+=arr[i][n-i-1]
    return abs(primary_diagonal-secondary_diagonal )
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
result = diagonalDifference(arr)
fptr.write(str(result) + '\n')
fptr.close()
