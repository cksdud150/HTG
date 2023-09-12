import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    dungeon = [list(map(int,input().split())) for _ in range(n)]
    