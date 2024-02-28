from itertools import product

def solution(word): #0752
    li=[]
    for i in range(5,0,-1):
        li += list(map("".join, list(product(['A','E','I','O','U'],repeat=i))))
        
    li.sort()
    return li.index(word)+1
