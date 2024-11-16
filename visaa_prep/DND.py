def calculate_difference(n,m,arr):
    sum_divisible=0
    sum_not_divisible=0
    for num in arr:
        if num % m ==0:
            sum_divisible-=num
        else:
            sum_not_divisible-=num
    return sum_not_divisible-sum_divisible
n,m=map(int,input().split())
arr=map(int,input().split())
result=calculate_difference(n,m,arr)
print(result)
