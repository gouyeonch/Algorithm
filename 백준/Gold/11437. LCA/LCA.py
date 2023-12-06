import sys
sys.setrecursionlimit(10**5)

# 노드 연결 데이터를 입력 받아 저장
# 루트 노드는 따로 찾아준다
N = int(sys.stdin.readline())

depth = [0] * (N+1)
parent = [0] * (N+1)
tr = [ [] for _ in range(N+1)]
visit = [False] * (N+1)

for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    tr[a].append(b)
    tr[b].append(a)
root = 1

# dfs로 depth와 parent 계산
def init(root):
    visit[root] = True
    for t in tr[root]:
        if visit[t] == False:
            parent[t] = root
            depth[t] = depth[root]+1
            init(t)

init(root)

# LCA 연산을 통해 높이를 맞춰주고 공통조상을 출력
def LCA(a, b):
    while depth[a] <  depth[b]:
        b = parent[b]
    while depth[a] >  depth[b]:
        a = parent[a]
    while a != b:
        b = parent[b]
        a = parent[a]
    return a

M = int(sys.stdin.readline())

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(LCA(a,b))