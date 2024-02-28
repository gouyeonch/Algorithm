def solution(numbers):
    ss = list(map(str,numbers))
    ss.sort(key=lambda k : k*3, reverse=True)
    return str(int("".join(ss)))