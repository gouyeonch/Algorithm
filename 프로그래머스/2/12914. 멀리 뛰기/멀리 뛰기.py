def solution(n):
    dp = [(0,0),(1,0)]
    for i in range(2, n+1):
        dp.append((dp[i-1][0]+dp[i-1][1], dp[i-1][0]))
    
    return (dp[n][0]+dp[n][1])%1234567