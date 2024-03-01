import sys

input = sys.stdin.readline

N = int(input())

li = list(map(int, input().split()))
dp = [0]*N

for i in range(N):
    dp[i] = li[i]
    for j in range(i):
        if li[i] > li[j]:
            dp[i] = max(dp[i], dp[j]+li[i])
print(max(dp))