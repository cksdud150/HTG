# n = int(input())

# n_2 = 1
# n_1 = 2
# n_0 = 1
# if n == 1:
#     print(n_2)
#     exit(0)
# if n == 2:
#     print(n_1)
#     exit(0)
# for i in range(2,n):
#     n_0 = n_2 + n_1
#     n_2 = n_1
#     n_1 = n_0
#     if n_0 >= 15746:
#         n_0 %= 15746
# print(n_0)

n = int(input())
arr = [0] * 2
arr[0] = 1
arr[1] = 2
for i in range(2,n):
    arr.append((arr[i-1] + arr[i-2]) % 15746) # 피보나치 수열, 나머지 계산 안하면 메모리 초과 남
print(arr[n-1])