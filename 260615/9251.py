# 백준 9251 - LCS (Longest Common Subsequence)
# 핵심 아이디어: 2D DP
# dp[i][j] = A의 i번째, B의 j번째 문자까지 고려했을 때 LCS 길이
# - A[i] == B[j] 이면: dp[i][j] = dp[i-1][j-1] + 1
# - A[i] != B[j] 이면: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

import sys
input = sys.stdin.readline

def solve():
    A = input().strip()
    B = input().strip()
    n, m = len(A), len(B)

    # dp[i][j]: A[:i], B[:j]의 LCS 길이
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print(dp[n][m])

solve()
