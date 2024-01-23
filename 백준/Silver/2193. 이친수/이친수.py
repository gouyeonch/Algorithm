import sys

input = sys.stdin.readline

N = int(input())

dp = [1,1]

dp[0] = dp[1]

for i in range(2, N):
    dp.append(dp[i-1] + dp[i-2])

print(dp[N-1])