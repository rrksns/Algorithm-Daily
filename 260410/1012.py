"""
T: test case
.가로 세로 : M , N
배추위치개수 K
위치 x,y

"""

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)


# 입력부
tc = int(input())

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


# dfs
def dfs(sy, sx):
    visited[sy][sx] = True
    for i in range(4):
        ny = sy + dy[i]
        nx = sx + dx[i]
        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            if graph[ny][nx] == 1:
                dfs(ny, nx)


# 출력부
for _ in range(tc):
    cnt = 0
    result = []
    M, N, K = map(int, input().split())
    visited = [[False] * M for _ in range(N)]
    graph = [[0] * M for _ in range(N)]

    for i in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1 and not visited[y][x]:
                dfs(y, x)
                cnt += 1

    print(cnt)
