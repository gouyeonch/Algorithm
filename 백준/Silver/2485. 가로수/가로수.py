import sys

def gcd(a, b):
    if a < b:
        a, b = b, a
    while a%b != 0:
        a, b = b, a%b
    return b 

n = int(sys.stdin.readline())

li = [int(sys.stdin.readline()) for _ in range(n)]

disli = [li[i] - li[i-1] for i in range(1,n)]

d = gcd(disli[0], disli[1])

for i in range(2, n-1):
    d = gcd(disli[i], d)

res = sum(disli) // d - len(disli)

print(res)