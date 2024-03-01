# 0421 ~ 0441
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

parent = [i for i in range(N+1)]

def find(n):
    if parent[n] == n:
        return n
    tmp = find(parent[n])
    parent[n] = tmp
    return tmp

def union(a,b):
    if parent[a] != parent[b]:
        tmpA = find(a)
        tmpB = find(b)
        if tmpA < tmpB:
            parent[tmpB] = tmpA
        else:
            parent[tmpA] = tmpB

for _ in range(M):
    c, a, b = map(int, input().split())

    if c == 0:
        union(a,b)
    else:
        if find(a) != find(b):
            print("NO")
        else:
            print("YES")