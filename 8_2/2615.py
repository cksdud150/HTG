def check(i,j,d,k,c): # 오목인지 아닌지 체크 / i,j는 돌위치  / d는 방향 키패드 방향을 뜻함 / k는 몇번째 인지 나타냄 / c는 돌 색깔 
#    print(i,j,d,k,c)
    if d == 5: # 방향 안정해진 상태
        for idx, next in enumerate(((i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1))):
            try:
                if c == board[next[0]][next[1]] and not visited[next[0]][next[1]][idx]: # 같은 숫자이고 방문 안했을 경우 재귀 시작
                    visited[i][j][idx] = 1
                    if check(next[0],next[1],idx+6,k+1,c):
                        if idx == 1 : # 처음에 6789 방향으로 진행했는데 3689 방향으로 진행했어야함 6789로 그대로 진행하기 위해서 왼쪽 아래에 있는 위치 계산해서 출력
                            print(board[i][j])
                            print(i+5,j-3)
                            exit(0)
                        else:
                            print(board[i][j])
                            print(i+1,j+1)
                            exit(0)
            except IndexError as e:
                pass
        return False
    else:
        try:
            visited[i][j][d-6] = 1
            if d == 6:
                if c == board[i][j+1]: # 다음 위치 돌 색이 같은지 확인
                    return check(i,j+1,6,k+1,c)
                else:
                    if k == 5: # 5번째 일때 다음위치가 틀린경우 이므로 True 리턴
                        return True
                    else:
                        return False
            elif d == 7:
                if c == board[i+1][j-1]:
                    return check(i+1,j-1,7,k+1,c)
                else:
                    if k == 5:
                        return True
                    else:
                        return False
            elif d == 8:
                if c == board[i+1][j]:
                    return check(i+1,j,8,k+1,c)
                else:
                    if k == 5:
                        return True
                    else:
                        return False
            elif d == 9:
                if c == board[i+1][j+1]:
                    return check(i+1,j+1,9,k+1,c)
                else:
                    if k == 5:
                        return True
                    else:
                        return False
        except:
            if k == 5:
                return True
            else:
                return False

import sys
input = sys.stdin.readline

board = [list(map(int,input().split())) for _ in range(19)]
visited = [[[0]*4 for _ in range(19)] for _ in range(19)] # 4가지방향으로 방문했었는지 체크

for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            check(i,j,5,1,board[i][j])
print(0)