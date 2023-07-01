import sys

n = int(sys.stdin.readline())

canvas = [[ 0 for _ in range(100)] for _ in range(100)]

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())

    for i in range(10):
        for j in range(10):
            canvas[y+i][x+j] = 1

s = 0
for li in canvas:
    s += li.count(1)

print(s)