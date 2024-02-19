#1031
#자리수 알아내기
# 자리수 부터 하나 씩 내려오면서 계산
def solution(n):
    answer = []
    
    while n:
        t = n%3
        if not t:
            t = 4
            n -= 1
            
        answer.append(str(t))
        n = n//3
    return "".join(answer[::-1])