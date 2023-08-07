import sys
import bisect

n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))

L = []
L.append(li[0])

for i in li:
    ind = bisect.bisect_left(L, i)
    if ind >= len(L)-1:
        if L[-1] < i:
            L.append(i)
        else:
            L[-1] = i
    elif L[ind] > i:
        L[ind] = i
print(len(L))