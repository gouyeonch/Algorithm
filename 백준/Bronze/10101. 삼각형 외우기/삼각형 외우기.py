import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

du = 0

sum = a+b+c

if sum != 180:
    print("Error")
    exit()

if a==b: du+=1
if b==c: du+=1
if a==c: du+=1

if du == 3:
    print("Equilateral")
elif du == 1:
    print("Isosceles")
else:
    print("Scalene")