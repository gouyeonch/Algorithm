import sys
from collections import deque

W, H = map(int, sys.stdin.readline().split())

dx = [1 ,0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not(nx < 0 or ny < 0 or nx >= H or ny >= W) and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

#상자 입력 받고
# 1로 표시되어 있는거 리스트에 정리해두고
# 해당 리스트원소만큼 bfs 실행
# bfs는 -1인거 빼고 다음께 더 작게 방문 가능하면 방문
# 다 끝나고 제일 큰 숫자 출력
# 만약에 0 남아 있으면 -1 출력

graph = []
start = []

queue = deque()

for _ in range(H):
    graph.append(list(map(int, sys.stdin.readline().split())))

for i in range(H):
    for j in range(W):
        if graph[i][j] == 1:
            queue.append([i, j])

bfs()

maxTomato = 0
for i in range(H):
    for j in range(W):
        if graph[i][j] == 0:
            print(-1)
            quit()
        maxTomato = max(graph[i][j], maxTomato)
print(maxTomato-1)