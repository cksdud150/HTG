t = int(input())
m = int(input())
arr = [[0]*4 for _ in range(4)]
dic = {'A':0,'B':1,'C':2,'D':3}

for _ in range(m):
    s, e, p = input().split()
    arr[dic[s]][dic[e]] = float(p) # i에서 j로 갈 확률이 들어있는 배열

prob = [25]*4 # 현재자리에 있을 확률

for _ in range(t):
    temp = [0]*4 # 다음턴에 있을 확률
    for i in range(4): # 현재위치
        for j in range(4): # 다음턴에 갈 위치
            temp[j] += arr[i][j]*prob[i] # i는 현재 위치 j는 다음 위치
    prob = temp # 다음턴
print(*list(map(lambda x: round(x,2),prob)))