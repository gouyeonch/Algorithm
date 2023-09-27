import sys
sys.setrecursionlimit(10 ** 6)

count = 0

def dfs(r):
    global count
    count += 1
    visited[r] = count
    for e in A[r]:
        if not visited[e]:
            dfs(e)

N, M, R = map(int, sys.stdin.readline().split())

visited = [False for _ in range(N+1)]
A = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    A[u].append(v)
    A[v].append(u)

for a in A:
    a.sort()

dfs(R)

for i in range(1, N+1):
    if visited[i] != False:
        print(visited[i])
    else:
        print(0)