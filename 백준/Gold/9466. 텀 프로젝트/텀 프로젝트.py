import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# check는 맨 처음 시작 노드
# dfs 도중 check를 만나면 flag 바꾸고 return
def dfs(s):
    global res
    next = li[s]

    visited[s] = 1
    cycle.append(s)

    if visited[next] == 1:
        if next in cycle:
            res += cycle[cycle.index(next):]
            return
    else:
        dfs(next)
    

T = int(input())

for _ in range(T):
    N = int(input())

    li = list(map(int, input().split()))
    li.insert(0,-1)

    visited = [0] * (N+1)
    visited[0] = -1

    res = []

    for i in range(1,N+1):
        if visited[i] == 0:
            cycle = []
            dfs(i)
    
    print(N - len(res))


