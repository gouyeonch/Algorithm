import sys

chess = [1,1,2,2,2,8]
n = list(map(int, sys.stdin.readline().split()))

for i in range(5):
    print(str(chess[i]-n[i])+" ", end="")
print(str(chess[5]-n[5]))