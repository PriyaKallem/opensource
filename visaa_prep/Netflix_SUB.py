X,Y,Z,A=map(int,input().split())
if (X+Y)>=A or (X+Z)>=A or (Y+Z)>=A:
    print("YES")
else:
    print("NO")
