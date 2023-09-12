import sys
input = sys.stdin.readline

n, d = map(int,input().split())
shortcut = []

for _ in range(n):
    start, end, distance = map(int,input().split())
    if end - start < distance or end > d: # 지름길이 원래길보다 긴경우 or 도착지점이 벗어나는경우
        continue
    else:
        shortcut.append((start,end,distance))

shortcut.sort(key = lambda x:(x[1],x[0],-x[2]))
i = 0 # shortcut 인덱스
result = [10000] * (d+1)
result[0] = 0
for j in range(1,d+1): # j는 현재 위치
    result[j] = result[j-1] + 1
    while i < len(shortcut) and j == shortcut[i][1]:
        result[j] = min(result[j],result[shortcut[i][0]] + shortcut[i][2])
        i += 1
    
print(result[d])