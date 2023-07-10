from collections import deque

n, m = map(int,input().split())
deq = deque([i for i in range(1,n+1)])
arr = list(map(int,input().split()))
result = 0

for a in arr:
    temp = 0
    while True:
        now = deq.popleft()
        if now == a:
            temp = temp if temp <= (len(deq)+1)//2 else len(deq)+1-temp
            break
        else:
            temp += 1
            deq.append(now)
    result += temp
print(result)