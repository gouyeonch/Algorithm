import sys

def dfs(x, y):
    global count
    visitied[x][y] = 1
    count += 1
    
    for i, j in li[x][y]:
        if visitied[i][j] != 1:
            dfs(i, j)

#맵 크기 입력 받기
N = int(sys.stdin.readline())

# 맵 입력받기
m = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    s = sys.stdin.readline()
    for j in range(N):
        m[i][j] = int(s[j])

#방문 리스트 생성 및 초기화
visitied = [[0 for _ in range(N)] for _ in range(N)]

#인접 리스트 초기화
li = [[[] for _ in range(N) ] for _ in range(N)]

#인접 리스트 생성
for i in range(N):
    for j in range(N):
        if m[i][j] == 1:
            if i != 0 and m[i-1][j] == 1:
                li[i][j].append([i-1, j])
            if i != N-1 and m[i+1][j] ==1:
                li[i][j].append([i+1, j])
            if j != 0 and m[i][j-1] == 1:
                li[i][j].append([i, j-1])
            if j != N-1 and m[i][j+1] ==1:
                li[i][j].append([i, j+1])

#각 단지 수를 출력할 배열
group = []

groupCount = 0

#dfs함수 호출 및 연결요소 체크
for i in range(N):
    for j in range(N):

        count = 0

        if visitied[i][j] != 1 and m[i][j] != 0:
            groupCount += 1
            dfs(i, j)

            if count != 0:
                group.append(count)

#결과 출력
group.sort()

print(groupCount)

for g in group:
    print(g)