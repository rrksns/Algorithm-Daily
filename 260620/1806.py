# 부분합 - 투 포인터 (슬라이딩 윈도우)
# 아이디어: 연속 수열의 합이 S 이상인 최소 길이 구하기
# left, right 포인터로 합이 S 이상이면 left를 줄여 최소 길이 갱신
import sys
input = sys.stdin.readline

def solve():
    N, S = map(int, input().split())
    nums = list(map(int, input().split()))
    left = 0
    total = 0
    ans = float('inf')

    for right in range(N):
        total += nums[right]
        while total >= S:
            ans = min(ans, right - left + 1)
            total -= nums[left]
            left += 1

    print(0 if ans == float('inf') else ans)

solve()
