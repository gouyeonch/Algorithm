import sys

n = int(sys.stdin.readline())

sys.stdin.readline().rstrip()

s = set()
res = 0

for i in range(1, n):
    c = sys.stdin.readline().rstrip()

    if c == "ENTER":
        res += len(s)
        s = set()
        continue

    s.add(c)
res += len(s)

print(res)