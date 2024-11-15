N=int(input())
matrix=[]
for _ in range(N):
    row=list(map(int,input().split()))
    matrix.append(row)
transpose=[]
for col in range(N):
    new_row=[matrix[row][col]for row in range(N)]
    transpose.append(new_row)
for row in transpose:
    print(" ".join(map(str,row)))
