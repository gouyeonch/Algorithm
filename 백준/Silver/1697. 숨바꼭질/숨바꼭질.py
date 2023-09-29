import sys
from collections import deque

visited = [0] * 100001

def bfs(S):
    queue = deque()
    queue.append(S)
    visited[S] = 0

    while queue:
        x = queue.popleft()

        if x == T:
            return visited[x]

        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100000 and visited[nx] == 0:
                queue.append(nx)
                visited[nx] = visited[x] +1



S, T =  map(int, sys.stdin.readline().split())

print(bfs(S))

# 근데 방문한 곳도 방문할 만 하지않나