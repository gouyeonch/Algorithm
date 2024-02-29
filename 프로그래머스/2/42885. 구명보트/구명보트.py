def solution(people, limit): #0400
    people.sort(reverse=True)
    
    cnt = 0
    for p in people:
        tmp = p
        for i in range(len(people)-1, -1,-1):
            if tmp + people[i] <= limit:
                tmp += people[i]
                people.pop()
            break
        cnt+=1
    
    return cnt