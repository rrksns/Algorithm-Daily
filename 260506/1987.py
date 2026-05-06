# 알파벳 : 백트레킹 bfs

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    global result

    q = set()
    q.add((x, y, arr[x][y]))

    while q:
        x, y, step = q.pop()
        result = max(result, len(step))  # 가장 긴 거리를 저장

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 이동할수 있는 위치이고, 새로운 알파벳일경우
            if 0 <= nx and nx < r and 0 <= ny and ny < c and arr[nx][ny] not in step:
                q.add((nx, ny, step + arr[nx][ny]))


# 입력값
r, c = map(int, input().split())
arr = []
for _ in range(r):
    arr.append(input())

result = 0
bfs(0, 0)
print(result)
