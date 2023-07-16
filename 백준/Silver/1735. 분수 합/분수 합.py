import sys

def gcd(a, b):
    return b, a%b

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

gcdA = A = a*d + c*b
gcdB = B = b*d

if gcdA < gcdB:
    gcdA , gcdB = gcdB, gcdA

while gcdA %gcdB != 0:
    gcdA, gcdB = gcdB, gcdA%gcdB

print(str(A//gcdB) + " " + str(B//gcdB))