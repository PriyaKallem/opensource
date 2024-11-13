M,N,O=map(int,input().split())
time_required=M*N
available_time=O*24*60
if time_required<=available_time:
    print("YES")
else:
    print("NO")
