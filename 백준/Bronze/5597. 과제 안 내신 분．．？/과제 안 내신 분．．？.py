import sys

list = list(range(1, 31))

for i in range(28):
    ind = int(sys.stdin.readline())
    list.remove(ind)

print(' '.join(map(str, list)))
