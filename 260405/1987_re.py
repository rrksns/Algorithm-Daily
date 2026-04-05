dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    global result

    q = set()
    q.add((x, y, arr[x][y]))

    while q:
        x, y, step = q.pop()
        result = max(result, len(step))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] not in step:
                q.add((nx, ny, step + arr[nx][ny]))


r, c = map(int, input().split())
arr = []
for _ in range(r):
    arr.append(input())

result = 0
bfs(0, 0)
print(result)
