import sys

s = sys.stdin.readline()

strlen = len(s)-1

if(s[:int(strlen/2)] == s[int((strlen+1)/2):strlen][::-1]):
    print(1)
else:
    print(0)