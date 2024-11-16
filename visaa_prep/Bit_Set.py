def is_kth_bit_set(N,k):
    if N & (1<<(k-1))!=0:
        return "true"
    else:
        return "false"       
N=int(input())
k=int(input())
print(is_kth_bit_set(N,k))
