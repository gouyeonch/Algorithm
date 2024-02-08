import sys
from collections import deque

input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def flow():
    for _ in range(len(water)):

        x,y = water.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<H and 0<=ny<M:
                if graph[nx][ny] != 'D' and graph[nx][ny] != '*' and graph[nx][ny] != 'X':
                    graph[nx][ny] = '*'
                    water.append((nx,ny))

def move():
    isMove = False
    for _ in range(len(start)):

        x,y = start.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<H and 0<=ny<M:
                # print("move")
                # print(str(nx)+" "+str(ny) )
                # print("graph[nx][ny] : " + str(graph[nx][ny]))
                # print("visited[nx][ny] : " + str(visited[nx][ny]))
                # print("graph")
                # for g in graph:
                #     print(g)
                # print("visit")
                # for g in visited:
                #     print(g)    
                if graph[nx][ny] == 'D':
                    return visited[x][y] + 1
                
                if graph[nx][ny] != '*' and graph[nx][ny] != 'X' and visited[nx][ny] == 0:
                    isMove = True
                    visited[nx][ny] = visited[x][y] + 1
                    start.append((nx,ny))
    if not isMove:
        return "KAKTUS"

start = deque()
water = deque()

H, M = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(H)]
for i in range(H):
    for j in range(M):
        # print(str(i) + " " + str(j))
        if graph[i][j] == 'S':
            start.append((i,j))
        elif graph[i][j] == '*':
            water.append((i,j))

visited = [[0]*M for _ in range(H)]
visited[start[0][0]][start[0][1]] = 0

result = 0
while True:
    flow()
    result = move()
    if result:
        break

print(result)