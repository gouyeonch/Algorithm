import sys

n = int(sys.stdin.readline())

while n != -1:
    res = []
    sum = 0

    for i in range(1, n):
        if n % i == 0:
            res.append(str(i))
            sum += i
    
    if sum == n:
        print(str(n) + " = " + " + ".join(res))
    else:
        print(str(n) + " is NOT perfect.")

    n = int(sys.stdin.readline())