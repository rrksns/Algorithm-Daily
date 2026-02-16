import sys
input = sys.stdin.readline

# 입력: n(동전 종류 수), k(목표 금액)
n, k = map(int, input().split())

# 각 동전의 가치 입력
coins = [int(input()) for _ in range(n)]

# dp[i] = i원을 만드는 경우의 수
dp = [0] * (k + 1)
dp[0] = 1  # 0원을 만드는 경우의 수 = 1 (아무 동전도 사용하지 않음)

# 각 동전에 대해 순서대로 처리 (순서 중복 방지)
for coin in coins:
    for j in range(coin, k + 1):
        dp[j] += dp[j - coin]

# 결과 출력
print(dp[k])