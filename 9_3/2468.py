import sys
from collections import deque
input = sys.stdin.readline

def bfs(i,j,h):
    deq = deque()
    deq.append([i,j])
    while deq:
        now_i, now_j = deq.popleft()
        for next_i, next_j in [[now_i+1,now_j],[now_i,now_j+1],[now_i-1,now_j],[now_i,now_j-1]]:
            if 0 <= next_i < n and 0 <= next_j < n and board[next_i][next_j] > h and not visited[next_i][next_j]:
                visited[next_i][next_j] = 1
                deq.append([next_i,next_j])

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
small = min(map(min,board))
big = max(map(max,board))
result = 1 

for h in range(small,big+1):
    visited = [[0]*n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] > h:
                visited[i][j] = 1
                count += 1
                bfs(i,j,h)
    result = max(result,count)
print(result)