import sys

n, k = int(sys.stdin.readline()), int(sys.stdin.readline())

left, right = 1, k

while left <= right:
    mid = (left + right) // 2

    tmp = 0
    for i in range(1, n+1):
        tmp += min(mid//i, n)

    if tmp >= k:
        ans = mid
        right = mid -1
    else:
        left = mid +1
print(ans)