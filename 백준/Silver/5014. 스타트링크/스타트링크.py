import sys
from collections import deque

input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

# 각 층 마다 U와 D에 해당하는 인접리스트 2개씩 생성

graph = [[] for _ in range(F+1)]

for i in range(1, F+1):
    if i + U <= F:
        graph[i].append(i+U)
    if i - D >= 1:
        graph[i].append(i-D)

def bfs():
    queue = deque()
    queue.append(S)

    visited[S] = 0

    while queue:
        node = queue.popleft()

        if node == G:
            return visited[G]

        for g in graph[node]:
            if visited[g] == -1:
                visited[g] = visited[node] + 1
                queue.append(g)
    
    return -1

visited = [-1] * (F+1)

res = bfs()
if res == -1:
    print("use the stairs")
else:
    print(res)