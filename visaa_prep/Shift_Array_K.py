N=int(input())  
arr=list(map(int,input().strip().split()))
K=int(input())
K=K%N
rotated_array=arr[-K:]+arr[:-K]
print(' '.join(map(str,rotated_array)))
