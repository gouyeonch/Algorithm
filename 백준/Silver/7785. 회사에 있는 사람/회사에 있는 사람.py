import sys

n = int(sys.stdin.readline())

d = set()

for _ in range(n):
    name, b = sys.stdin.readline().split()
    if b == "enter":
        d.add(name)
    else:
        d.remove(name)

d = sorted(d, reverse=True)

for i in d:
    print(i)