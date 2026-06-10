# 백준 2688 - 줄어들지 않아
# 핵심 아이디어: DP
# dp[i][d] = i자리 수이면서 마지막 자리가 d(0~9)인 줄어들지 않는 수의 개수
# 점화식: dp[i][d] = sum(dp[i-1][k] for k in range(0, d+1))
# 즉, 이전 자리 수가 현재 자리 수보다 작거나 같은 경우의 합

import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    MAX_N = 65
    # dp[i][d]: i자리, 마지막 숫자 d
    dp = [[0] * 10 for _ in range(MAX_N)]
    for d in range(10):
        dp[1][d] = 1

    for i in range(2, MAX_N):
        for d in range(10):
            for k in range(d + 1):
                dp[i][d] += dp[i-1][k]

    for _ in range(T):
        n = int(input())
        print(sum(dp[n]))

solve()
