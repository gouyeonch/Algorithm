import sys

def cant(A):
    if len(A) == 1:
        return A
    
    m = len(A)//3

    A[0:m] = cant(A[0:m])
    A[m:m*2] = [' ' for _ in range(m*1,m*2)]
    A[m*2:m*3] = cant(A[m*2:m*3])

    return A

while True:
    try:
        n = int(sys.stdin.readline())

        A = ['-' for _ in range(3**n)]

        cant(A)
        print("".join(A))

    except:
        break