import sys

input = sys.stdin.readline

N = int(input())

dp = list(map(int, input().split()))

for i in range(1, N):
    maxList = [dp[i]]
    for j in range(i//2+1):
        maxList.append(dp[j] + dp[i-1-j])
    dp[i] = max(maxList)

print(dp[N-1])