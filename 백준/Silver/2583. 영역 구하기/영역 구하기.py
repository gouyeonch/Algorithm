import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

# 직사각형 칠하고
# 빈공간 찾으면 cnt++하고 dfs로 다 색칠

M, N, K = map(int, input().split())
# M은 세로 N은 가로

dx = [0,0,1,-1]
dy = [1,-1,0,0]

graph = [[0]*N for _ in range(M)]

res = []

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

def dfs(s, e):
    global area
    graph[s][e] = 1

    for i in range(4):
        nx = e + dx[i]
        ny = s + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if not graph[ny][nx]:
                area += 1
                area = dfs(ny, nx)
    
    return area

cnt = 0
for i in range(M):
    for j in range(N):
        if not graph[i][j]:
            cnt += 1
            area = 1
            
            res.append(dfs(i, j))

print(cnt)
res.sort()
res = " ".join(map(str, res))
print(res)
