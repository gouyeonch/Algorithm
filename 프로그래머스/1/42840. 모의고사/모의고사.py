def solution(answers):#0622~0632
    a=[]
    b=[]
    c=[]
    while len(a) < len(answers):
        a+=[1,2,3,4,5]
    while len(b) < len(answers):
        b+=[2, 1, 2, 3, 2, 4, 2, 5]
    while len(c) < len(answers):
        c+=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
        
    print(a)
    print(b)
    print(c)
    
    cntA = cntB = cntC = 0
    for i in range(len(answers)):
        if a[i] == answers[i]: cntA+=1
        if b[i] == answers[i]: cntB+=1
        if c[i] == answers[i]: cntC+=1
    mm = max(cntA,cntB,cntC)
    res=[]
    if cntA==mm: res.append(1)
    if cntB==mm: res.append(2)
    if cntC==mm: res.append(3)
    return res