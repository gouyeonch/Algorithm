

def mul(a,b):
    ll = len(a)
    x = [[0]*ll for _ in range(ll)]

    for i in range(ll):
        for j in range(ll):
            for k in range(ll):
                x[i][j] = (x[i][j] + (a[i][k] * b[k][j])%1000) % 1000
    return x

def division(m, n):
    if n == 1:
        return m
    mm = division(m,n//2)
    
    if n%2 == 0:
        return mul(mm,mm)
    else:
        return mul(mul(mm,mm),m)
import sys
#0252
input = sys.stdin.readline

N,B = map(int,input().split())

mat = [list(map(int,input().split())) for _ in range(N)]

mm = division(mat,B)
for i in range(N):
    for j in range(N):
        mm[i][j] %= 1000

for k in mm:
    print(*k)