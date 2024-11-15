T=int(input())
results=[]
for _ in range(T):
    X,Y=map(int,input().split())
    results.append((X-Y)+1)
for result in results:
    print(result)
