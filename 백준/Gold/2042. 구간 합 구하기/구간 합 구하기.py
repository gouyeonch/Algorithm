import sys

N, M, K = map(int, sys.stdin.readline().split())

#트리 배열 크기 정하기
treeSize = 0
while 2**treeSize < N:
    treeSize += 1

#트리 초기화
seg = [0] * ((2**treeSize) * 2)

leafStart = 2**treeSize

for i in range(N):
    n = int(sys.stdin.readline())
    seg[leafStart + i] = n

for i in range(1, leafStart):
    ind = leafStart - i
    seg[ind] = seg[2*ind] + seg[2*ind + 1]

for i in range(M+K):
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 1:
        ind = leafStart + b - 1
        seg[ind] = c

        ind //= 2
        while ind > 0:
            seg[ind] = seg[2*ind] + seg[2*ind + 1]
            ind //= 2
    
    elif a == 2:
        sum = 0

        start = leafStart + b - 1
        end = leafStart + c - 1

        while start <= end:
            if start % 2 == 1:
                sum += seg[start]
                start += 1
            if end % 2 == 0:
                sum += seg[end]
                end -= 1
            start //= 2
            end //= 2
        print(sum)