import sys
from collections import deque

X, Y, Z = map(int, sys.stdin.readline().split())

dx = [1 ,0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    while queue:
        z, y, x = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if not(nx < 0 or ny < 0 or nx >= X or ny >= Y or nz <0 or nz >= Z) and graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                queue.append([nz, ny, nx])

#상자 입력 받고
# 1로 표시되어 있는거 리스트에 정리해두고
# 해당 리스트원소만큼 bfs 실행
# bfs는 -1인거 빼고 다음께 더 작게 방문 가능하면 방문
# 다 끝나고 제일 큰 숫자 출력
# 만약에 0 남아 있으면 -1 출력

graph = []
start = []

queue = deque()

graph = [[[0 for _ in range(X)] for _ in range(Y)] for _ in range(Z)]

for i in range(Z):
    for j in range(Y):
        graph[i][j] = list(map(int, sys.stdin.readline().split()))

for i in range(Z):
    for j in range(Y):
        for k in range(X):
            if graph[i][j][k] == 1:
                queue.append([i, j, k])

bfs()

maxTomato = 0
for i in range(Z):
    for j in range(Y):
        for k in range(X):
            if graph[i][j][k] == 0:
                print(-1)
                quit()
            maxTomato = max(graph[i][j][k], maxTomato)
print(maxTomato-1)