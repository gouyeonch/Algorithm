import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())

dp = [0] * (N+1)

rut = N**(1/2)

li = []

l = 0
while l <= rut:
    p = l**2
    li.append(p)
    if p <= N:
        dp[p] = 1
    l+=1

for i in range(2,N+1):
    if i in li:
        continue
    cp = bisect_left(li, i)

    checkList = li[1:cp]
    sumList = []
    for c in checkList:
        sumList.append(dp[i-c]+1)
    dp[i] = min(sumList)

print(dp[N])