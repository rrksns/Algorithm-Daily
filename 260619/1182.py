# 부분수열의 합 - BackTracking(DFS)
# 아이디어: N개 원소 각각을 포함/미포함으로 2^N 경우의 수 탐색
# 현재 합이 S와 같고 공집합이 아닌 경우 카운트
import sys
input = sys.stdin.readline

def solve():
    N, S = map(int, input().split())
    nums = list(map(int, input().split()))
    count = 0

    def dfs(idx, total, picked):
        nonlocal count
        if idx == N:
            if picked > 0 and total == S:
                count += 1
            return
        dfs(idx + 1, total + nums[idx], picked + 1)  # 포함
        dfs(idx + 1, total, picked)                   # 미포함

    dfs(0, 0, 0)
    print(count)

solve()
