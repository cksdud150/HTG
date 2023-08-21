import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t): #조합 계산 bCa 계산
    a,b = map(int,input().split())
    result = 1
    for i in range(b-a+1,b+1):
        result *= i
    for j in range(2,a+1):
        result //= j
    print(result)