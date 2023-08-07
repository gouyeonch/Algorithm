import sys

n = int(sys.stdin.readline())

student = list(map(int, sys.stdin.readline().split()))
student.reverse()
temp = []
temp.append(0)
flag = 1

for i in (range(1, n+1)):
    if temp[-1] == i:
        temp.pop()
    elif student.count(i) != 0:
        while True:
            p = student.pop()
            if p == i:
                break
            else:
                temp.append(p)
    else:
        flag = -1
        break

if flag == 1:
    print("Nice")
else:
    print("Sad")
