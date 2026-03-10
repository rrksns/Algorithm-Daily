import sys
from collections import deque
input = sys.stdin.readline

def solve():
    N, L, R = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def bfs(start_r, start_c, visited):
        """BFS로 연합 국가 찾기: 인구 차이가 [L, R] 범위인 나라들을 하나의 연합으로 묶음"""
        q = deque([(start_r, start_c)])
        visited[start_r][start_c] = True
        union = [(start_r, start_c)]

        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + dx[i], c + dy[i]
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                    diff = abs(A[r][c] - A[nr][nc])
                    if L <= diff <= R:
                        visited[nr][nc] = True
                        q.append((nr, nc))
                        union.append((nr, nc))

        return union

    days = 0

    while True:
        visited = [[False] * N for _ in range(N)]
        moved = False  # 이번 날 인구 이동이 발생했는지 여부

        # 모든 칸을 순회하며 미방문 칸에 대해 BFS 수행
        for r in range(N):
            for c in range(N):
                if not visited[r][c]:
                    union = bfs(r, c, visited)

                    # 연합 크기가 2 이상이면 인구 이동 발생
                    if len(union) > 1:
                        moved = True
                        avg = sum(A[ur][uc] for ur, uc in union) // len(union)
                        for ur, uc in union:
                            A[ur][uc] = avg

        if not moved:
            break  # 더 이상 인구 이동이 없으면 종료

        days += 1

    print(days)

solve()