import sys
from itertools import combinations

input = sys.stdin.readline

N, S = map(int, input().split())

list = list(map(int, input().split()))

res = 0

for i in range(1, N+1):
    comb = combinations(list, i)
    for c in comb:
        if sum(c) == S:
            res += 1

print(res)