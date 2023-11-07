import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())

#처음에 n+1까지 배열 만들기
arr = [ i for i in range(n+1)]

def find(x):
    if x == arr[x]:
        return x
    else:
        arr[x] = find(arr[x])
        return arr[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        arr[a] = b

def checkSame(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        print("yes")
    else:
        print("no")

for _ in range(m):
    c, a, b = map(int, sys.stdin.readline().split())

    if c == 0:
        union(a, b)
    else:
        checkSame(a, b)