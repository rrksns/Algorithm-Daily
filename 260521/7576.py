# 토마토 BFS: 익은 토마토(1)를 모두 큐에 넣고 동시 BFS로 전파
# 최소 일수 = BFS 깊이, 미익은 토마토 남으면 -1 반환
import sys
from collections import deque
input = sys.stdin.readline

def solve():
    M, N = map(int, input().split())  # M: 열, N: 행
    grid = []
    q = deque()
    
    for r in range(N):
        row = list(map(int, input().split()))
        grid.append(row)
        for c in range(M):
            if row[c] == 1:
                q.append((r, c, 0))  # (행, 열, 날짜)
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    max_day = 0
    while q:
        r, c, day = q.popleft()
        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]
            if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 0:
                grid[nr][nc] = 1
                max_day = max(max_day, day + 1)
                q.append((nr, nc, day + 1))
    
    # 익지 않은 토마토가 남아있으면 -1
    for row in grid:
        if 0 in row:
            print(-1)
            return
    
    print(max_day)

solve()
