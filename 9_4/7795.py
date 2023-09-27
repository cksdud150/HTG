import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t): # 이진탐색으로 해야하는데 그냥 완전탐색으로 함 pypy3로 해결함
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    b.sort(reverse=True)
    a.sort(reverse=True)
    result = 0
    for i in range(n):
        if a[i] < b[m-1]:
            break
        for j in range(m):
            if a[i] > b[j]:
                result += m-j
                break
    print(result)