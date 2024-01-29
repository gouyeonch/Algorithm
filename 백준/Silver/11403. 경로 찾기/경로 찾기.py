# 인접행렬 생성
# 그래프도 생성
# dfs 돌면서 기록

import sys

input = sys.stdin.readline

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

li = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            li[i].append(j)

# 인접리스트 돌면서 그래프 기록
def dfs(s, check):
    visited[s] = 1

    for l in li[s]:
        graph[check][l] = 1
        if visited[l] == 0:
            dfs(l, check)
            

for i in range(N):
    visited = [0] * N
    dfs(i, i)

# 결과 출력
for row in graph:
    print(" ".join(map(str, row)))