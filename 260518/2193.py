# 이친수: n자리 이친수의 개수 구하기 (DP)
# 핵심 아이디어:
#   dp[i][j] = i자리이고 마지막 비트가 j인 이친수의 개수
#   - 마지막이 0이면: 앞자리가 0 또는 1 모두 가능 → dp[i][0] = dp[i-1][0] + dp[i-1][1]
#   - 마지막이 1이면: 앞자리가 0만 가능(연속 1 금지) → dp[i][1] = dp[i-1][0]
#   - 1자리: dp[1][1] = 1 (이친수는 0으로 시작 불가)
#   답: dp[n][0] + dp[n][1]

import sys
input = sys.stdin.readline

n = int(input())

dp = [[0] * 2 for _ in range(n + 1)]
dp[1][1] = 1  # "1"만 1자리 이친수

for i in range(2, n + 1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]

print(dp[n][0] + dp[n][1])
