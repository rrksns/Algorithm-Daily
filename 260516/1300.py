# [BinarySearch] K번째 수
# 핵심 아이디어:
# N×N 배열에서 A[i][j] = i*j (1-indexed)를 정렬했을 때 K번째 수 찾기
# 이진 탐색으로 mid값 이하인 원소의 개수를 구해 K번째 수를 특정
# i행에서 mid 이하인 원소 수 = min(mid // i, N) (i*j <= mid → j <= mid//i, 최대 N개)
# 이 합계가 K 이상이 되는 가장 작은 mid를 찾으면 K번째 수

import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    K = int(input())
    
    lo, hi = 1, K  # K번째 수는 최대 K (A[1][K] 또는 A[K][1])
    
    while lo < hi:
        mid = (lo + hi) // 2
        # mid 이하인 원소 수 계산
        count = sum(min(mid // i, N) for i in range(1, N + 1))
        if count >= K:
            hi = mid
        else:
            lo = mid + 1
    
    print(lo)

solve()
