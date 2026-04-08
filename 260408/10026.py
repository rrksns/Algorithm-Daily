from collections import deque


def BFS(y, x):
    q.append((y, x))
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    visited[y][x] = 1
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            # 인덱스 범위 안에 있으면서, 같은 색이면서, 방문 안한 경우
            if (
                0 <= ny < N
                and 0 <= nx < N
                and a[ny][nx] == a[y][x]
                and not visited[ny][nx]
            ):
                visited[ny][nx] = 1  # 방문체크 후 큐에 넣음
                q.append((ny, nx))


N = int(input())
a = [list(input()) for _ in range(N)]
q = deque()

# 적록색약 아닌 경우
visited = [[0] * N for _ in range(N)]
cnt1 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:  # 아직 방문 안한 경우만 체킹
            BFS(i, j)
            cnt1 += 1

# 적록색약인 경우
for i in range(N):
    for j in range(N):
        if a[i][j] == "G":
            a[i][j] = "R"

visited = [[0] * N for _ in range(N)]
cnt2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i, j)
            cnt2 += 1

print(cnt1, cnt2)
