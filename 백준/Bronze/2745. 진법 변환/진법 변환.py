import sys

d = 0

n, b = sys.stdin.readline().split()

n = n[::-1]
b = int(b)

for i in range(len(n)):
    if n[i].isupper():
        t = ord(n[i]) - ord('A') + 10
    else:
        t = int(n[i])
    
    for j in range(i):
        t *= b
    
    d += t

print(d)
