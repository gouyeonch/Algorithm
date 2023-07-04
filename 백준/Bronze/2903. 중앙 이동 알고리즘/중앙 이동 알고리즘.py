import sys

dot = 4
slide = 2

n = int(sys.stdin.readline())

for i in range(n):
    dot = dot*4 - slide*4 + 1
    slide = slide*2 -1

print(dot)

