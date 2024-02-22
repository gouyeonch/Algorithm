import sys

input = sys.stdin.readline

cnt0 = 0
cnt1 = 0

N = int(input())

ragt = []
for _ in range(N):
    ragt.append(list(map(int,input().split())))

def sol(x,y,N):
    global cnt1, cnt0
    c = ragt[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if c != ragt[i][j]:
                ll = N//2
                sol(x,y,ll)
                sol(x+ll,y,ll)
                sol(x,y+ll,ll)
                sol(x+ll,y+ll,ll)
                return
    if c == 1:
        # print("x, y, ll : " + str(x) + ", " + str(y) + ", " + str(N))
        cnt1 += 1
    else:
        # print("x, y, ll : " + str(x) + ", " + str(y) + ", " + str(N))
        cnt0 += 1

sol(0,0,len(ragt[0]))
print(cnt0)
print(cnt1)