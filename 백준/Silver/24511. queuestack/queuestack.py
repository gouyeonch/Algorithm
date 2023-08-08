import sys
from collections import deque

n = int(sys.stdin.readline())

qs = list(map(int, sys.stdin.readline().split()))

m = list(map(int, sys.stdin.readline().split()))

nn = int(sys.stdin.readline())

list = list(map(int, sys.stdin.readline().split()))

res = []

B = deque()

for i in range(n):
    if qs[i] == 0:
        B.append(m[i])

for e in list:
    B.appendleft(e)
    res.append(str(B.pop()))

print(" ".join(res))