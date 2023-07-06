import sys

line = sorted(list(map(int, sys.stdin.readline().split())))
if line[2] >= line[1] + line[0]:
    line[2] = line[1] + line[0] -1
print(sum(line))
