import sys
from collections import deque
input = sys.stdin.readline

def bfs(i,j): #빙산이 몇개인지 찾음
    deq = deque([[i,j]])
    while deq:
        x,y = deq.popleft()
        for nx,ny in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
            if 0 <= nx < n and 0 <= ny < m:
                if ice[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    deq.append([nx,ny])


            
def melt(): #녹이는 과정
    melt_count = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp_count = 0
            if ice[i][j] != 0:
                for ni, nj in [[i+1,j],[i,j+1],[i-1,j],[i,j-1]]:
                    if 0<=ni<n and 0<=nj<m:
                        if ice[ni][nj] == 0:
                            temp_count += 1
                melt_count[i][j] = temp_count

    for i in range(n):
        for j in range(m):
            if melt_count[i][j] != 0:
                if melt_count[i][j] > ice[i][j]:
                    ice[i][j] = 0
                else:
                    ice[i][j] -= melt_count[i][j]

n, m = map(int,input().split())

ice = [list(map(int,input().split())) for _ in range(n)]


for t in range(3000): # 녹는데 걸리는시간이 상당히 오래걸릴수도 있음/ 녹이고 bfs 도는 것을 한번씩 반복
    count = 0
    melt() #녹이고
    # print(*ice,sep = '\n')
    # print()
    visited = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if ice[i][j] > 0 and not visited[i][j]:
                visited[i][j] = 1
                bfs(i,j)
                # print(*visited,sep = '\n')
                # print()
                count += 1
    if count > 1:
        print(t+1)
        exit(0)

print(0)