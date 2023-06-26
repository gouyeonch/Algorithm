import sys

n, m = map(int,sys.stdin.readline().split())

bucket = [0] * n

for i in range(m):
    start, fin, b = map(int,sys.stdin.readline().split())
    for j in range(start-1, fin):
        bucket[j] = b

for i in range(n-1):
    print(str(bucket[i]) + " ", end="")
print(bucket[n-1], end="")