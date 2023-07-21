import sys

n = int(sys.stdin.readline())

s = set(["ChongChong"])

for i in range(n):
    a, b = sys.stdin.readline().split()

    if a in s and b in s:
        continue
    elif a in s:
        s.add(b)
    elif b in s:
        s.add(a)

print(len(s))