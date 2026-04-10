import sys

input = sys.stdin.readline

n = int(input())
graph = []  # 입력받을 그래프를 담을 리스트 선언
result = []  # 결과를 담을 리스트 선언
visited = [[False] * n for _ in range(n)]
cnt = 0

for _ in range(n):
    graph.append(list(map(int, input().strip())))

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

# print(graph)


def dfs(sy, sx):
    global cnt
    visited[sy][sx] = True
    cnt += 1

    for i in range(4):
        ny = sy + dy[i]
        nx = sx + dx[i]
        if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
            if graph[ny][nx] == 1:
                dfs(ny, nx)


for y in range(n):
    for x in range(n):
        if graph[y][x] == 1 and not visited[y][x]:
            cnt = 0
            dfs(y, x)
            result.append(cnt)

result.sort()
print(len(result))
print(*result, sep="\n")


# import sys
# input = sys.stdin.readline

# # 지도 크기 입력
# n = int(input())

# # 지도 입력 (각 줄을 문자 리스트로 저장)
# graph = [list(map(int, input().strip())) for _ in range(n)]
# visited = [[False] * n for _ in range(n)]
# print(graph)

# # 상하좌우 방향 벡터
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]


# def dfs(x, y):
#     """현재 위치에서 DFS 탐색 후 연결된 집의 수 반환"""
#     global count
#     visited[x][y] = True
#     count += 1  # 현재 집 포함

#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         # 범위 안이고, 집이 있고, 아직 방문하지 않은 경우
#         if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and not visited[nx][ny]:
#             dfs(nx, ny)


# result = []  # 각 단지의 집 수 저장

# for i in range(n):
#     for j in range(n):
#         # 집이 있고 아직 방문하지 않은 경우 → 새 단지 발견
#         if graph[i][j] == 1 and not visited[i][j]:
#             count = 0
#             dfs(i, j)
#             result.append(count)

# # 단지 수 출력
# print(len(result))

# # 각 단지 집 수를 오름차순으로 출력
# result.sort()
# for size in result:
#     print(size)
