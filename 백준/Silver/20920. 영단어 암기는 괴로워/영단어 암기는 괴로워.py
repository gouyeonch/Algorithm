import sys

n, m = map(int,sys.stdin.readline().split())

word_dic = {}

for i in range(n):
    word = sys.stdin.readline().rstrip()

    if len(word) >= m:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1

word_dic = sorted(word_dic.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for i in word_dic:
    print(i[0])