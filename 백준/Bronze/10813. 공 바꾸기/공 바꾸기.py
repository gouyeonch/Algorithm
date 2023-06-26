import sys

def swap(array, a, b):
    array[a], array[b] = array[b],array[a]
    return array

n, m = map(int,sys.stdin.readline().split())

bucket = list(range(1, n+1))

for i in range(m):
    a, b = map(int,sys.stdin.readline().split())
    bucket = swap(bucket, a-1, b-1)

print(' '.join(map(str, bucket)))
