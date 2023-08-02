def is_ok(k): # 적절한한가 k길이로 모든 강의 담을수 있는가
    kk = k # kk는 남은 블루레이 길이
    mm = m # mm은 남은 블루레이 개수
    for a in arr:
        if k < a:
            return False
        if kk >= a:
            kk -= a
        else:
            kk = k - a
            mm -= 1
        if mm <= 0:
            return False
    return True


def bisearch(start, end): #이진탐색
    if start > end:
        return 100000000001
    mid = (start + end) // 2
    if is_ok(mid):
        return min(mid, bisearch(start, mid - 1))
    else:
        return bisearch(mid + 1, end)


n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(bisearch(1, 100000000000))
