# 최대공약수와 최소공배수 - Math (유클리드 호제법)
# GCD(a, b) = GCD(b, a % b), LCM = a * b // GCD(a, b)
import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

g = gcd(a, b)
print(g)
print(a * b // g)
