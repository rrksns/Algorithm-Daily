# 3×N 보드를 2×1 타일로 채우는 경우의 수 (DP)
# 핵심 아이디어:
# - N이 홀수면 0 (3×N 칸 수가 홀수이므로 타일로 채울 수 없음)
# - dp[0]=1, dp[2]=3
# - 점화식: dp[n] = 4*dp[n-2] - dp[n-4]
# (3*dp[n-2] + 2*(dp[n-4]+...+dp[0]) 를 정리하면 위 점화식이 성립)
import sys
input = sys.stdin.readline

n = int(input())
if n % 2 == 1:
    print(0)
else:
    dp = [0] * (n + 1)
    dp[0] = 1
    if n >= 2:
        dp[2] = 3
    for i in range(4, n + 1, 2):
        dp[i] = 4 * dp[i-2] - dp[i-4]
    print(dp[n])
