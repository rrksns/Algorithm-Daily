import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

dist = [[0] * m for _ in range(n)]
dist[0][0] = 1  # 시작점 거리 = 1


def bfs(sy, sx):
    q = deque([(sy, sx)])
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if board[ny][nx] == 1 and dist[ny][nx] == 0:
                    dist[ny][nx] = dist[cy][cx] + 1  # ✅ 이전 거리 + 1
                    q.append((ny, nx))


bfs(0, 0)
print(dist[n - 1][m - 1])  # ✅ 도착점의 거리 출력
