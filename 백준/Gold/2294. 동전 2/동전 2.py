import sys
from bisect import bisect_left

input = sys.stdin.readline

N, K = map(int, input().split())
dp = [0]*(K+1)

li = set()

for _ in range(N):
    li.add(int(input()))

li = list(li)

li.sort()

for l in li:
    if K >= l:
        dp[l] = 1

for i in range(1, K+1):
    if i in li:
        continue

    cp = bisect_left(li, i)

    if cp == 0:
        continue

    checkList = li[:cp]
    sumList = []
    for c in checkList:
        if dp[i-c] != 0:
            sumList.append(dp[i-c] + 1)
    if len(sumList) == 0:
        continue
    dp[i] = min(sumList)

if dp[K] == 0:
    print("-1")
else:
    print(dp[K])