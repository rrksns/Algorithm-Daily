# [분할정복] Z
# 핵심 아이디어:
# 2^N × 2^N 배열을 Z 모양(좌상→우상→좌하→우하)으로 재귀 방문할 때
# (r, c)가 속한 사분면을 판단하여 이전 사분면 크기(half*half)를 누적하고
# 재귀적으로 좌표를 절반씩 줄여 O(N) 시간에 답을 구한다.

import sys
input = sys.stdin.readline

def solve(n, r, c):
    if n == 0:
        return 0
    half = 2 ** (n - 1)
    quad_size = half * half
    if r < half and c < half:
        # 1사분면 (좌상)
        return solve(n - 1, r, c)
    elif r < half and c >= half:
        # 2사분면 (우상)
        return quad_size + solve(n - 1, r, c - half)
    elif r >= half and c < half:
        # 3사분면 (좌하)
        return 2 * quad_size + solve(n - 1, r - half, c)
    else:
        # 4사분면 (우하)
        return 3 * quad_size + solve(n - 1, r - half, c - half)

N, r, c = map(int, input().split())
print(solve(N, r, c))
