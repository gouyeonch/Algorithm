import sys

A = [sys.stdin.readline().rstrip() for _ in range(5)]

max = 0

for i in range(5):
    if max < len(A[i]):
        max = len(A[i])

for i in range(max):
    for j in range(5):
        if(len(A[j]) > i):
            print(A[j][i], end="")