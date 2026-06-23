# 사탕 게임 - 브루트포스
# 핵심 아이디어: 인접한 두 칸을 교환한 뒤 행/열의 최대 연속 길이를 구한다.
# N ≤ 50이므로 모든 교환(O(N^2)) × 연속 계산(O(N^2)) = O(N^4) ≈ 6.25M으로 충분.

import sys
input = sys.stdin.readline

def max_streak(board, N):
    best = 1
    for r in range(N):
        cnt = 1
        for c in range(1, N):
            if board[r][c] == board[r][c-1]:
                cnt += 1
                best = max(best, cnt)
            else:
                cnt = 1
    for c in range(N):
        cnt = 1
        for r in range(1, N):
            if board[r][c] == board[r-1][c]:
                cnt += 1
                best = max(best, cnt)
            else:
                cnt = 1
    return best

N = int(input())
board = [list(input().strip()) for _ in range(N)]

ans = 1
# 가로 방향 교환
for r in range(N):
    for c in range(N - 1):
        board[r][c], board[r][c+1] = board[r][c+1], board[r][c]
        ans = max(ans, max_streak(board, N))
        board[r][c], board[r][c+1] = board[r][c+1], board[r][c]

# 세로 방향 교환
for r in range(N - 1):
    for c in range(N):
        board[r][c], board[r+1][c] = board[r+1][c], board[r][c]
        ans = max(ans, max_streak(board, N))
        board[r][c], board[r+1][c] = board[r+1][c], board[r][c]

print(ans)
