from collections import defaultdict, deque

def solution(relationships, target, limit):
    dic = defaultdict(list)
    for a,b in relationships:
        dic[a].append(b)
        dic[b].append(a)
    stage = [-1]*101
    stage[target] = 0

    deq = deque()
    deq.append(target)

    while deq:
        now = deq.popleft()
        for n in dic[now]:
            if stage[n] == -1 and stage[now] < limit:
                stage[n] = stage[now] + 1
                deq.append(n)
    
    origin = 0
    new = 0
    for i in range(1,101):
        if stage[i] == 1:
            origin += 1
        elif stage[i] > 1:
            new += 1
    answer = origin*5+new*10+new
    return answer
