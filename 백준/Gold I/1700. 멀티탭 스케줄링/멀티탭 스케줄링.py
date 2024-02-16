# 8:00
# 멀티탭 안에 있는 숫자들 기존 배열에서 index로 구하고 제일 큰 숫자 넣기
# li = [2,3,2,3,1,2,7]
# print(li[2:].index(7)) 4
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
li = list(map(int, input().split()))
if N >= K:
    print(0)
    exit()

multitab = set()
# print(li)
for l in li:
    multitab.add(l)
    if len(multitab) == N:
        break

cnt = 0
for i in range(N, K):
    # print(li)
    # print(i)
    if li[i] in multitab:
        continue
    cnt += 1
    max_ind = -1
    max_num = -1
    s = li[i:]
    mul = list(multitab)
    for j in range(N):
        num = mul[j] #조사할 전자기기
        if num not in s:
            max_num = num
            break
        ind = s.index(num)
        if  ind > max_ind:
            max_ind = ind
            max_num = num
    
    multitab.remove(max_num)
    multitab.add(li[i])

print(cnt)