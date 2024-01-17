import sys

input = sys.stdin.readline

n = 1

T = []

while (n*(n+1)/2) < 1000:
    T.append(n*(n+1)/2)
    n+=1

li = set()
for i in range(len(T)):
    for j in range(i, len(T)):
        for k in range(j, len(T)):
          li.add(T[i] + T[j] + T[k])  

N = int(input())

for _ in range(N):
    C = int(input())

    if C in li:
        print(1)
    else:
        print(0)
