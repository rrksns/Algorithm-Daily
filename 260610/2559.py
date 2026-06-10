# 백준 2559 - 수열
# 핵심 아이디어: 누적 합(Prefix Sum)
# prefix[i] = 처음부터 i번째까지의 합
# 연속된 K일의 합 = prefix[i] - prefix[i-K]
# 이를 모든 구간에 대해 계산하여 최댓값 반환

import sys
input = sys.stdin.readline

def solve():
    N, K = map(int, input().split())
    temps = list(map(int, input().split()))

    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + temps[i]

    max_sum = -float('inf')
    for i in range(K, N + 1):
        max_sum = max(max_sum, prefix[i] - prefix[i - K])

    print(max_sum)

solve()
