import math
x,N=map(int,input().strip().split())
total_planes_needed=math.ceil(N/100)
new_planes=max(0,total_planes_needed-x)
print(new_planes)
