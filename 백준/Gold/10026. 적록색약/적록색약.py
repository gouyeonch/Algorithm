# 메인 함수에서 dfs를 호출해서 구역을 계산하는 건 쉬움
# 색약을 계산 할 때는 G를 R로 변경
# 맨 앞에 상하좌우 같은건 필터림

import sys
import copy

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

N = int(input())

graph = []
save = []
for _ in range(N):
    graph.append(list(input().strip()))

save = copy.deepcopy(graph)

# 상하좌우 필터링
for i in range(1,N-1):
    for j in range(1, N-1):
        if graph[i][j] == graph[i+1][j] == graph[i-1][j] == graph[i][j+1] == graph[i][j-1]:
            graph[i][j] = graph[i+1][j]

def dfs(s, e):
    temp = graph[s][e]
    graph[s][e] = 0

    for x, y in zip(dx, dy):
        nx = e + x
        ny = s + y

        if 0 <= nx < N and 0 <= ny < N:
            if graph[ny][nx] != 0 and graph[ny][nx] == temp:
                dfs(ny, nx)

cnt = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            cnt += 1
            dfs(i, j)
res = [str(cnt)]

# 여기부턴 적록색약
graph = save

# R을 G로 전부 변경
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

# 상하좌우 필터링
for i in range(1,N-1):
    for j in range(1, N-1):
        if graph[i][j] == graph[i+1][j] == graph[i-1][j] == graph[i][j+1] == graph[i][j-1]:
            graph[i][j] = graph[i+1][j]

cnt = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            cnt += 1
            dfs(i, j)
res.append(str(cnt))

print(' '.join(res))