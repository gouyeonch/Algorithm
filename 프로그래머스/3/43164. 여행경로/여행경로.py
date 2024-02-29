from collections import deque

def solution(tickets): # 1100 ~ 1125
    queue = deque()
    queue.append(("ICN",["ICN"],[]))
    answer = []
    while queue:
        now, path, used = queue.popleft()
        
        if len(used) == len(tickets):
            answer.append(path)
        
        for ind, t in enumerate(tickets):
            if ind not in used and t[0] == now:
                queue.append([t[1], path + [t[1]], used + [ind]])
    answer.sort()
    return answer[0]