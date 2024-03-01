def solution(targets):#0237~0300
    targets.sort()
    
    cnt = 0
    now = []
    for i in range(len(targets)):
        if not now:
            cnt += 1
            now = targets[i]
        else:
            nowMax =  max(now[0], targets[i][0]) 
            nowMin = min(now[1], targets[i][1])
            if nowMax < nowMin:
                now = [nowMax, nowMin]
            else:
                cnt += 1
                now = targets[i]
        
        
    return cnt