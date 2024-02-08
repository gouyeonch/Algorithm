from collections import deque
import sys
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def burn():
    for _ in range(len(fire)):
        x, y = fire.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<H and 0<=ny<M:
                if graph[nx][ny] != '#' and graph[nx][ny] != '*':
                    graph[nx][ny] = '*'
                    fire.append((nx,ny))

def move():
    isMove = False
    for _ in range(len(start)):
        x, y = start.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<H and 0<=ny<M:
                if graph[nx][ny] != '#' and graph[nx][ny] != '*' and visited[nx][ny] == 0:
                    isMove = True
                    visited[nx][ny] = visited[x][y] +1
                    start.append((nx,ny))
            else:
                return visited[x][y]
    if not isMove:
        return "IMPOSSIBLE"




T = int(input())

for _ in range(T):
    fire = deque()
    start = deque()

    M, H = map(int, input().split())

    graph=[]
    for i in range(H):
        graph.append(list(input().rstrip()))
        for j in range(M):
            if graph[i][j] == '*':
                fire.append((i,j))
            if graph[i][j] == '@':
                start.append((i,j))
    
    visited = [[0] * M for _ in range(H)]
    visited[start[0][0]][start[0][1]] = 1

    result = 0
    while True:
        burn()
        result = move()
        if result:
            break
    
    print(result)
