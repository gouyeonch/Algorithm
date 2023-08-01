import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    res = []

    f = sys.stdin.readline().rstrip()
    nn = sys.stdin.readline().rstrip()
    s = sys.stdin.readline().rstrip()
    parseStr = deque(s[1:-1].split(","))
    flag = 1

    for c in f:
        if c == 'R':
            flag *= -1
        else:
            if len(parseStr) == 0 or nn == "0":
              res = "error"
              break  
            elif flag == 1:
                parseStr.popleft()
            else:
                parseStr.pop()
    
    if res == "error":
        print(res)
    else:
        if flag == -1:
            parseStr.reverse()
        print("[" + ",".join(str(x) for x in parseStr) + "]")