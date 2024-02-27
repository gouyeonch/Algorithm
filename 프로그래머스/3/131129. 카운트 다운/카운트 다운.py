INF = 987654321

def create_table():
    arr = []
    arr.append([i for i in range(1,21)])
    arr[0].append(50)
    
    tmp = set()
    for i in range(1,21):
        for j in range(2,4):
            r = i*j
            if r > 20:
                tmp.add(i*j)
    arr.append(list(tmp))
    return arr
INF =987654321
def solution(target):
    table = create_table()
    dp = [[INF,0] for _ in range(target+1)]
    dp[0][0] = 0
    for i in range(1,target+1):
        for j in range(2):
            for k in range(len(table[j])):
                prev = i - table[j][k]
                
                if prev < 0:
                    continue
                
                point, pl = dp[prev][0] + 1, dp[prev][1] + 1 - j
                
                if point < dp[i][0]:
                    dp[i] = [point, pl]
                elif point == dp[i][0]:
                    dp[i] = [point, max(dp[i][1], pl)]
    return dp[target]