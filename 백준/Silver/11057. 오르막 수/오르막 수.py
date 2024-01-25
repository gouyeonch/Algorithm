import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())

dp = [[1,1,1,1,1,1,1,1,1,1]]

for i in range(1,N):
    sumList = [1]
    for j in range(1,10):
        sumList.append((sumList[j-1]+dp[i-1][j]))
    dp.append(sumList)


print(sum(dp[N-1])%10007)