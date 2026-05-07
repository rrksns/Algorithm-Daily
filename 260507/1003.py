import sys
input = sys.stdin.readline

# f(n)을 재귀 호출할 때 f(0), f(1)이 각각 몇 번 호출되는지 계산
# count0(n): f(n) 호출 시 f(0) 호출 횟수
# count1(n): f(n) 호출 시 f(1) 호출 횟수
# 점화식: count0(n) = count0(n-1) + count0(n-2)
#         count1(n) = count1(n-1) + count1(n-2)
# 기저값: count0(0)=1, count1(0)=0
#         count0(1)=0, count1(1)=1

MAX = 41
dp = [[0, 0] for _ in range(MAX)]  # dp[i] = [f(0) 호출수, f(1) 호출수]
dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, MAX):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n][0], dp[n][1])
