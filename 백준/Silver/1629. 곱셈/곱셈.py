import sys

input = sys.stdin.readline

A,B,C = map(int, input().split())

def multi(A, n):
    if n == 1:
        return A%C
    else:
        tmp = multi(A, n//2)
        if n%2 == 0:
            return ((tmp%C) * (tmp%C))%C
        else:
            return ((tmp%C) * (tmp%C) * (A%C))%C

print(multi(A,B))