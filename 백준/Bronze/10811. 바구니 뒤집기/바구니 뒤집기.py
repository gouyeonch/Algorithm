import sys

n, m = map(int, sys.stdin.readline().split())

bucket = list(range(1, n+1))

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    bucket[a-1:b] = bucket[a-1:b][::-1]
    

print(' '.join(map(str, bucket)))
