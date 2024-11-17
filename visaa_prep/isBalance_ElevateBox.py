s=int(input())
a=list(map(int,input().split()))
total_sum=sum(a)
left_wg=0
b=[]
for i in range(s):
    right_wg=total_sum-left_wg-a[i]
    b.append(abs(left_wg-right_wg))
    left_wg+=a[i]
print(" ".join(map(str,b)))
