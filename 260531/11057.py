# 오르막 수 - DP
# dp[i][j]: 길이 i이고 마지막 자리가 j인 오르막 수의 개수
# dp[i][j] = sum(dp[i-1][k] for k in 0..j)
# 답: sum(dp[N][j] for j in 0..9) mod 10007

import sys
input = sys.stdin.readline

MOD = 10007
N = int(input())

dp = [[0] * 10 for _ in range(N + 1)]
for j in range(10):
    dp[1][j] = 1

for i in range(2, N + 1):
    for j in range(10):
        for k in range(j + 1):
            dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD

print(sum(dp[N]) % MOD)
