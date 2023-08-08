import sys
from collections import deque

n = int(sys.stdin.readline())

ballun = deque(map(int, sys.stdin.readline().split()))
dq = deque()
res = []

for i in range(len(ballun)):
    dq.append((ballun[i], i+1))

def boom(dq, n):
    if n > 0:
        for _ in range(n-1):
            dq.append(dq.popleft())
        return dq.popleft()
    else:
        n*=-1
        for _ in range(n-1):
            dq.appendleft(dq.pop())
        return dq.pop()

b = dq.popleft()
res.append(str(b[1]))

for i in range(n-1):
    b = boom(dq, b[0])
    res.append(str(b[1]))

print(" ".join(res))