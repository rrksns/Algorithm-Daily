# Dance Dance Revolution - DP
# 두 발의 위치(left, right)를 상태로 dp 적용
# dp[left][right] = 최솟값 에너지
# 각 명령마다 왼발 또는 오른발을 이동
# 비용: 중앙(0)->어딘가: 2, 같은 위치: 1, 인접: 3, 반대: 4

import sys
input = sys.stdin.readline

def cost(a, b):
    if a == 0:
        return 2
    if a == b:
        return 1
    if abs(a - b) == 2:
        return 4
    return 3

INF = float('inf')
dp = [[INF] * 5 for _ in range(5)]
dp[0][0] = 0

commands = []
while True:
    x = int(input())
    if x == 0:
        break
    commands.append(x)

for cmd in commands:
    ndp = [[INF] * 5 for _ in range(5)]
    for l in range(5):
        for r in range(5):
            if dp[l][r] == INF:
                continue
            # 왼발 이동
            nl = cmd
            ndp[nl][r] = min(ndp[nl][r], dp[l][r] + cost(l, cmd))
            # 오른발 이동
            nr = cmd
            ndp[l][nr] = min(ndp[l][nr], dp[l][r] + cost(r, cmd))
    dp = ndp

ans = INF
for l in range(5):
    for r in range(5):
        ans = min(ans, dp[l][r])
print(ans)
