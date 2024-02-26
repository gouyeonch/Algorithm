# 0132
import sys
input = sys.stdin.readline

N = int(input())

rag = [list(map(int, input().split())) for _ in range(N)]

cnt0 = cnt1 = cnt_1 = 0

def division(x,y,n):
    global cnt0
    global cnt1
    global cnt_1
    if n == 0: return
    # print("x : " + str(x) + ", y : " + str(y) + ", n: " + str(n))
    c = rag[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if c != rag[i][j]:
                n = n//3
                division(x,y,n)
                division(x+n,y,n)
                division(x+(2*n),y,n)
                division(x,y+n,n)
                division(x+n,y+n,n)
                division(x+(2*n),y+n,n)
                division(x,y+(2*n),n)
                division(x+n,y+(2*n),n)
                division(x+(2*n),y+(2*n),n)
                return
    if c==0: cnt0 += 1
    elif c==1: cnt1 += 1
    elif c==-1: cnt_1 += 1

division(0,0,N)

print(cnt_1)
print(cnt0)
print(cnt1)