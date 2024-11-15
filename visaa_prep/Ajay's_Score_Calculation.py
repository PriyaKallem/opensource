T=int(input().strip())
results=[]
for _ in range(T):
    X,N=map(int,input().strip().split())
    Score=(X//10)*N
    results.append(Score)
for result in results:
    print(result)
