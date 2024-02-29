from collections import deque

def solution(n, computers): # 0919~0930
    graph = [[] for _ in range(n)]
    
    for i in range(len(computers)):
        for j in range(n):
            if j!=i:
                if computers[i][j] == 1:
                    graph[i].append(j)

    visit = [0] * n
    def bfs(s):
        queue = deque()
        queue.append(s)
        
        while queue:
            nn = queue.pop()
            
            for node in graph[nn]:
              if visit[node] == 0:
                visit[node] = 1
                queue.append(node)
    
    cnt = 0
    for i in range(n):
        if visit[i] == 0:
            cnt+=1
            bfs(i)
            
    return cnt