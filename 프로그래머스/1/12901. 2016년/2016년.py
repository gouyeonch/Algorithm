def solution(a, b):
    dd = dict()
    dd[1] = 31
    dd[2] = 29
    dd[3] = 31
    dd[4] = 30
    dd[5] = 31
    dd[6] = 30
    dd[7] = 31
    dd[8] = 31
    dd[9] = 30
    dd[10] = 31
    dd[11] = 30
    dd[12] = 31
    
    m = 0
    for i in range(1, a):
        m += dd[i]
    m += b-1
    
    m %= 7
    
    MM = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    return MM[m]
    
