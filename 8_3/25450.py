import sys
input = sys.stdin.readline

n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            temp = 0
        elif i == 0:
            temp = board[i][j-1]
        elif j == 0:
            temp = board[i-1][j]
        else:
            temp = min(board[i][j-1],board[i-1][j]) # 왼쪽이랑 위쪽 비교 해서 작은 값하고 현재값하고 비교해서 업데이트함
        board[i][j] += temp
        # print(*board,sep = '\n')
        # print()
h = int(input())
if h < board[n-1][m-1]:
    print('NO')
else:
    print('YES')
    print(board[n-1][m-1])