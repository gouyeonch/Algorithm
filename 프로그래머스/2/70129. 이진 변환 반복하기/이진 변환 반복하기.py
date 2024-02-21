def solution(s):
    cnt_0 = 0
    res = 0
    
    def toBin(num):
        tmp = 1
        cntt = 0
        while num >= tmp:
            tmp *= 2
            cntt += 1
        res = []
        for i in range(cntt, 0, -1):
            tmp = tmp // 2
            rr = num // tmp
            num = num % tmp
            res.append(str(rr))
            
        return "".join(res)
        
    def trans(str):
        cnt = 0
        tt = str.count('0')
        cnt += tt
        num = len(str) - tt
        
        return (cnt,num)
    
    while s != "1":
        res += 1
        cc, bb = trans(s)
        cnt_0 += cc
        s = toBin(bb)
    
    return [res, cnt_0]