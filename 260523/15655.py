# N과 M (6): N개의 자연수 중 M개를 선택, 오름차순(비내림차순) 출력
# 조합(Combination) - 입력 배열 정렬 후 백트래킹으로 인덱스 기반 탐색
# 선택한 인덱스보다 큰 인덱스만 재귀 탐색 → 자동으로 오름차순 보장

import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    nums = sorted(map(int, input().split()))
    result = []

    def backtrack(start, chosen):
        if len(chosen) == M:
            result.append(' '.join(map(str, chosen)))
            return
        for i in range(start, N):
            chosen.append(nums[i])
            backtrack(i + 1, chosen)
            chosen.pop()

    backtrack(0, [])
    print('\n'.join(result))

solve()
