# 벽 부수고 이동하기 - BFS (3차원 상태 공간)
# (행, 열, 벽_부순_횟수) 를 상태로 하는 BFS.
# 벽을 0번 또는 1번 부순 경우로 나누어 최단 거리 탐색.
# 상태: visited[r][c][broken] — broken=0: 아직 벽 안 부숨, broken=1: 이미 부숨
import sys
from collections import deque
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(input().strip())

    if N == 1 and M == 1:
        print(1)
        return

    # visited[r][c][broken]
    visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = True
    dq = deque()
    dq.append((0, 0, 0, 1))  # row, col, broken, dist

    dirs = [(-1,0),(1,0),(0,-1),(0,1)]

    while dq:
        r, c, broken, dist = dq.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                cell = board[nr][nc]
                if cell == '0':
                    if not visited[nr][nc][broken]:
                        visited[nr][nc][broken] = True
                        if nr == N-1 and nc == M-1:
                            print(dist + 1)
                            return
                        dq.append((nr, nc, broken, dist + 1))
                elif cell == '1' and broken == 0:
                    if not visited[nr][nc][1]:
                        visited[nr][nc][1] = True
                        if nr == N-1 and nc == M-1:
                            print(dist + 1)
                            return
                        dq.append((nr, nc, 1, dist + 1))

    print(-1)

solve()
