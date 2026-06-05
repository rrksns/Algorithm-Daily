# [DP] 피보나치 수 5 - BOJ 10870
# F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)
# n <= 20이므로 단순 반복으로 충분

import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    if n == 0:
        print(0)
        return
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    print(b)

solve()
