# 01타일 - DP
# 길이 N인 타일을 1(길이 1짜리)과 00(길이 2짜리)으로 채우는 경우의 수
# dp[i] = dp[i-1] + dp[i-2] (피보나치와 동일한 점화식)
# dp[i-1]: 마지막에 1을 붙이는 경우
# dp[i-2]: 마지막에 00을 붙이는 경우
# 15746으로 나눈 나머지 출력

import sys
input = sys.stdin.readline

N = int(input())
if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    dp = [0] * (N + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, N + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
    print(dp[N])
