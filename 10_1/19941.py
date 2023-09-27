#뭔가 느낌이 제일 왼쪽에 있는사람부터 제일 왼쪽에 있는거 먹이면 될거 같은 느낌이였음
n, k = map(int,input().split())
arr = list(input().rstrip())
result = 0
for i in range(n):
    if arr[i] == 'P':
        for j in range(max(i-k,0),min(i+k+1,n)):
            if arr[j] == 'H':
                result += 1
                arr[j] = 'X'
                break
print(result)