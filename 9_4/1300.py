# import heapq

# n = int(input())
# k = int(input())

# i = 2
# h = [[1,1,1]] # 현재값, 행, 열

# for _ in range(k):
#     now = heapq.heappop(h)
#     next = now[0]+now[1]
#     if i <= n and i <= next:
#         heapq.heappush(h,[i,i,1]) # n2logn, n3logn
#         i += 1
#     if now[2] < n:
#         heapq.heappush(h,[next,now[1],now[2]+1])
        
# print(now[0])


def count(m):
    result_count = 0
    for i in range(1,n+1):
        result_count += min(m // i,n) #i는 행 또는 열을 의미 min()은 m보다 작은 i행의 개수를 의미
    return result_count


def bisearch(s,e):
    if s > e:
        return 10000000000
    m = (s+e)//2
    if count(m) >= k:
        return min(bisearch(s,m-1),m) # 만족하는 가장 작은 값을 찾으면 됨
    else:
        return bisearch(m+1,e)

n = int(input())
k = int(input())

result = bisearch(1,min(n**2,10**9))
print(result)