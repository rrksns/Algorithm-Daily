import sys
input = sys.stdin.readline

# 체스판 다시 칠하기 - 브루트포스
# 8x8 체스판을 잘라낼 때 다시 칠해야 하는 칸의 최솟값
# 체스판 패턴: W시작 or B시작 두 가지 → 각각 비교
# 칸(r,c)가 올바른 색: (r+c)%2 == 0 이면 첫칸과 같은 색

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

ans = 64  # 최대 다시 칠하는 수
for r in range(n - 7):
    for c in range(m - 7):
        # W로 시작하는 경우
        cnt_w = 0
        for i in range(8):
            for j in range(8):
                expected = 'W' if (i + j) % 2 == 0 else 'B'
                if board[r+i][c+j] != expected:
                    cnt_w += 1
        ans = min(ans, cnt_w, 64 - cnt_w)  # B 시작 = 64 - cnt_w

print(ans)
