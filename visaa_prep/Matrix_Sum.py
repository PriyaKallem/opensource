N=int(input().strip())
matrix=[]
for _ in range(N):
    row=list(map(int,input().strip().split()))
    matrix.append(row)
row_sums=[0]*N
col_sums=[0]*N
for i in range(N):
    for j in range(N):
        row_sums[i]+=matrix[i][j]
        col_sums[j]+=matrix[i][j]
A=[0]*N
for i in range(N):
    A[i]=row_sums[i]+col_sums[i]
print(" ".join(map(str,A)))
