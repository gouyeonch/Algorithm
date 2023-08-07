import sys

n = int(sys.stdin.readline())

st = []

for i in range(n):
    c = list(map(int, sys.stdin.readline().split()))

    if c[0] == 1:
        st.append(c[1])
    elif c[0] == 2:
        if len(st) != 0:
            print(st.pop())
        else:
            print(-1)
    elif c[0] == 3:
        print(len(st))
    elif c[0] == 4:
        if len(st) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 5:
        if len(st) != 0:
            print(st[-1])
        else:
            print(-1)

