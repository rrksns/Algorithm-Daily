# 나이트의 이동 (백준 7562)
# 핵심 아이디어: 체스판에서 나이트의 L자 이동을 BFS로 탐색
# 최단 이동 횟수 = BFS의 레벨(깊이)
import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(l, sx, sy, ex, ey):
    if sx == ex and sy == ey:
        return 0
    visited = [[False] * l for _ in range(l)]
    visited[sx][sy] = True
    q = deque([(sx, sy, 0)])
    while q:
        x, y, dist = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                if nx == ex and ny == ey:
                    return dist + 1
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))

t = int(input())
for _ in range(t):
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    print(bfs(l, sx, sy, ex, ey))
