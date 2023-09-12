from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline
h = []
dic = defaultdict(list)

n,m = map(int,input().split())

for _ in range(m):
    s,e,c = map(int,input().split())
    dic[s].append((c,e))
    dic[e].append((c,s))

result = [50000000]*(n+1)
visited = [0]*(n+1)
result[1] = 0
heapq.heappush(h,(0,1))


while h:
    # print(result)
    now = heapq.heappop(h)
    visited[now[1]] = 1
    for c2, e2 in dic[now[1]]:
        if not visited[e2]:
            if result[now[1]] + c2 < result[e2]:
                result[e2] = result[now[1]] + c2
                heapq.heappush(h,(result[e2],e2))
print(result[n])