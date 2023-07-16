from itertools import permutations
n = int(input())
for a in permutations(range(1,n+1),n):
    print(*a, sep =' ')