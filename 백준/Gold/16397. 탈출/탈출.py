import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append(N)

    visited[N] = 0

    # print(queue)
    while queue:
        node = queue.popleft()
        # print(node)
        if node == G:
            if visited[node] > T:
                break
            return visited[node]

        for n in graph[node]:
            if visited[n] == -1:
                visited[n] = visited[node] + 1
                queue.append(n)
    
    return "ANG"


N, T, G = map(int, input().split())

# 스타트링크랑 똑같이 각 노드별로 가능한 인접리스트 만들기
graph = [[] for _ in range(100000)]

graph[0].append(1)

for i in range(50000, 99999):
    graph[i].append(i+1)

for i in range(1, 5):
    graph[i].append(i+1)
    num = i*2
    graph[i].append(num-1)

for i in range(5, 50000):
    graph[i].append(i+1)
    num = i*2
    num = str(num)
    high = str(int(num[0]) - 1)
    num = int(high + num[1:])
    graph[i].append(num)

visited = [-1] * 100000

# for i in range(99995, 100000):
#     print(graph[i])

print(bfs())