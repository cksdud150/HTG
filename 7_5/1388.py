import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())

board = [list(input().rstrip()) for _ in range(n)]
deq = deque()
result = 0


for i in range(n):
    for j in range(m):
        if board[i][j] != -1:
            result += 1
            deq.append((i,j))
            temp = board[i][j]
            board[i][j] = -1
            while deq:
                now = deq.popleft()
                try : # 범위벗어나는거 처리용
                    if temp == '-': #오른쪽으로만 증가하게 만듦
                        if board[now[0]][now[1]+1] == '-':
                            deq.append((now[0],now[1]+1))
                            board[now[0]][now[1]+1] = -1
                    if temp == '|': #아래쪽으로만 증가하게 만듦
                        if board[now[0]+1][now[1]] == '|':
                            deq.append((now[0]+1,now[1]))
                            board[now[0]+1][now[1]] = -1
                except:
                    pass
                    
print(result)