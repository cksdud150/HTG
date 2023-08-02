import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]
arr.sort() #정렬해서
dic = list(Counter(arr).items())
dic.append((4001,0))
dic.sort(key=lambda x:(-x[1],x[0])) #최빈값을 위해 sort

print(round((sum(arr)+10**-10)/n)) # 오사오입때문에 소숫점 플러스
print(arr[n//2])
print(dic[0][0] if dic[0][1] > dic[1][1] else dic[1][0])
print(arr[n-1] - arr[0])