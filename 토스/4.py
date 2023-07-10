#4
from collections import defaultdict
def solution(maxSize, actions):
    now = ''
    back = []
    forward = []
    history = []
    for a in actions:
        if a == 'B':
            if not back:
                continue
            else:
                forward.append(now)
                now = back.pop()
                history.append(now)
                
        elif a == 'F':
            if not forward:
                continue
            else:
                back.append(now)
                now = forward.pop()
                history.append(now)
                
        else:
            if now:
                back.append(now)
            now = a
            history.append(now)
            forward = []

    answer = []
    dic = defaultdict(int)
    while len(answer) < maxSize:
        if not history:
            return answer
        temp = history.pop()
        if dic[temp]:
            continue
        else:
            answer.append(temp)
            dic[temp] = 1
    return answer