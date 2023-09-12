def recursion(zero_list, row, col, box):
    if not zero_list:
        for i in range(9):
            print(*board[i])
        exit(0)
    else:
        r, c, b = zero_list.pop()
        for i in range(1,10):
            if not row[r][i] and not col[c][i] and not box[b][i]:
                row[r][i] = 1
                col[c][i] = 1
                box[b][i] = 1
                board[r][c] = i
                recursion(zero_list.copy(),row,col,box)
                row[r][i] = 0
                col[c][i] = 0
                box[b][i] = 0
import sys
sys.setrecursionlimit(10000)

board = [list(map(int,input().split())) for _ in range(9)]
row = [[0]*10 for _ in range(9)] #숫자있는지 없는지 체크(로우단위)
col = [[0]*10 for _ in range(9)] #숫자있는지 없는지 체크(컬럼단위)
box = [[0]*10 for _ in range(9)] #숫자있는지 없는지 체크(박스단위)
zero_list = []



for i in range(9):
    for j in range(9):
        row[i][board[i][j]] = 1
        col[j][board[i][j]] = 1
        box[(i//3)*3+j//3][board[i][j]] = 1

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            # zero_list.append((max(sum(row[i]),sum(col[j]),sum(box[(i//3)*3+j//3])),i,j,(i//3)*3+j//3))
            zero_list.append((i,j,(i//3)*3+j//3))

# zero_list.sort(key = lambda x:x[0])
recursion(zero_list, row, col, box)
