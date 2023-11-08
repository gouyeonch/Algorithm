import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())

# 유니온 파인드 배열
parent = [i for i in range(n+1)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]
    
def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        parent[a] = b
    elif a < b:
        parent[b] = a

def isSame(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return 1
    else:
        return 0
# 각각 유니온 파인드 메서드 정의

#에지 클래스 정의
class edge:
    def __init__(self, s, e, w):
        self.s = s
        self.e = e
        self.w = w
        

# 에지 리스트 만들기
eList = []
for i in range(m):
    s, e, w = map(int, sys.stdin.readline().split())
    
    eList.append(edge(s, e, w))

eList.sort(key=lambda edge : edge.w)

unionNum = 0
weightSum = 0
for e in eList:

    if unionNum == n - 1:
        break

    sRoot = find(e.s)
    eRoot = find(e.e)

    if sRoot != eRoot:
        if sRoot > eRoot:
            parent[sRoot] = eRoot
        else:
            parent[eRoot] = sRoot
        weightSum += e.w
        unionNum += 1

print(weightSum)