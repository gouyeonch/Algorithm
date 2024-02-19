import sys
sys.setrecursionlimit(10**6)

inpur = sys.stdin.readline

p, e = map(int, input().split())
start, end = map(int, input().split())

parent = []
for i in range(p):
    parent.append(i)

def find(n):
    if n == parent[n]:
        return n
    a = find(parent[n])
    parent[n] = a
    return a

def union(a,b):
    a = find(a)
    b = find(b)

    if a==b:
        return
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

li = []
for _ in range(e):
    a,b,c = map(int, input().split())
    li.append((a,b,c))

li.sort(key=lambda l : -l[2])

for l in li:
    union(l[0], l[1])
    if find(start) == find(end):
        print(l[2])
        break