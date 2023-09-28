import sys
sys.setrecursionlimit(10 ** 6)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):

    graph[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not(nx < 0 or nx >= H or ny <0 or ny>= W) and graph[nx][ny]:
            dfs(nx, ny)
    

T = int(sys.stdin.readline())

for _ in range(T):
    W, H, K = map(int, sys.stdin.readline().split())

    graph = [[0 for _ in range(W)] for _ in range(H)]

    for _ in range(K):
        j, i = map(int, sys.stdin.readline().split())
        graph[i][j] = 1

    count = 0
    for i in range(H):
        for j in range(W):
            if graph[i][j]:
                count+=1
                dfs(i,j)
    
    print(count)

# 2차원이면 굳이 방문 리스트랑 인접리스트를 만들 필요 없이 그래프를 바로 만들면됌