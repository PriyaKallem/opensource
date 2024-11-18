def highest_altitude(N,A):
    current_altitude=0
    highest_altitude=0
    for height in A:
        current_altitude+=height
        highest_altitude=max(highest_altitude,current_altitude)
    return highest_altitude
N=int(input())
A=list(map(int,input().split()))
print(highest_altitude(N,A))
