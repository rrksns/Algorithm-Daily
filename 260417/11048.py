# import sys

# input = sys.stdin.readline

# R, C = map(int, input().split())
# # visited = [[False] * C for _ in range(R)]
# # cc = list(map(int, input().replace(" ", "").strip()))

# board = [list(map(int, input().split())) for _ in range(R)]

# max_cnt = 0


# def dfs(y, x, cnt):
#     global max_cnt

#     if y == R - 1 and x == C - 1:
#         max_cnt = max(max_cnt, cnt)
#         return

#     dy = [0, 1, 1]
#     dx = [1, 0, 1]

#     for i in range(3):
#         ny, nx = y + dy[i], x + dx[i]

#         if 0 <= ny < R and 0 <= nx < C:
#             dfs(ny, nx, cnt + board[ny][nx])


# cnt = 0

# dfs(0, 0, board[0][0])
# print(max_cnt)


import sys

# 재귀 깊이 제한 해제 (DFS 필수)
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

R, C = map(int, input().split())

# 1. 입력 버그 수정: split() 사용 (숫자가 10 이상일 수도 있으니까요!)
board = [list(map(int, input().split())) for _ in range(R)]

max_cnt = 0


def dfs(y, x, cnt):
    global max_cnt

    # 2. 종료 조건 수정: (R-1, C-1)에 도착했을 때
    if y == R - 1 and x == C - 1:
        max_cnt = max(max_cnt, cnt)
        return

    # 이동 방향: 오른쪽, 아래, 대각선
    dy = [0, 1, 1]
    dx = [1, 0, 1]

    for i in range(3):
        ny, nx = y + dy[i], x + dx[i]

        # 3. 격자 범위 안에 있는지 확인
        if 0 <= ny < R and 0 <= nx < C:
            # 4. 재귀 호출: 다음 좌표(ny, nx)를 전달해야 함!
            # 현재까지의 사탕(cnt) + 다음 칸의 사탕(board[ny][nx])
            dfs(ny, nx, cnt + board[ny][nx])


# 5. 시작점 사탕을 포함해서 DFS 시작
dfs(0, 0, board[0][0])

print(max_cnt)
