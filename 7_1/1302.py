import sys
from collections import defaultdict
input = sys.stdin.readline

dic = defaultdict(int)
for _ in range(int(input())):
    k = input().rstrip()
    dic[k] += 1

result = []
for key in dic:
    result.append([dic[key],key])

result.sort(key=lambda x:(-x[0],x[1]))
print(result[0][1])