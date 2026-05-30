# 평범한 배낭 (0/1 Knapsack)
# 핵심 아이디어: 각 물건을 넣거나 안 넣는 경우를 고려하는 DP
# dp[j] = 무게 한도 j일 때 최대 가치
# 물건을 역순으로 순회해 중복 선택 방지

import sys
input = sys.stdin.readline

def solve():
    N, K = map(int, input().split())
    dp = [0] * (K + 1)
    
    for _ in range(N):
        W, V = map(int, input().split())
        for j in range(K, W - 1, -1):
            dp[j] = max(dp[j], dp[j - W] + V)
    
    print(dp[K])

solve()
