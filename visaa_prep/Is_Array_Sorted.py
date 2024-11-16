def is_sorted(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            return "false"
    return "true"
n=int(input())
arr=list(map(int,input().split()))
print(is_sorted(arr))
