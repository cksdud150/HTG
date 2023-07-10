from collections import deque

n, m = map(int, input().split())
deq = deque([i for i in range(1, n + 1)])
arr = list(map(int, input().split()))
result = 0

#한방향으로 돌되 만약 반대방향으로 돌아야 하는거라면 전체길이에서 돌아야하는 횟수를 빼서 반대로 도는 것처럼 생각
for a in arr:
    temp = 0
    while True:
        now = deq.popleft()
        if now == a:
            temp = temp if temp <= (len(deq) + 1) // 2 else len(deq) + 1 - temp
            break
        else:
            temp += 1
            deq.append(now)
    result += temp
print(result)
