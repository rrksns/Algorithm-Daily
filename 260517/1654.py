# 랜선 자르기 - 이진 탐색 (Parametric Search)
# K개의 랜선을 잘라 N개 이상의 동일 길이 랜선을 만들 때 최대 길이 구하기
# 길이 L로 자를 때 얻는 개수 = sum(cable_i // L)
# 이 개수 >= N이 되는 최대 L을 이진탐색으로 찾는다

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]

lo, hi = 1, max(cables)
ans = 0

while lo <= hi:
    mid = (lo + hi) // 2
    count = sum(c // mid for c in cables)
    if count >= N:
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(ans)
