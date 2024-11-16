def max_triangle_perimeter(n,lengths):
    lengths.sort()
    for i in range(n-1,1,-1):
        if lengths[i-2]+lengths[i-1]>lengths[i]:
            return lengths[i-2]+lengths[i-1]+lengths[i]
    return -1
n=int(input())
lengths=list(map(int,input().split()))
result=max_triangle_perimeter(n,lengths)
print(result)
