import sys


n = int(sys.stdin.readline())

for i in range(n):
    n, m = map(int, sys.stdin.readline().split())
    mul = 1
    div = 1
    for j in range(n):
        mul *= (m-j)
    for j in range(n, 1, -1):
        div *= j
    print(mul//div)
