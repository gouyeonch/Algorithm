# 9:50
import sys, math
#sys.setrecursionlimit(10 ** 5)
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

length, width, height = tuple(map(int, input().split()))
n = int(input())

size =[]
ans = 0

for _ in range(n):
    size.append(tuple(map(int, input().split())))

size.sort(reverse=True)


total_cnt, ans = 0, 0
for power, cnt in size:
    # 현재 크기의 정육면체를 이용해 지금까지 채운 부피
    total_cnt *= 8
    # 현재 정육면체의 한변의 길이
    cur_len = 2 ** power

    # 남은 부피를 채우기 위해 필요한 정육면체의 개수
    fill_cnt = (length // cur_len) * (width // cur_len) * (height // cur_len) - total_cnt

    # 가지고 있는 정육면체와 필요한 정육면체의 개수 중 최소를 선택한다.
    fill = min(fill_cnt, cnt)

    ans += fill
    total_cnt += fill

if total_cnt == length * width * height:
    print(ans)
else:
    print(-1)