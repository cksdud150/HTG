#1
from collections import deque, defaultdict

def solution(s, N):
    if len(s) < N:
        return -1
    def is_ok(): #숫자를 하나씩 사용했는지 체크
        for j in range(1,N+1):
            if dic[str(j)] != 1:
                return False
        return True
    
    dic = defaultdict(int) #윈도우에 어떤 숫자들이 들어있는지 + 몇개가 들어있는지
    deq = deque() # 윈도우
    answer = ''

    for i in range(N): #초기화
        deq.append(s[i])
        dic[s[i]] += 1

    if is_ok():
        answer = ''.join(deq)

    for i in range(N,len(s)):
        deq.append(s[i])
        dic[s[i]] += 1
        dic[deq.popleft()] -= 1
        if is_ok():
            answer = answer if answer >= ''.join(deq) else ''.join(deq)
    if not answer:
        answer = -1
    return int(answer)