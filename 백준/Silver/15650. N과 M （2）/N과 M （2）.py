import sys

n, m = map(int, sys.stdin.readline().split())

answer = []

def dfs(cnt, ind, li):
    if cnt == m:
        answer.append(li[:])
        return
    for i in range(ind+1, n+1):
        li.append(str(i))
        dfs(cnt+1, i, li)
        li.pop()

dfs(0, 0, []) 

for i in range(len(answer)):
    print(" ".join(answer[i]))
