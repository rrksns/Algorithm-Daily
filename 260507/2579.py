import sys
input = sys.stdin.readline

# 계단 오르기 - DP
# 규칙: 연속 3칸 불가, 마지막 칸은 반드시 밟아야 함
# dp[i] = i번째 계단까지의 최대 점수
# 점화식:
#   dp[i] = max(
#     dp[i-2] + stair[i],          # i-1 건너뛰고 i 밟기
#     dp[i-3] + stair[i-1] + stair[i]  # i-2 건너뛰고 i-1, i 연속 밟기
#   )

n = int(input())
stair = [0] + [int(input()) for _ in range(n)]

if n == 1:
    print(stair[1])
elif n == 2:
    print(stair[1] + stair[2])
else:
    dp = [0] * (n + 1)
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]
    for i in range(3, n + 1):
        dp[i] = max(dp[i-2] + stair[i],
                    dp[i-3] + stair[i-1] + stair[i])
    print(dp[n])
