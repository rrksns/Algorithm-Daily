import sys

input = sys.stdin.readline

n = int(input())


for i in range(n):
    m = int(input())
    dp = [0] * (max(m, 3) + 1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, m + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    print(dp[m])


# import sys
# input = sys.stdin.readline

# n = int(input())
# for i in range(n):
#     m = int(input())
#     dp = [0, 1, 2, 4] + [0] * max(0, m - 3)  # 기본값 미리 포함
#     for j in range(4, m + 1):
#         dp[j] = dp[j - 1] + dp[j - 2] + dp[j - 3]
#     print(dp[m])
