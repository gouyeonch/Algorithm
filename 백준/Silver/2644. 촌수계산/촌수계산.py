import sys

input = sys.stdin.readline

N = int(input())

start, end = map(int, input().split())

M = int(input())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    if node == end:
        return
    for g in graph[node]:
        if not visited[g]:
            visited[g] = visited[node] +1
            dfs(g)

visited[start] = 0

dfs(start)

if not visited[end]:
    print("-1")
else:
    print(visited[end])