import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * (n+1)
for i in range(1,n+1):
    arr[i] = max(arr[i],arr[i-1])
    t, p = map(int,input().split())
    if i+t-1 > n:
        continue
    arr[i+t-1] = max(arr[i-1]+p,arr[i+t-1])

print(arr[n])