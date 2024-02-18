

def solution(nums):
    dd = set()
    ll = len(nums)//2
    for i in range(len(nums)):
        dd.add(nums[i])
    
    if ll < len(dd):
        return ll
    else:
        return len(dd)
    return answer