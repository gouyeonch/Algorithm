import sys

input = sys.stdin.readline

li = []

for i in range(9):
    li.append(int(input()))

li.sort()

sum_ = sum(li)

for i in range(9):
    for j in range(i+1, 9):
        if sum_ - li[i] - li[j] == 100:
            for k in range(9):
                if k != i and k != j:
                    print(li[k])
            exit()