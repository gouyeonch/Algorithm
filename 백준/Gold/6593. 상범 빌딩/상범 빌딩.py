import sys
from collections import deque

input = sys.stdin.readline

dx = [1,0,0,-1,0,0]
dy = [0,-1,1,0,0,0]
dz = [0,0,0,0,1,-1]

def bfs():
    queue = deque()
    queue.append([sz,sy,sx])

    while queue:
        z,y,x = queue.popleft()

        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<=nz<L and 0<=ny<R and 0<=nx<C:
                if graph[nz][ny][nx] == '.':
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    queue.append([nz, ny, nx])
                elif graph[nz][ny][nx] == 'E':
                    graph[sz][sy][sx] = graph[z][y][x] + 1
                    return


while True:
    L, R, C = map(int, input().split())

    if L==R==C==0:
        break

# 이거 input 받는법 찾아보자
    graph = []
    for _ in range(L):
        g = [list(input().rstrip()) for _ in range(R)]
        graph.append(g)
        input()
    
    #S 기록
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            for k in range(len(graph[i][j])):
                if graph[i][j][k] == 'S':
                    sz = i
                    sy = j
                    sx = k

    graph[sz][sy][sx] = 0
    bfs()

    if graph[sz][sy][sx] == 0:
        print("Trapped!")
    else:
        print("Escaped in " + str(graph[sz][sy][sx]) + " minute(s).")
    

