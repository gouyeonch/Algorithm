import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coin = []
for _ in range(N):
    coin.append(int(input()))

res = 0
for i in range(N-1, -1, -1):
    cc = coin[i]
    if cc <= K:
        # print("K : ")
        # print(K)
        # print("cc : ")
        # print(cc)
        res += K//cc
        K -= (K//cc)*cc
    if K == 0:
        break

print(res)