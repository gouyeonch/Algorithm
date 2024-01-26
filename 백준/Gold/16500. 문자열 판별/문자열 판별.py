import sys

input = sys.stdin.readline

S = list(str(input().rstrip()))
S_len = len(S)

N = int(input())

words = []
for _ in range(N):
    words.append(str(input().rstrip()))

dp = [0] * (S_len+1)
dp[0] = 1

for i in range(1, S_len+1):
    for word in words:
        word_len = len(word)
        if word_len <= i and S[i-word_len : i] == list(word) and dp[i-word_len] == 1:
            dp[i] = 1

if dp[S_len] == 1:
    print(1)
else:
    print(0)
