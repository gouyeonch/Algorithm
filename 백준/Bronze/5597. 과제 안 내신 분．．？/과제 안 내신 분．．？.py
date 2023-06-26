import sys

list = list(range(1, 31))

for i in range(28):
    ind = int(sys.stdin.readline())
    list[ind-1] = 0

new_list = [i for i in list if i != 0]

print(' '.join(map(str, new_list)))
