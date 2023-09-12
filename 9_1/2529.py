def recursion(i,kk,num,visited): # i는 현재 숫자, kk는 몇자리인지, num은 결과물용, visited는 방문 체크용
    visited[i] = kk #몇번째 위치에 있는지 하는걸로 처음 의도 했는데 지금은 딱히 필요 없을듯?
    # print(visited)
    global big, small
    if kk == k:
        big = max(num,big)
        small = min(num,small)
        return
    for j,v in enumerate(visited): #
        if v == -1:
            if operation[kk] == '>':
                if i > j:
                    recursion(j,kk+1,num+str(j),visited.copy())
            else:
                if i < j:
                    recursion(j,kk+1,num+str(j),visited.copy())

k = int(input())
operation = input().split()
visited = [-1] * 10 
big = '0'*k
small = '9'*k
for i in range(10):
    recursion(i,0,str(i),visited.copy())
print(big)
print(small)