import sys

a = list(map(int, input().split()))
sum = 0
for n in a:
    sum += n
print(sum)