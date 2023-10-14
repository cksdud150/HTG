from collections import deque

def bfs(i,j): 
    visited = [[0]*n for _ in range(n)] 
    deq = deque([[i,j,0]])
    visited[i][j] = 1
    flag = 0
    arr = []
    while deq:
        # print(deq)
        x,y,t = deq.popleft()
        if bowl[x][y] and bowl[x][y] < size:
            flag = 1
            arr.append([x,y,t])
        if not flag:
            for nx,ny in [[x-1,y],[x,y-1],[x+1,y],[x,y+1]]:
                if 0 <= nx < n and 0 <= ny < n:
                    if not visited[nx][ny] and bowl[nx][ny] <= size:
                        deq.append([nx,ny,t+1])
                        visited[nx][ny] = 1
    if arr:
        arr.sort(key = lambda x:(x[2],x[0],x[1]))
        bowl[arr[0][0]][arr[0][1]] = 0
        return arr[0][0], arr[0][1], arr[0][2]
    else:
        return 0,0,0 #잡아먹은 위치 + 몇초 걸렸는지

n = int(input())
bowl = [list(map(int,input().split())) for _ in range(n)]
size = 2
answer = 0
count = 0 # 몇마리 잡아먹고 있는지

flag = 0
for i in range(n): #초기위치 찾음
    for j in range(n):
        if bowl[i][j] == 9:
            bowl[i][j] = 0
            flag = 1
            break
    if flag:
        break
while True:
    i,j,t = bfs(i,j) # 한번 돌때 마다 한마리 잡아 먹음
    # print(i,j)
    # print(*bowl,sep='\n')
    if not t:
        break
    answer += t
    count += 1
    if count == size:
        size += 1
        count = 0
print(answer)    

