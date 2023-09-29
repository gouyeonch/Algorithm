import sys
from collections import deque

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def bfs():
    global sx, sy, tx, ty, graph

    queue = deque()
    queue.append([sx,sy])

    while queue:
        x, y = queue.popleft()

        #목표 노드에 도달했으면 bfs 종료
        if x == tx and y == ty:
            return graph[x][y]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if not(nx < 0 or nx >= L or ny < 0 or ny >= L) and graph[nx][ny] == 0:
                queue.append([nx,ny])
                graph[nx][ny] = graph[x][y] + 1
                


T = int(sys.stdin.readline())

for _ in range(T):
    L = int(sys.stdin.readline())
    sx, sy = map(int, sys.stdin.readline().split())
    tx, ty = map(int, sys.stdin.readline().split())

    graph = [[0 for _ in range(L)] for _ in range(L)]

    print(bfs())
