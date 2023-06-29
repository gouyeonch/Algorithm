import sys

n, n1 = map(int, sys.stdin.readline().split())

A = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
B = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(len(A)):
    for j in range(len(A[0])):
        A[i][j] = str(A[i][j] + B[i][j])

res = []

for i in range(len(A)):
    res.append(" ".join(A[i]))

res = "\n".join(res)

print(res)