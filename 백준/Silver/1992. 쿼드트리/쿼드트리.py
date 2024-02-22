import sys

input = sys.stdin.readline

N = int(input())

pic = []
for _ in range(N):
    pic.append(list(input().rstrip()))

res = []

def sol(x,y,N):
    c = pic[x][y]
    res = []
    for i in range(x,x+N):
        for j in range(y,y+N):
            if pic[i][j] != c:
                ll = N//2
                res.append('(')
                res.append(sol(x,y,ll))
                res.append(sol(x,y+ll,ll))
                res.append(sol(x+ll,y,ll))
                res.append(sol(x+ll,y+ll,ll))
                res.append(')')
                return "".join(res)
    res.append(c)
    return "".join(res)

res = sol(0,0,N)
print("".join(res))