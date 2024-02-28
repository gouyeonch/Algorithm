def solution(citations):
    citations.sort()
    
    ll = len(citations)
    
    res = 0
    for i in range(ll):
        if citations[i] >= (ll - i):
            res = ll-i
            break
        
    return res
