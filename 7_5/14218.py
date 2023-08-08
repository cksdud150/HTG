import sys
from collections import defaultdict
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int,input().split())
dic = defaultdict(list)
arr = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    dic[a].append(b)
    dic[b].append(a)
    arr[a][b] = 1
    arr[b][a] = 1


for i in range(n+1):
    arr[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            arr[i][j] = min(arr[i][j],arr[i][k]+arr[k][j]) #플루이드 알고리즘

q = int(input())

for _ in range(q):
    a, b = map(int,input().split())
    arr[a][b] = 1
    arr[b][a] = 1
    for i in range(1,n+1):
        for j in range(1,n+1):
            arr[i][j] = min(arr[i][j], arr[i][a]+arr[b][j]+1, arr[i][b]+arr[a][j]+1)
            arr[j][i] = min(arr[j][i], arr[j][a]+arr[b][i]+1, arr[j][b]+arr[a][i]+1)
    for i in range(1,n+1):
        print(arr[i][1] if arr[i][1] != INF else -1, end = ' ')
    # print(*arr, sep = '\n')
    print()