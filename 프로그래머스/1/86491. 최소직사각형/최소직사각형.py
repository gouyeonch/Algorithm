def solution(sizes): #0600~0610
    x=0
    y=0
    for s in sizes:
        if s[0] > s[1]:
            s[0],s[1] = s[1],s[0]
        x = max(x,s[0])
        y = max(y,s[1])
    print(x)
    print(y)

            
    return x*y