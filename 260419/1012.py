import sys
from collections import deque

input = sys.stdin.readline


dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def bfs(sy, sx, n, m, board, visited):
    q = deque([(sy, sx)])
    visited[sy][sx] = True

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if board[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))  # 빠트림
    return 1


tc = int(input())

for c in range(tc):
    m, n, k = map(int, input().split())

    board = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        bx, by = map(int, input().split())
        board[by][bx] = 1

    need = 0
    for y in range(n):
        for x in range(m):
            if board[y][x] == 1 and not visited[y][x]:
                need += bfs(y, x, n, m, board, visited)
    print(need)
