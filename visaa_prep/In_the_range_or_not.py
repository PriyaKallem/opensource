def can_binary_hear(frequency):
    return 67<=frequency<=45000
T=int(input())
results=[]
for _ in range(T):
    X=int(input())
    if can_binary_hear(X):
        results.append("YES")
    else:
        results.append("NO")
for result in results:
    print(result)
