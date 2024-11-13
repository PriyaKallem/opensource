P,S,M=map(int,input().split())
if M%S==0 and M<=P*S:
    print("YES")
else:
    print("NO")
