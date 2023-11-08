import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

parent = [ i for i in range(N)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

for i in range(N):
    nodes = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if nodes[j] == 1:
            sNode = find(i)
            eNode = find(j)
            if sNode != eNode:
                if sNode > eNode:
                    parent[sNode] = eNode
                else:
                    parent[eNode] = sNode

tList = list(map(int, sys.stdin.readline().split()))
target = find(tList[0]-1)
for i in range(1, M):
    #find해서 대표노드 다 같은지 체크
    if find(tList[i]-1) != target:
        print("NO")
        exit()
    
print("YES")