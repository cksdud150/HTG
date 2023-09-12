import sys
from collections import defaultdict
input = sys.stdin.readline
import heapq

t = int(input())
for _ in range(t):
    k = int(input())
    min_heap = [] #최소힙, 최대힙 2개를 이용해서 구현
    max_heap = []
    length_heap = 0
    dic = defaultdict(int)
    for __ in range(k):
        command, num = input().split()
        if command == 'I':
            heapq.heappush(min_heap,int(num))
            heapq.heappush(max_heap,-int(num))
            length_heap += 1
            dic[int(num)] += 1
        elif length_heap > 0:
            if num == '1':
                temp_i = -heapq.heappop(max_heap)
                while dic[temp_i] == 0: # -1일때 min_heap에서만 빼므로 있는 값인지 체크해야함
                    temp_i = -heapq.heappop(max_heap)
                dic[temp_i] -= 1
                length_heap -= 1
            else:
                temp_i = heapq.heappop(min_heap)
                while dic[temp_i] == 0:
                    temp_i = heapq.heappop(min_heap)
                dic[temp_i] -= 1
                length_heap -= 1
        # if length_heap == 0: # 필요없는거였음
        #     min_heap = []
        #     max_heap = []
    if length_heap == 0:
        print('EMPTY')
    else:
        big_i = -heapq.heappop(max_heap)
        small_i = heapq.heappop(min_heap)
        while dic[big_i] == 0:
             big_i = -heapq.heappop(max_heap)
        while dic[small_i] == 0:
            small_i = heapq.heappop(min_heap)
        print(big_i, small_i)