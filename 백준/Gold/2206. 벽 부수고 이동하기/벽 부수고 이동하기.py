# bfs를 통해 최단 거리 계산
# 그 다음 벽을 하나씩 부수면서 최단 거리 계산
import sys
from collections import deque

input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs():
    while queue:
        x,y,z = queue.popleft()

        if x == H-1 and y == M-1:
            return visited[x][y][z]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<H and 0<=ny<M:
                if z == 0 and graph[nx][ny] == '1':
                    queue.append((nx,ny,1))
                    visited[nx][ny][1] = visited[x][y][0] + 1
                elif graph[nx][ny] == '0' and visited[nx][ny][z] == 0:
                    queue.append((nx,ny,z))
                    visited[nx][ny][z] = visited[x][y][z] + 1
    return -1

H, M = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(H)]

queue = deque()
queue.append((0,0,0))

visited = [[[0]*2 for _ in range(M)] for _ in range(H)]
visited[0][0][0] = 1

print(bfs())