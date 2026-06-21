# 행렬 곱셈 순서 - DP (구간 DP)
# dp[i][j] = i번째부터 j번째 행렬까지 곱하는 최소 연산 횟수
# dp[i][j] = min(dp[i][k] + dp[k+1][j] + r[i]*c[k]*c[j]) for k in range(i, j)
import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j]: i~j 행렬 곱의 최소 비용
dp = [[0] * n for _ in range(n)]

# 구간 길이 2부터 n까지
for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        dp[i][j] = float('inf')
        for k in range(i, j):
            cost = dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1]
            dp[i][j] = min(dp[i][j], cost)

print(dp[0][n-1])
