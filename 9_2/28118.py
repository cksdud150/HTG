# 그룹이 몇개 나오는지가 비용과 연관되어 있음 그룹이 1개면 비용 0 그룹이 1개 늘어날수록 1개씩 비용 발생
def bfs(i):
    visited[i] = 1
    deq = deque([i])
    while deq:
        now = deq.popleft()
        for next in dic[now]:
            if not visited[next]:
                deq.append(next)
                visited[next] = 1
                
import sys 
from collections import defaultdict, deque
input = sys.stdin.readline

n,m = map(int,input().split())
dic = defaultdict(list)
visited = [0] *(n+1)
result = -1

for _ in range(m):
    a,b = map(int,input().split())
    dic[a].append(b)
    dic[b].append(a)
print(dic)
for i in range(1,n+1):
    if not visited[i]:
        bfs(i)
        result += 1

print(result)
