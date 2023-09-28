import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())

li = [[] for _ in range(N+1)]
visitied = [0 for _ in range(N+1)]

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    li[u].append(v)
    li[v].append(u)

for e in li:
    e.sort(reverse=True)

def bfs(R):

    count = 1
    visitied[R] = count
    queue = deque([R])

    while queue:
        u = queue.popleft()
        for v in li[u]:
            if visitied[v] == 0:
                count += 1
                visitied[v] = count
                queue.append(v)

bfs(R)

for v in visitied[1:]:
    print(v)