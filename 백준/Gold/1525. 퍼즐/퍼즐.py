# visit 배열 만들고 그래프 이동마다 방문 했었는지 따지기
import sys
from collections import deque

input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

puzzle = ""
for _ in range(3):
    puzzle += "".join(input().split())

visited = {puzzle:0}
queue = deque()
queue.append(puzzle)

def bfs():
    while queue:
        puzzle = queue.popleft()
        z = puzzle.index('0')

        if puzzle == "123456780":
            return visited[puzzle]
        
        x = z // 3
        y = z % 3
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<3 and 0<=ny<3:
                nz = nx*3 + ny
                puzzle_list = list(puzzle)
                puzzle_list[z], puzzle_list[nz] = puzzle_list[nz], puzzle_list[z]

                new_puzzle = "".join(puzzle_list)

                if visited.get(new_puzzle, 0) == 0:
                    queue.append(new_puzzle)
                    visited[new_puzzle] = visited[puzzle] + 1
    return -1

print(bfs())