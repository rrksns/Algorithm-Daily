import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    n, m = int(input_data[0]), int(input_data[1])
    grid = [input_data[2 + i] for i in range(n)]

    visited = [[False] * m for _ in range(n)]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for si in range(n):
        for sj in range(m):
            if visited[si][sj]:
                continue

            color = grid[si][sj]
            visited[si][sj] = True

            # BFS: (row, col, parent_row, parent_col)
            queue = deque([(si, sj, -1, -1)])

            while queue:
                r, c, pr, pc = queue.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == color:
                        if not visited[nr][nc]:
                            visited[nr][nc] = True
                            queue.append((nr, nc, r, c))
                        elif (nr, nc) != (pr, pc):
                            # 이미 방문한 이웃 (부모 제외) → 사이클 발견
                            print("Yes")
                            return

    print("No")

solve()