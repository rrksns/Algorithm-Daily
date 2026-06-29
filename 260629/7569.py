# BFS: 3차원 토마토 익히기
# 익은 토마토에서 동시에 BFS 확산, 최소 일수 계산
# 상하좌우 + 위아래(층) 방향 총 6방향
import sys
from collections import deque
input = sys.stdin.readline

def main():
    M, N, H = map(int, input().split())
    box = []
    queue = deque()
    total = M * N * H
    ripe = 0
    
    for h in range(H):
        layer = []
        for n in range(N):
            row = list(map(int, input().split()))
            for m in range(M):
                if row[m] == 1:
                    queue.append((h, n, m, 0))
                    ripe += 1
                elif row[m] == -1:
                    ripe += 1  # 빈칸도 카운트에서 제외
            layer.append(row)
        box.append(layer)
    
    # 6방향: 층, 행, 열
    dz = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dx = [0, 0, 0, 0, -1, 1]
    
    ans = 0
    while queue:
        z, y, x, day = queue.popleft()
        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and box[nz][ny][nx] == 0:
                box[nz][ny][nx] = 1
                ripe += 1
                ans = day + 1
                queue.append((nz, ny, nx, day + 1))
    
    if ripe == total:
        print(ans)
    else:
        print(-1)

main()
