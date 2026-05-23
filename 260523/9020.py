# 골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 표현 가능
# 에라토스테네스의 체로 소수를 구한 후, n//2에서 양쪽으로 탐색하며
# 두 소수의 합이 n이 되는 경우 중 차이가 가장 작은 쌍을 출력

import sys
input = sys.stdin.readline

def solve():
    # 에라토스테네스의 체 (10000 이하)
    MAX = 10001
    is_prime = [True] * MAX
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(MAX**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, MAX, i):
                is_prime[j] = False

    T = int(input())
    for _ in range(T):
        n = int(input())
        # n//2에서 시작해 좌우로 탐색 → 차이가 가장 작은 쌍을 먼저 발견
        mid = n // 2
        for a in range(mid, 1, -1):
            b = n - a
            if is_prime[a] and is_prime[b]:
                print(a, b)
                break

solve()
