def solution(n):
    if n%2==1:
        return 0
    
    dp = [0,0,(1,0),0,(3,1),0]
    for i in range(6, n+1):
        if i%2 == 1:
            dp.append(0)
        else:
            dd = (dp[i-2][0]*3)%1000000007 + (dp[i-2][1]*2)%1000000007
            pp = (dp[i-2][0])%1000000007 + (dp[i-2][1])%1000000007
            dp.append((dd,pp))
    return (dp[n][0]*3 + dp[n][1]*2)%1000000007