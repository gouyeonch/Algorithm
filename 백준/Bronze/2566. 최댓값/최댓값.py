import sys

A = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

mmax = 0
inx = 0
iny = 0

for i in range(9):
    for j in range(9):
        if A[i][j] > mmax:
            mmax = A[i][j]
            inx = i
            iny = j
print(mmax)
print(str(inx+1) + " " + str(iny+1))