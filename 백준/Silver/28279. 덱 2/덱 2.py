import sys
from collections import deque

n = int(sys.stdin.readline())

def isEmpty(dq):
    if len(dq) == 0:
        return True
    else:
        return False

dq = deque()

for i in range(n):
    c = list(map(int, sys.stdin.readline().split()))

    if c[0] == 1:
        dq.appendleft(c[1])
    elif c[0] == 2:
        dq.append(c[1])
    elif c[0] == 3:
        if isEmpty(dq) == True:
            print(-1)
        else:
            print(dq.popleft())
    elif c[0] == 4:
        if isEmpty(dq) == True:
            print(-1)
        else:
            print(dq.pop())
    elif c[0] == 5:
        print(len(dq))
    elif c[0] == 6:
        if isEmpty(dq) == True:
            print(1)
        else:
            print(0)
    elif c[0] == 7:
        if isEmpty(dq) == True:
            print(-1)
        else:
            print(dq[0])
    elif c[0] == 8:
        if isEmpty(dq) == True:
            print(-1)
        else:
            print(dq[-1])