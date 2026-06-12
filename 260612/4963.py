# 섬의 개수: 8방향 연결된 땅(1) 덩어리 수 세기
# BFS로 각 미방문 땅에서 탐색 → 섬 카운트 증가
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    grid = []
    for _ in range(h):
        grid.append(list(map(int, input().split())))
    
    visited = [[False]*w for _ in range(h)]
    count = 0
    
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not visited[i][j]:
                count += 1
                queue = deque([(i, j)])
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    for d in range(8):
                        nx, ny = x+dx[d], y+dy[d]
                        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
    print(count)
