from itertools import permutations
from math import sqrt

def solution(numbers):# 0647 ~ 0707
    ll = int(sqrt(9999999))
    SS = [0]*(9999999+1)
    SS[0] = SS[1] = 1
    
    for i in range(1,10,3):
        print(i)
    for i in range(2, ll+1):
        for j in range(i+i, 9999999+1, i):
           SS[j] = 1
    li = [] 
    for i in range(len(numbers),0,-1):
        for l in set(list(permutations(numbers,i))):
            li.append(int("".join(l)))
    li = list(set(li))
    print(li)
    cnt=0
    for l in li:
        if SS[l] == 0: cnt+=1
    return cnt