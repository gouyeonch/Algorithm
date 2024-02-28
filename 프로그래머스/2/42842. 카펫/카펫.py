from math import sqrt
def solution(brown, yellow): # 0715~0735
    li = []
    for i in range(1,int(sqrt(yellow))+1):
        if yellow % i == 0:
            li.append([i,yellow//i])
    
    for l in li:
        if l[0]*2 + l[1]*2 + 4 == brown:
            return [l[1]+2,l[0]+2]
