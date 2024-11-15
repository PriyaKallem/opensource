N=int(input())
arr=list(map(int,input().split()))
unique_elements=[]
seen=set()
for num in arr:
    if num not in seen:
        unique_elements.append(num)
        seen.add(num)
print(" ".join(map(str,unique_elements)))
