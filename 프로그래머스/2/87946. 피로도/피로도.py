from itertools import permutations

def solution(k, dungeons):#0737
    answer = -1
    
    dg = list(permutations(dungeons))
    
    res = 0
    for d in dg:
        tmp = k
        cnt = 0
        for dd in d:
            
            if dd[0] <= tmp:
                tmp-=dd[1]
                cnt+=1
            else:
                break
        res = max(res,cnt)
    
    return res