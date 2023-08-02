def change(i,j): # 3X3을 바꾸는 함수
    for ni in (i-1,i,i+1):
        for nj in (j-1,j,j+1):
            A[ni][nj] = (A[ni][nj] + 1)%2

import sys

input = sys.stdin.readline

n,m = map(int,input().split())
A = [list(map(int,input().rstrip())) for _ in range(n)]
B = [list(map(int,input().rstrip())) for _ in range(n)]
result = 0

for i in range(1,n-1):
    for j in range(1,m-1):
        if A[i-1][j-1] != B[i-1][j-1]:
            change(i,j)
            result += 1
    for j in range(m-2,m):
        if A[i-1][j] != B[i-1][j]:
            print(-1)
            exit(0)


for i in range(n-2,n):
    for j in range(m):
        if A[i][j] != B[i][j]:
            print(-1)
            exit(0)
print(result)