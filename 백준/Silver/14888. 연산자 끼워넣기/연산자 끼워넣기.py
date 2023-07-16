from itertools import permutations
import sys


def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiple(a, b):
    return a * b


def divide(a, b):
    if a < 0:
        return -(-a // b)
    else:
        return a // b


fun = [add, minus, multiple, divide]

n = int(input())
an = list(map(int, input().split()))
operN = list(map(int, input().split()))
oper = []
for i, o in enumerate(operN):
    for _ in range(o):
        oper.append(fun[i])

big = -100**11
small = 100**11

for oo in permutations(oper, n - 1):
    result = an[0]
    for i, f in enumerate(oo):
        result = f(result, an[i + 1])
    if result > big:
        big = result
    if result < small:
        small = result
print(big)
print(small)
