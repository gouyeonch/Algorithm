import sys

time, min = input().split()
num = input()

time = int(time)
min = int(min)
num = int(num)

sol = time*60 + min + num

time = (sol / 60) % 24
min = sol % 60

time = int(time)
min = int(min)

print(str(time) + " " + str(min))