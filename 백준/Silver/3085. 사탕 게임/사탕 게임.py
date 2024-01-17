import sys

input = sys.stdin.readline

N = int(input())

li_col = [[] for _ in range(N)]
li_row = [[] for _ in range(N)]

max_cnt = 0

def check(list):
    max_alp = 0
    cnt = 1
    for i in range(1, N):
        if list[i] == list[i-1]:
            cnt+=1
        else:
            max_alp = max(max_alp, cnt)
            cnt = 1

    max_alp = max(max_alp, cnt)
    
    return max_alp

# 행 리스트도 생성
for i in range(N):
    li_col[i] = list(input().rstrip())

# 열 리스트도 생성
for i in range(N):
    for j in range(N):
        li_row[i].append(li_col[j][i])
        
for i in range(N):
    for j in range(N-1):
        # 원소 바꿨을 때 최대 몇개인지 체크

        # 행 바꾸기
        li_col[i][j], li_col[i][j+1] = li_col[i][j+1], li_col[i][j]
        li_row[j+1][i], li_row[j][i] = li_row[j][i], li_row[j+1][i]

        # 행 체크
        max_cnt = max(max_cnt, check(li_col[i]))
        max_cnt = max(max_cnt, check(li_row[j]))
        max_cnt = max(max_cnt, check(li_row[j+1]))

        # 행 되돌리기
        li_col[i][j], li_col[i][j+1] = li_col[i][j+1], li_col[i][j]
        li_row[j+1][i], li_row[j][i] = li_row[j][i], li_row[j+1][i]

        # 열 바꾸기
        li_row[i][j], li_row[i][j+1] = li_row[i][j+1], li_row[i][j]
        li_col[j+1][i], li_col[j][i] = li_col[j][i], li_col[j+1][i]

        # 열 체크
        max_cnt = max(max_cnt, check(li_row[i]))
        max_cnt = max(max_cnt, check(li_col[j]))
        max_cnt = max(max_cnt, check(li_col[j+1]))

            
        # 열 되돌리기
        li_row[i][j], li_row[i][j+1] = li_row[i][j+1], li_row[i][j]
        li_col[j+1][i], li_col[j][i] = li_col[j][i], li_col[j+1][i]


print(max_cnt)