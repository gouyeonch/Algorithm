import sys

n, m = map(int, sys.stdin.readline().split())

woods = list(map(int, sys.stdin.readline().split()))

l, r = 0, max(woods)

while l <= r:
    nWood = 0
    mid = (l+r)//2

    for wood in woods:
        if mid < wood:
            nWood += (wood-mid) 
    
    if nWood >= m:
        l = mid + 1
    else:
        r = mid - 1

print(r)
