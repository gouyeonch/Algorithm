import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

tr = [[] for i in range(N+1)]
ans = [0] * (N+1)

for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    tr[a].append(b)
    tr[b].append(a)

def DFS(s):

    for n in tr[s]:
        if ans[n] == 0:
            ans[n] = s
            DFS(n)

DFS(1)

for i in range(2, N+1):
    print(ans[i])