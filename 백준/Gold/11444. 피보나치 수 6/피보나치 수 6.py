import sys
input = sys.stdin.readline #~3:40
sys.setrecursionlimit(10**6)
def mul(a,b):
    x = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                x[i][j] = ((a[i][k]*b[k][j])%1000000007 + x[i][j])%1000000007
    return x
def fib(m, n):
    if n == 1:
        return m
    now = fib(m,n//2)
    if n%2 == 0:
        return mul(now,now)
    else:
        return mul(mul(now,now), m)

n = int(input())

if n < 3:
    print(1)
else:
    res = fib([[1,1],[1,0]], n-1)
    print(res[0][0])