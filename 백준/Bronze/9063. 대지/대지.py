import sys

n = int(sys.stdin.readline())

minX, minY, maxX, maxY = [10000, 10000, -10000, -10000]

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    
    minX = min(x, minX)
    minY = min(y, minY)
    maxX = max(x, maxX)
    maxY = max(y, maxY)

print((maxX-minX)*(maxY-minY))