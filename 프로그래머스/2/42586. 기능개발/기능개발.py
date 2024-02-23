def solution(progresses, speeds): # 2:00 ~ 2:25
    
    def rest(p, sp):
        r = 100 - p
        if r < sp:
            return 1
        rr = r//sp
        if r%sp != 0:
            rr+=1
        return rr
    
    if len(speeds) == 0:
        return []
    
    answer = 0
    
    progresses[0] = rest(progresses[0], speeds[0])
    for i in range(1, len(progresses)):
        r = rest(progresses[i], speeds[i])
        if progresses[i-1] > r:
            progresses[i] = progresses[i-1]
        else:
            progresses[i] = r
    
    res = []
    cnt = 1
    for i in range(1, len(progresses)):
        if progresses[i-1] != progresses[i]:
            res.append(cnt)
            cnt = 1
        else:
            cnt += 1
    res.append(cnt)
    
    
    return res