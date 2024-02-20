def solution(s):
    answer = 0
    for i in range(len(s)):
        cnt = 0
        # print("i")
        # print(s[i])
        for j in range(min(i+1, len(s)-i)):
            # print("j")
            # print(j)
            # print("s[i-j], s[i+j] : "+ str(s[i-j]) + " " + str(s[i+j]))
            if s[i-j] != s[i+j]:
                break
            cnt+=1
        if cnt*2-1 > answer:
            answer = cnt*2-1
    for i in range(1, len(s)):
        cnt = 0
        # print("i")
        # print(s[i])
        for j in range(min(i, len(s)-i)):
            # print("j")
            # print(j)
            # print("s[i-j-1], s[i+j] : "+ str(s[i-j-1]) + " " + str(s[i+j]))
            if s[i-j-1] != s[i+j]:
                break
            cnt+=1
        if cnt*2 > answer:
            answer = cnt*2
    
    return answer