# 정수 삼각형 - Dynamic Programming
# 핵심 아이디어:
# 삼각형 위에서 아래로 내려가며, 각 위치에서 도달 가능한 최대 합을 누적한다.
# dp[i][j] = i번째 줄 j번째 수까지의 최대 합
# 점화식: dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
# 단, 가장 왼쪽(j=0)은 위쪽 왼쪽에서만, 가장 오른쪽은 위쪽 오른쪽에서만 올 수 있음

import sys
input = sys.stdin.readline

n = int(input())
triangle = []
for _ in range(n):
    row = list(map(int, input().split()))
    triangle.append(row)

dp = [[0] * (i + 1) for i in range(n)]
dp[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

print(max(dp[n-1]))
