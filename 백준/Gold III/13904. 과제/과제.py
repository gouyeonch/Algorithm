# 8:56

#제일 높은 날짜부터 진행
# 해당 크기 만큼 리스트 만들기 days
# 각 날짜 리스트는 dict으로 받기
# 힙 에다가 현재 날짜거랑 지금까지 쌓인거로 해서 넣고 하나 팝해서 넣기
import sys
from heapq import *

input = sys.stdin.readline

days = []

N = int(input())

li = []
max_day = 0
for _ in range(N):
    d, p = map(int,input().split())
    li.append([d,p])
    if max_day < d:
        max_day = d
# print(li)
# print(max_day)

li.sort(key=lambda l : l[1])
# print(li)
hws = [[] for _ in range(max_day+1)]
# print(hws)
for d, p in li:
    hws[d].append(p)
# print(hws)

heap = []

points = 0
for d in range(max_day,0,-1):
    for h in hws[d]:
        heappush(heap, (-h, h))
    # print("d " + str(d))
    # print(heap)
    if len(heap) != 0:
        points += heappop(heap)[1]
    # print("Res : " + str(heap))
    # print("points : " + str(points))
    # print()
print(points)
