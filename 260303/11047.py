import sys
input = sys.stdin.readline

# 동전 종류 N개, 목표 금액 K
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

count = 0
# 큰 동전부터 사용 (그리디)
for coin in reversed(coins):
    if coin <= K:
        count += K // coin
        K %= coin

print(count)