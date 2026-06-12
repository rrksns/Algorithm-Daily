# 연구소: 빈 칸에 벽 3개 추가 후 BFS로 바이러스 확산 → 안전 구역 최대화
# 완전탐색(벽 위치 조합 C(빈칸수,3)) + BFS O(NM) → 전체 O(C*NM)
import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

empty = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 0]
viruses = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 2]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(grid):
    visited = [row[:] for row in grid]
    q = deque(viruses)
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                visited[nx][ny] = 2
                q.append((nx, ny))
    return sum(row.count(0) for row in visited)

ans = 0
for walls in combinations(range(len(empty)), 3):
    for w in walls:
        r, c = empty[w]
        lab[r][c] = 1
    ans = max(ans, bfs(lab))
    for w in walls:
        r, c = empty[w]
        lab[r][c] = 0

print(ans)
