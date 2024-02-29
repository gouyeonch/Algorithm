from collections import deque

def solution(begin, target, words): # 0950~1010 12시까지 그래프 완료 2시까지 그리디 완료
    def isSame(s1,s2):
        cnt = 0
        
        s1 = list(s1)
        s2 = list(s2)
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                cnt+=1
        return cnt
    
    graph = [[] for _ in range(len(words))]
    
    for i in range(len(words)):
        for j in range(len(words)):
            if i!=j:
                if isSame(words[i],words[j]) == 1:
                    graph[i].append(j)
    print(graph)
    visit = [0] * (len(words))
    queue = deque()
    for i in range(len(words)):
        if isSame(words[i],begin) == 1:
            queue.append(i)
            visit[i] = 1
    print(queue)
    
    def bfs():
        while queue:
            print(queue)
            node = queue.popleft()
            print(words[node])
            print(visit[node])
            if words[node] == target:
                return visit[node]
            
            for n in graph[node]:
                if visit[n] == 0:
                    visit[n] = visit[node] + 1
                    queue.append(n)
        return 0
    
    return(bfs())
