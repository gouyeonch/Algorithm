import sys

n = int(sys.stdin.readline())

m = list(map(int, sys.stdin.readline().split()))

if len(m) == 1:
    print(m[0]**2)
else:
    print(min(m)*max(m))