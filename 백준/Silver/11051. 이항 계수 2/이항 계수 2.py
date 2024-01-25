import sys
from itertools import combinations

input = sys.stdin.readline

N,K = map(int, input().split())

pascal = []

for i in range(N+1):
    pascal.append([0]*(i+1))

pascal[0][0] = pascal[1][0] = pascal[1][1] = 1

for i in range(2, N+1):
    pascal[i][0] = 1
    for j in range(1, i):
        pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]
    pascal[i][i] = 1

print(pascal[N][K]%10007)