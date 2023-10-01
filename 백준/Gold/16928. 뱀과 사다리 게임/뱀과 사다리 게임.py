import sys
from collections import deque


def bfs():
    queue = deque()
    queue.append(1)

    while queue:

        point = queue.popleft()

        if point >= 94:
            print(graph[point]+1)
            return
        
        for i in range(1,7):
            if graph[dest[point+i]] == 0 or graph[dest[point+i]] > graph[point]+1:
                queue.append(dest[point+i])
                graph[dest[point+i]] = graph[point] + 1


L, S = map(int, sys.stdin.readline().split())

dest = [i for i in range(101)]
graph = [0 for i in range(101)]


for _ in range(L+S):
    a, b = map(int, sys.stdin.readline().split())
    dest[a] = b

bfs()
