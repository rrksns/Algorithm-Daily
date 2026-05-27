# 제곱수의 합 (BOJ 1699) - DP
#
# 핵심 아이디어:
# dp[i] = i를 완전제곱수의 합으로 나타낼 때 필요한 항의 최솟값
# 점화식: dp[i] = min(dp[i - j*j] + 1)  (j*j <= i인 모든 j)
# 기저 조건: dp[0] = 0
# 예) dp[4] = dp[4-4] + 1 = dp[0] + 1 = 1  (4 = 2²)
#     dp[5] = min(dp[4]+1, dp[1]+1) = 2     (5 = 4+1)

import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    dp = [float('inf')] * (N + 1)
    dp[0] = 0

    for i in range(1, N + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1

    print(dp[N])

solve()
