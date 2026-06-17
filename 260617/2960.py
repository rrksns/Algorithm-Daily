# BOJ 2960 - 에라토스테네스의 체 (Math)
# 핵심 아이디어:
# 에라토스테네스의 체를 그대로 시뮬레이션하면서
# 지워지는 순서를 세어 K번째로 지워지는 수를 출력한다.
# 2부터 순서대로 소수를 찾고, 해당 소수의 배수를 지운다.
# 아직 안 지워진 소수 자신도 지우는 횟수에 포함된다.
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
sieve = [True] * (N + 1)
count = 0

for i in range(2, N + 1):
    if sieve[i]:
        for j in range(i, N + 1, i):
            if sieve[j]:
                sieve[j] = False
                count += 1
                if count == K:
                    print(j)
                    exit()
