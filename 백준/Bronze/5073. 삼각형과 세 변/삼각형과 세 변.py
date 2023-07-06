import sys

line = sorted(list(map(int, sys.stdin.readline().split())))

while line[0] != 0 or line[1] != 0 or line[2] != 0:

    if line[2] >= line[0] + line[1]:
        print("Invalid")
        line = list(map(int, sys.stdin.readline().split()))
        continue

    du = 0
    if line[0]==line[1]: du+=1
    if line[1]==line[2]: du+=1
    if line[0]==line[2]: du+=1

    if du == 3:
        print("Equilateral")
    elif du == 1:
        print("Isosceles")
    else:
        print("Scalene")

    line = sorted(list(map(int, sys.stdin.readline().split())))