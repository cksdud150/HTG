import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    arr = list(map(int,input().split()))
    deq = deque(enumerate(arr))
    result = 1
    while True:
        big = max(deq, key = lambda x: x[1])[1]
        now = deq.popleft()
        if now[1] == big: # 가장 큰값일 경우 일단 빼님
            if m == now[0]: # 원하는 문서의 경우 반복문 종료
                print(result)
                break
            else: 
                result += 1
        else: # 아닐경우 다시 que에 다시 넣음
            deq.append(now)