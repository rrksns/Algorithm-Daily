# 백준 1644 - 소수의 연속합
# 핵심 아이디어: 에라토스테네스의 체로 소수 목록을 구한 뒤,
#   투 포인터(Two Pointer) 기법으로 연속된 소수의 합이 N이 되는 경우의 수를 셈
#   - left, right 포인터로 구간의 합을 관리
#   - 합 < N: right 확장 / 합 > N: left 축소 / 합 == N: 카운트 후 left 축소

import sys
input = sys.stdin.readline

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [i for i in range(2, n+1) if is_prime[i]]

def main():
    n = int(input())
    primes = sieve(n)
    
    count = 0
    left = 0
    total = 0
    
    for right in range(len(primes)):
        total += primes[right]
        while total > n and left <= right:
            total -= primes[left]
            left += 1
        if total == n:
            count += 1
    
    print(count)

main()
