import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

dp = [[-1] * n for _ in range(m)]
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]


def dfs(y, x):
    if y == m - 1 and x == n - 1:
        return 1  # 목적지 도달 → 경로 1개
    if dp[y][x] != -1:  # ✅ 메모이제이션 "조회"
        return dp[y][x]  # 이미 계산됨 → 캐시 반환

    dp[y][x] = 0  # 방문 시작 (0으로 초기화)

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < m and 0 <= nx < n:
            if graph[ny][nx] < graph[y][x]:  # 내리막 조건
                dp[y][x] += dfs(ny, nx)  # 하위 경로 수 누적

    return dp[y][x]  # ✅ 메모이제이션 "저장"


print(dfs(0, 0))
