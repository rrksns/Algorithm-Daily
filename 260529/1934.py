# 최소공배수 - Math
# lcm(a, b) = a * b // gcd(a, b)
import sys
input = sys.stdin.readline
from math import gcd

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))
