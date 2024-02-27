def solution(k, ranges): # 0104~0124
    nlist = [k]
    while k != 1:
        if k%2 == 1:
            k = (k*3) + 1
        else:
            k /= 2
        nlist.append(k)
    print(nlist)
    squ = [0]
    for i in range(1,len(nlist)):
        squ.append(((nlist[i]+nlist[i-1])/2) + squ[i-1])
    print(squ)
    
    res = []
    for r in ranges:
        a = r[0]
        b = len(nlist) + r[1] -1
        if b < a:
            res.append(-1)
            continue
        res.append(squ[b] - squ[a])
        
    return res