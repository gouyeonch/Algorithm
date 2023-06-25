import sys

n = int(sys.stdin.readline())
list = [*map(int, sys.stdin.readline().split())]
v = int(sys.stdin.readline())

print(list.count(v))