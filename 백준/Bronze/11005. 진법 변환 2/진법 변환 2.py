import sys

resStr = ""

n, b = map(int, sys.stdin.readline().split())

state = 1
stateInx = 1

while n >= state*b:
    state *= b
    stateInx += 1

for i in range(stateInx):
    temp = n / state
    n = n % state
    state = state / b

    temp =  int(temp)

    if temp < 10:
        resStr = resStr + str(temp)
    else:
        resStr = resStr + chr(ord('A') + temp - 10)

print(resStr)
