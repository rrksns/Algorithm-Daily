# 두 용액 - 투 포인터 (Two Pointer)
# 아이디어: 정렬 후 양 끝에서 포인터를 좁혀가며 합이 0에 가장 가까운 쌍 탐색
# - left + right > 0 이면 right를 줄임 (합을 작게)
# - left + right < 0 이면 left를 늘림 (합을 크게)
# - 절댓값이 더 작으면 정답 갱신

import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    liquids = list(map(int, input().split()))
    liquids.sort()

    left, right = 0, N - 1
    best_sum = float('inf')
    ans = (liquids[0], liquids[1])

    while left < right:
        s = liquids[left] + liquids[right]
        if abs(s) < best_sum:
            best_sum = abs(s)
            ans = (liquids[left], liquids[right])
        if s < 0:
            left += 1
        elif s > 0:
            right -= 1
        else:
            break

    print(ans[0], ans[1])

solve()
