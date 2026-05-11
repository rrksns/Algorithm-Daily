import sys
input = sys.stdin.readline

# 나무 자르기 - 이진 탐색
# 절단기 높이 H를 이진탐색으로 결정
# H를 올릴수록 얻는 나무 감소 → 최대 H이면서 M미터 이상 얻는 값 탐색

n, m = map(int, input().split())
trees = list(map(int, input().split()))

lo, hi = 0, max(trees)
while lo < hi:
    mid = (lo + hi + 1) // 2
    # mid 높이로 잘랐을 때 얻는 나무 총량
    total = sum(t - mid for t in trees if t > mid)
    if total >= m:
        lo = mid  # 더 높게 자를 수 있음
    else:
        hi = mid - 1

print(lo)
