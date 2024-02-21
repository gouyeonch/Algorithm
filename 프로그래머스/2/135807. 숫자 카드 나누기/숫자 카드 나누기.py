def solution(arrayA, arrayB):
    def uc(a,b):
        while a%b != 0:
            tmp = a
            a = b
            b = tmp%b
        return b
    
    #철수
    AA = 0
    a=arrayA[0]
    for i in range(1,len(arrayA)):
        if a == 1: 
            break
        # print("a")
        # print(a)
        # print("arrayA[i]")
        # print(arrayA[i])
        a = uc(a, arrayA[i])
    if a != 1:
        f = 0
        for b in arrayB:
            if b%a == 0:
                f = 1
                break
        if f == 0:
            AA = a
    
    # 영희
    BB = 0
    a=arrayB[0]
    for i in range(1,len(arrayB)):
        if a == 1: 
            break
        # print("a")
        # print(a)
        # print("arrayA[i]")
        # print(arrayA[i])
        a = uc(a, arrayB[i])
    if a != 1:
        f = 0
        for b in arrayA:
            if b%a == 0:
                f = 1
                break
        if f == 0:
            BB = a
    
    return max(AA,BB)