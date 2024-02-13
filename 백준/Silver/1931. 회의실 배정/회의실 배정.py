import sys

input = sys.stdin.readline

N = int(input())

li = []
for _ in range(N):
    li.append(list(map(int, input().split())))

# 두 번째 원소를 기준으로 정렬 후 첫 번째 원소를 기준으로 정렬
li.sort(key=lambda x: (x[1], x[0]))

cnt = 0
last = 0
for i in range(N):
    start, end = li[i]
    if last <= start:
        start = last
        cnt += 1
        last = end
print(cnt)