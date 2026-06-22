# 고층 빌딩 - DP (경우의 수)
# 핵심 아이디어: dp[i][j][k] = i개의 빌딩 배치에서 왼쪽 j개, 오른쪽 k개 보이는 경우의 수
# 전이: 가장 낮은 빌딩(높이 1)을 추가하는 방식
#   - 맨 왼쪽에 추가: 왼쪽에서 보임 → dp[i+1][j+1][k] += dp[i][j][k]
#   - 맨 오른쪽에 추가: 오른쪽에서 보임 → dp[i+1][j][k+1] += dp[i][j][k]
#   - 중간 삽입 (i-1개 위치): 보이지 않음 → dp[i+1][j][k] += dp[i][j][k] * (i-1)

import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
MOD = 1000000007

dp = [[[0] * (N + 2) for _ in range(N + 2)] for _ in range(N + 2)]
dp[1][1][1] = 1

for i in range(1, N):
    for j in range(1, i + 1):
        for k in range(1, i + 1):
            if dp[i][j][k] == 0:
                continue
            v = dp[i][j][k]
            # 맨 왼쪽에 추가
            dp[i+1][j+1][k] = (dp[i+1][j+1][k] + v) % MOD
            # 맨 오른쪽에 추가
            dp[i+1][j][k+1] = (dp[i+1][j][k+1] + v) % MOD
            # 중간 삽입
            dp[i+1][j][k] = (dp[i+1][j][k] + v * (i - 1)) % MOD

print(dp[N][L][R])
