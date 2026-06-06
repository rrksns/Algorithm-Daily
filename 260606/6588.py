# [Math] 골드바흐의 추측 - BOJ 6588
# 4 이상의 짝수는 두 홀수 소수의 합으로 표현 가능
# 핵심 아이디어:
# - 에라토스테네스의 체로 1000000까지 소수 미리 계산
# - 각 짝수 n에 대해 3부터 n/2까지 소수 p 순회
#   → n-p도 소수이면 "n = p + (n-p)" 출력
# - 조건 "b-a가 최대"이므로 가장 작은 p부터 찾으면 됨

import sys
input = sys.stdin.readline

def solve():
    MAX = 1_000_001
    sieve = [True] * MAX
    sieve[0] = sieve[1] = False
    for i in range(2, int(MAX**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, MAX, i):
                sieve[j] = False

    while True:
        n = int(input())
        if n == 0:
            break
        found = False
        for p in range(3, n // 2 + 1, 2):
            if sieve[p] and sieve[n - p]:
                print(f"{n} = {p} + {n - p}")
                found = True
                break
        if not found:
            print("Goldbach's conjecture is wrong.")

solve()
