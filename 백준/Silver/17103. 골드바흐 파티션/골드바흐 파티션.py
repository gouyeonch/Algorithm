import sys


n = int(sys.stdin.readline())

prime = [i for i in range(1000001)]

for i in range(2, 500001):
    if prime[i] == 0:
        continue
    for j in range(i*2, 1000001, i):
        prime[j] = 0
prime[1] = 0
for i in range(n):
    k = int(sys.stdin.readline())
    res = 0

    for j in range(2, k//2+1):
        if prime[j] != 0 and prime[k-j] != 0:
            res+=1
    print(res)