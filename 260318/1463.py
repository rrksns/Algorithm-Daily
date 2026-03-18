import sys

intput = sys.stdin.readline
N = int(input())

dp = [0] * 100000001

# dp[i] 숫자i를 만드는데 필요한 최소 연산횟수

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])
