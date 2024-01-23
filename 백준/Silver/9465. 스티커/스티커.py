import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    li = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0] * N for _ in range(2)]

    # 길이 1인 경우
    dp[0][0] = li[0][0]
    dp[1][0] = li[1][0]
    if N == 1:
        print(max(dp[0][0],dp[1][0]))
        continue

    # 길이 2인 경우
    dp[0][1] = li[0][1] + li[1][0]
    dp[1][1] = li[1][1] + li[0][0]
    if N == 2:
        print(max(dp[1][1],dp[0][1]))
        continue

    # 길이가 3 이상
    for i in range(2, N):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + li[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + li[1][i]
    print(max(dp[0][N-1],dp[1][N-1]))