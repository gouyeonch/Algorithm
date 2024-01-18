import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

d = ['1', '2', '3','4','5','6','7','8','9']

nums = list(permutations(d, 3))

for _ in range(N):
    C, s, b = map(int, input().split())

    C = list(str(C))

    rmcnt = 0

    for i in range(len(nums)):
        strike = ball = 0
        i -= rmcnt
        for j in range(3):
            if nums[i][j] == C[j]:
                strike += 1
            elif C[j] in nums[i]:
                ball += 1
        
        if strike != s or ball != b:
            nums.remove(nums[i])
            rmcnt += 1

print(len(nums))