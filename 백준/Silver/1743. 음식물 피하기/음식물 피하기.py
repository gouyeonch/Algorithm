import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

dx = [1 ,-1 ,0 ,0]
dy = [0, 0 ,1 ,-1]

N, M, K = map(int, input().split())

graph = [[0]*(M) for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1

def dfs(y, x):
    if not graph[y][x]:
        return
    global cnt
    graph[y][x] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < M and 0 <= ny and ny < N and graph[ny][nx]:
            cnt += 1
            dfs(ny, nx)

res = 1
for i in range(N):
    for j in range(M):
        cnt = 1
        dfs(i,j)
        res = max(res, cnt)

print(res)