import sys

resStr = ""

n = int(sys.stdin.readline())

for i in range(n):
    cent = int(sys.stdin.readline())
    for j in [25, 10, 5, 1]:
        print(cent//j, end=' ')
        cent %= j

