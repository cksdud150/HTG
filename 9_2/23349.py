import sys
from collections import defaultdict

input = sys.stdin.readline

dic = defaultdict(lambda: defaultdict(int)) #플레이스별 시간대를 딕셔너리로 저장
n = int(input())
name_dic = defaultdict(int)
big_count = 0
big_place = ''
for _ in range(n):
    name, place, start, end = input().split()
    if name_dic[name]: # 이미 제출한 이름인지 체크
        continue
    else:
        name_dic[name] = 1
    start = int(start)
    end = int(end)
    for i in range(start, end):
        dic[place][i] += 1
        if dic[place][i] == big_count:
            big_place = min(place, big_place)
        elif dic[place][i] > big_count:
            big_count = dic[place][i]
            big_place = place

flag = 0
min_key = min(dic[big_place].keys())
max_key = max(dic[big_place].keys())
big_start = 0
big_end = 0
for k in range(min_key,max_key+2):
    if dic[big_place][k] == big_count and not flag:
        big_start = k
        flag = 1
    if dic[big_place][k] != big_count and flag:
        big_end = k
        break
print(big_place, big_start, big_end)