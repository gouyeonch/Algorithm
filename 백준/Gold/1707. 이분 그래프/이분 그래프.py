import sys
sys.setrecursionlimit(10**6)

T = int(sys.stdin.readline())

#dfs 시 컬러를 바꾸면서 진행
#컬러를 바꿔야 하는데 다른색이 이미 되어있으면 false
#위의 케이스가 하나도 발견 안되면 ok
def dfs(start, color):
    global isBiGraph
    for node in start:
        if colorList[node] == 0:
            colorList[node] = -color
            dfs(adj[node], -color)
        if colorList[node] == color:
            isBiGraph = False
            return

for _ in range(T):
    V, E = map(int, sys.stdin.readline().split())
    isBiGraph = True

    #빈 인접리스트 생성, 컬러리스트 생성
    adj = [[] for _ in range(V+1)]
    colorList = [0 for _ in range(V+1)]

    #인접리스트 정보 입력
    for i in range(E):
        a, b = map(int, sys.stdin.readline().split())

        adj[a].append(b)
        adj[b].append(a)
    
    for i in range(1, V+1):
        if colorList[i] == 0:
            colorList[i] = 1
            dfs(adj[i], 1)
            if isBiGraph == False:
                break
    
    if isBiGraph == True:
        print("YES")
    else:
        print("NO")
