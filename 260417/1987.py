"""
#아이디어
    (0,0) 부터 시작해서 방문여부를 체크
    재귀적으로 호출
#시간복잡도
 O(N!)
#자료구조
    방문여부체크 visited
    상하좌우이동 dx,dy
    포함된여부 set()
    max_cnt
"""

import sys

input = sys.stdin.readline
R, C = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(R)]
alpha = set()

cnt = 0
max_cnt = 0
# print("b", board[0][0])
# print("c", chk)


def dfs(y, x, cnt):
    global max_cnt
    max_cnt = max(cnt, max_cnt)

    # 반복
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < R and 0 <= nx < C:
            if board[ny][nx] not in alpha:
                alpha.add(board[ny][nx])
                dfs(ny, nx, cnt + 1)
                alpha.remove(board[ny][nx])


alpha.add(board[0][0])
dfs(0, 0, 1)

print(max_cnt)
