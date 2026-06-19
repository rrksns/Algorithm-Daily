# 곱셈 - 분할정복 (빠른 거듭제곱)
# 아이디어: a^b mod c 계산 시 b를 절반씩 나눠 재귀
# b 짝수: a^b = (a^(b//2))^2, b 홀수: a^b = a * a^(b-1)
# 시간복잡도 O(log b)
import sys
input = sys.stdin.readline

def power(a, b, c):
    if b == 1:
        return a % c
    half = power(a, b // 2, c)
    result = (half * half) % c
    if b % 2 == 1:
        result = (result * a) % c
    return result

a, b, c = map(int, input().split())
print(power(a, b, c))
