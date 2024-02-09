# 이것도 배열 상에서 가능한 것을 미리 노드로 만들어 놓고 시작해야할듯
import sys
from collections import deque

input = sys.stdin.readline

def fill0(s):
    while True:
        if len(s) >= 4:
            break
        s = "0" + s
    return s

def bfs():
    queue = deque()
    queue.append(S)

    while queue:
        node = queue.popleft()
        # print("node : " + str(node))

        if node == G:
            return visited[node]

        ss=visited[node]

        #D
        n = (node*2)%10000
        if not visited[n]:
            queue.append(n)
            visited[n] = visited[n] + ss + "D"
            # print("D - n : " + str(n) + ", visited[n] : " + str(visited[n]))
        
        #S
        if node == 0:
            n = 9999
        else:
            n = node - 1
        if not visited[n]:
            queue.append(n)
            visited[n] = visited[n] + ss + "S"
            # print("S - n : " + str(n) + ", visited[n] : " + str(visited[n]))

        s = fill0(str(node))
        # print(s)

        #L
        n = int(s[1:] + s[0])
        if not visited[n]:
            queue.append(n)
            visited[n] = visited[n] + ss + "L"
            # print("L - n : " + str(n) + ", visited[n] : " + str(visited[n]))

        #R
        n = int(s[3] + s[:3])
        if not visited[n]:
            queue.append(n)
            visited[n] = visited[n] + ss + "R"
            # print("R - n : " + str(n) + ", visited[n] : " + str(visited[n]))


T = int(input())

for _ in range(T):
    # print()
    # print()
    # print()

    S, G = map(int, input().split())

    visited = ["" for _ in range(10000)]

    print(bfs())