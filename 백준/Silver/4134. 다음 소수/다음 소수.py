import sys

def isDeno(n):
    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            return 1
    return 0

n = int(sys.stdin.readline())


for _ in range(n):
    num = int(sys.stdin.readline())

    if num == 0 or num == 1:
        print(2)
    else:
        while(isDeno(num)):
            num += 1
        print(num)