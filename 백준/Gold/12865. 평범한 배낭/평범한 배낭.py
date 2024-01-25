# 이해해보니 신셰계가 동전2 같은 문제들도 전부다 이걸로 풀 수 있다 y축을 체크포인트 x축을 dp 라고 생각하자 현재 검사하는 배낭이 최적값을 구하는데 동조 할 수 있는지 3짜리 배낭은 무게 3부터 일일히 이전 케이스와 비교한다 때문에 모든 케이스 고려
# 일차원 dp로 푼다고 생각하면 체크포인트 배열을 일일히 만들었었지만 이러면 훨씬 간단
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

knapsack = [[0,0]]

for _ in range(N):
    knapsack.append(list(map(int, input().split())))

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    weight = knapsack[i][0]
    value = knapsack[i][1]
    for j in range(1, K+1):
        if weight <= j:
            dp[i][j] = max(dp[i-1][j], value + dp[i-1][j-weight])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])