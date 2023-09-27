# import sys
# sys.setrecursionlimit(10000)
# def dfs(ss,reversed):
#     if ss not in r_t and ss not in t:
#         return
#     if reversed:
#         if ss == r_t:
#             print(1)
#             exit(0)
#         else:
#             dfs('A'+ss,1)
#             dfs(ss+'B',0)
#     else:
#         if ss == t:
#             print(1)
#             exit(0)
#         else:
#             dfs(ss+'A',0)
#             dfs('B'+ss,1)
        

# s = input().rstrip()
# t = input().rstrip()
# r_t = ''.join((reversed(t)))
# dfs(s,0)
# print(0)

#dfs로 풀시 시간초과
#s에서 t를 만드는 것이 아니라 t에서 s를 만듬
s = input().rstrip()
t = input().rstrip()

for _ in range(len(t)-len(s)):
    if t[-1] == 'A':
        t = t[:-1]
    elif t[-1] == 'B':
        t = t[-2::-1]
if s == t:
    print(1)
else:
    print(0)