import sys

a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())

r = 1 if a1*n0+a0 <= c*n0 and a1 <= c else 0
print(r)