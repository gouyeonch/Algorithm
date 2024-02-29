def solution(numbers, target):#0800
    leaves = [0]
    for number in numbers:
        tmp = []
        
        for leaf in leaves:
            tmp.append(leaf+number)
            tmp.append(leaf-number)
        
        leaves = tmp
    cnt = 0
    for leaf in leaves:
        if target == leaf:
            cnt+=1
            
    return cnt