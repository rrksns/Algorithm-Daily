import sys
input = sys.stdin.readline

# 피보나치 수 2 - DP (큰 수 처리)
# f(0)=0, f(1)=1, f(n) = f(n-1) + f(n-2)
# n <= 90 → Python 큰 정수 그대로 처리 가능

n = int(input())
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n])
