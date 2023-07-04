import sys

resStr = ""

n = int(sys.stdin.readline())

for i in range(n):
    q = 0
    d = 0
    n = 0
    p = 0
    cent = int(sys.stdin.readline())
    q = cent // 25
    cent %= 25
    d = cent // 10
    cent %= 10
    n = cent // 5
    cent %= 5
    p = cent

    print(str(q) + " " + str(d) + " " + str(n) + " " + str(p))

