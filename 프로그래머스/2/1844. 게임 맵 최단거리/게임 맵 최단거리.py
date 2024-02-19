# 1000
from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def solution(maps):
    
    XX = len(maps)
    YY = len(maps[0])
    visit = [[0]*(YY+1) for _ in range(XX+1)]
    visit[1][1] = 1
    
    # print(visit)
    # print()
    # 함수 어캐 구현하는지 검색
    def bfs():
        queue = deque()
        queue.append((1,1))
        
        while queue:
            x,y = queue.popleft()

            if x == XX and y == YY:
                return visit[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<nx<=XX and 0<ny<=YY:
                    if visit[nx][ny] == 0 and maps[nx-1][ny-1] != 0:
                        visit[nx][ny] = visit[x][y] + 1
                        queue.append((nx,ny))
                        # print(visit)
                        # print()
            
        return -1
    # print(visit)
    answer = bfs()
    return answer