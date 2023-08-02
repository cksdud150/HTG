def dfs(A, depth):
    depth += 1
    if A > B:
        return 99999
    elif A == B:
        return depth
    else:
        return min(dfs(A*2, depth), dfs(A*10+1, depth))

A, B = map(int,input().split())
result = dfs(A,0)
print(result if result != 99999 else -1)