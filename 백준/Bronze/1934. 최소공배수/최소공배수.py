import sys

n = int(sys.stdin.readline())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    m = a*b
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a%b
    print(int(m/b))