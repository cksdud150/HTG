n = int(input())
arr = [int(input()) for _ in range(n)]
arr = arr[::-1]
result = 0

for i in range(1,n):
    if arr[i-1] <= arr[i]:
        result += arr[i] - arr[i-1] + 1
        arr[i] = arr[i-1] - 1
print(result)