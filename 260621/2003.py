# 수들의 합 2 - 투 포인터
# 아이디어: 연속 부분 수열의 합이 M인 경우의 수
# left, right 포인터로 합 비교 → 작으면 right 증가, 크면 left 증가, 같으면 카운트
import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    left = 0
    total = 0
    count = 0

    for right in range(N):
        total += nums[right]
        while total > M and left <= right:
            total -= nums[left]
            left += 1
        if total == M:
            count += 1

    print(count)

solve()
