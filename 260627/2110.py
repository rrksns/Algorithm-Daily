# 공유기 설치 - 이진 탐색 (Binary Search)
# 아이디어: 공유기 간 최소 거리를 이진 탐색으로 결정
# - mid 거리로 공유기를 탐욕적으로 배치할 때 C개 이상 놓을 수 있으면 거리를 늘림
# - 집을 정렬 후, 첫 집부터 mid 이상 떨어진 집에 순서대로 배치

import sys
input = sys.stdin.readline

def can_place(houses, C, mid):
    count = 1
    last = houses[0]
    for h in houses[1:]:
        if h - last >= mid:
            count += 1
            last = h
    return count >= C

def solve():
    N, C = map(int, input().split())
    houses = [int(input()) for _ in range(N)]
    houses.sort()

    lo, hi = 1, houses[-1] - houses[0]
    ans = 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if can_place(houses, C, mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    print(ans)

solve()
