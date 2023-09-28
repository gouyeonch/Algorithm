import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):

    queue = deque()
    queue.append([a, b])

    while queue:
        x, y = queue.popleft()

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= col or ny >= row:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])
    return graph[col-1][row-1]


    

col, row = map(int, input().split())

graph = []

for _ in range(col):
  graph.append(list(map(int, input())))

print(bfs(0,0))

# 2차원이면 굳이 방문 리스트랑 인접리스트를 만들 필요 없이 그래프를 바로 만들면됌
# 최소 경로를 어떻게 저장할까 당장 생각나는건 디피임 맞네 디피네