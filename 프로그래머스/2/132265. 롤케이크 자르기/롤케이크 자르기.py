def solution(topping):#0237
    LL = set()
    RR = set()
    
    reverse = topping[::-1]
    
    setL = []
    for t in topping:
        LL.add(t)
        setL.append(len(LL))
    
    setR = []
    for r in reverse:
        RR.add(r)
        setR.append(len(RR))
    setR.reverse()
    
    cnt = 0
    for i in range(len(topping)-1):
        if setL[i] == setR[i+1]:
            cnt+=1
    
    return cnt