from collections import defaultdict
n = int(input())

arr = list(map(int,input().split()))
arr2 = sorted(arr)

j = 0
dic = defaultdict(lambda : -1)
for a in arr2:
    if dic[a] == -1:
        dic[a] = j
        j += 1

for a in arr:
    print(dic[a],end = ' ')
        