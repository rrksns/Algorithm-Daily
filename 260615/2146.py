# 백준 2146 - 다리 만들기
# 핵심 아이디어: BFS 2단계
# 1단계: BFS로 각 섬에 고유 번호(island_id) 부여
# 2단계: 각 섬에서 multi-source BFS (섬의 모든 칸에서 동시 출발)
#        → 바다를 건너다가 다른 섬 육지에 닿을 때 건넌 바다 칸 수 = 다리 길이
#        → 모든 섬 쌍 중 최솟값이 정답
# 시간복잡도: O(K * N^2), K=섬 개수

import sys
from collections import deque
input = sys.stdin.readline

def solve():
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # 1단계: 섬 번호 부여
    label = [[-1] * N for _ in range(N)]
    island_id = 0
    islands = []  # islands[i] = 섬 i의 모든 칸 좌표

    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1 and label[i][j] == -1:
                q = deque([(i, j)])
                label[i][j] = island_id
                cells = [(i, j)]
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 1 and label[nx][ny] == -1:
                            label[nx][ny] = island_id
                            q.append((nx, ny))
                            cells.append((nx, ny))
                islands.append(cells)
                island_id += 1

    # 2단계: 각 섬에서 multi-source BFS
    ans = float('inf')

    for iid, cells in enumerate(islands):
        dist = [[-1] * N for _ in range(N)]
        q = deque()
        # 섬의 모든 육지 칸을 거리 0으로 시작
        for x, y in cells:
            dist[x][y] = 0
            q.append((x, y))

        while q:
            x, y = q.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if dist[nx][ny] != -1:
                    continue
                if grid[nx][ny] == 1:
                    # 다른 섬 육지에 도달 → 현재 위치까지 건넌 바다 칸 수 = 다리 길이
                    if label[nx][ny] != iid:
                        ans = min(ans, dist[x][y])
                    # 같은 섬은 이미 dist=0으로 초기화되어 있으므로 여기 오지 않음
                else:
                    # 바다 칸: 거리 +1
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    print(ans)

solve()
