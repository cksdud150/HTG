# 녹이고 bfs 한번씩 반복
# import sys
# from collections import deque
# input = sys.stdin.readline

# def melt():
#     melt_point = []
#     for i in range(r):
#         for j in range(c):
#             if ice[i][j] == 'X':
#                 for ni, nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
#                     if 0<=ni<r and 0<=nj<c and ice[ni][nj] == '.':
#                         melt_point.append([i,j])
#                         break
#     for i, j in melt_point:
#         ice[i][j] = '.'

# def bfs():
#     deq = deque([[bird[0][0],bird[0][1]]])
#     visited = [[0]*c for _ in range(r)]
#     visited[bird[0][0]][bird[0][1]] = 1
    
#     while deq:
#         i, j = deq.popleft()
#         for ni, nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
#             if 0<=ni<r and 0<=nj<c:
#                 if ice[ni][nj] != 'X' and visited[ni][nj] == 0:
#                     if ice[ni][nj] == 'L':
#                         return True
#                     visited[ni][nj] = 1
#                     deq.append([ni,nj])
#     return False

# r, c = map(int,input().split())

# ice = [list(input().rstrip()) for _ in range(r)]
# bird = []
# count = 0

# for i in range(r):
#     for j in range(c):
#         if ice[i][j] == 'L':
#             bird.append([i,j])
#             break

# while True:
#     if bfs():
#         break
#     else:
#         melt()
#         count += 1
        
# print(count)

# 먼저 다녹이고 BFS를 도는 데 그 때 힙으로
# import sys, heapq
# from collections import deque
# input = sys.stdin.readline

# def melt():
#     melt_point = deque()
#     for i in range(r):
#         for j in range(c):
#             if ice[i][j] == 'X':
#                 for ni, nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
#                     if 0<=ni<r and 0<=nj<c and not ice[ni][nj]:
#                         melt_point.append([i,j])
#                         ice[i][j] = 1
#                         break
#     while melt_point:
#         i, j = melt_point.popleft()
#         for ni, nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
#             if 0<=ni<r and 0<=nj<c and ice[ni][nj] == 'X':
#                 melt_point.append([ni,nj])
#                 ice[ni][nj] = ice[i][j] + 1


# r, c = map(int,input().split())

# ice = [list(input().rstrip()) for _ in range(r)]
# bird = []

# for i in range(r):
#     for j in range(c):
#         if ice[i][j] == 'L':
#             bird.append([i,j])
#         if ice[i][j] != 'X':
#             ice[i][j] = 0

# melt()

# h = [[ice[bird[0][0]][bird[0][1]],bird[0][0],bird[0][1]]]
# visited = [[0]*c for _ in range(r)]
# visited[bird[0][0]][bird[0][1]] = 1
# big = 0

# while h:
#     v, i, j = heapq.heappop(h)
#     big = max(v,big)
#     for ni, nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
#         if 0<=ni<r and 0<=nj<c and not visited[ni][nj]:
#             visited[ni][nj] = 1
#             if ni == bird[1][0] and nj == bird[1][1]:
#                 h = []
#                 break
#             else:
#                 heapq.heappush(h,[ice[ni][nj],ni,nj])

# print(big)

# 먼저 다녹이고 BFS를 도는 데 그 때 이중큐로
import sys
from collections import deque
input = sys.stdin.readline

def melt():
    melt_point = deque()
    for i in range(r): # 첫날 녹을 애
        for j in range(c):
            if ice[i][j] == 'X':
                for ni, nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                    if 0<=ni<r and 0<=nj<c and not ice[ni][nj]:
                        melt_point.append([i,j])
                        ice[i][j] = 1
                        break
    while melt_point: # 다음날 녹을 곳 찾는 과정
        i, j = melt_point.popleft()
        for ni, nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
            if 0<=ni<r and 0<=nj<c and ice[ni][nj] == 'X':
                melt_point.append([ni,nj])
                ice[ni][nj] = ice[i][j] + 1


r, c = map(int,input().split())

ice = [list(input().rstrip()) for _ in range(r)]
bird = []

for i in range(r):
    for j in range(c):
        if ice[i][j] == 'L':
            bird.append([i,j])
        if ice[i][j] != 'X':
            ice[i][j] = 0

melt()
print(*ice,sep='\n')

que = deque([bird[0]]) # 내가 방문할 친구들
que2 = deque() # 하루 지나고 방문할 친구들
visited = [[0]*c for _ in range(r)]
visited[bird[0][0]][bird[0][1]] = 1
day = 0

while True:
    if not que:
        if not que2:
            break
        else:
            que = que2
            que2 = deque()
            day += 1
    i, j = que.popleft()
    for ni, nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
        if 0<=ni<r and 0<=nj<c and not visited[ni][nj]:
            visited[ni][nj] = 1
            if ice[ni][nj] <= day:
                que.append([ni,nj])
            else:
                que2.append([ni,nj])
            if ni == bird[1][0] and nj == bird[1][1]:
                que = []
                que2 = []
                break

print(day)