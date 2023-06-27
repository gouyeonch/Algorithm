import sys

n = int(sys.stdin.readline())

for i in range(n*2-1):
    num = abs(n-(i+1))
    for j in range(num):
        print(" ", end = "")
    for j in range((n-num)*2-1):
        print("*", end="")
    print()