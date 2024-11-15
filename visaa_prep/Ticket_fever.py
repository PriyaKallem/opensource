M=int(input())
for _ in range(0,M):
    P,S=map(int,input().split())
    if P>S:
        print(P-S)
    else:
        print("0")
