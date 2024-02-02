import sys
import copy

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))
save = copy.deepcopy(graph)

def rain(k):
    for i in range(N):
        for j in range(N):
            if graph[i][j] <= k:
                graph[i][j] = -1

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(s, e):
    graph[s][e] = -1

    for i in range(4):
        nx = e + dx[i]
        ny = s + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if graph[ny][nx] != -1:
                dfs(ny, nx)

res = 0
for k in range(0, 101):
    cnt = 0
    graph = copy.deepcopy(save)
    rain(k)
    for i in range(N):
        for j in range(N):
            if graph[i][j] != -1:
                cnt += 1
                dfs(i, j)
    if res < cnt:
        res = cnt

print(res)