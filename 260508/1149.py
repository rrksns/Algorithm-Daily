import sys
input = sys.stdin.readline

# RGB 거리 - DP
# 규칙: 인접한 집은 같은 색 불가
# dp[i][c] = i번째 집을 색 c(0:R, 1:G, 2:B)로 칠할 때 최솟값
# dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
# dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
# dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

dp = cost[0][:]
for i in range(1, n):
    new_dp = [0] * 3
    new_dp[0] = min(dp[1], dp[2]) + cost[i][0]
    new_dp[1] = min(dp[0], dp[2]) + cost[i][1]
    new_dp[2] = min(dp[0], dp[1]) + cost[i][2]
    dp = new_dp

print(min(dp))
