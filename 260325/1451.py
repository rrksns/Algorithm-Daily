import sys

# 입력을 빠르게 받기 위한 설정
input = sys.stdin.readline


def solve():
    # 1. N(세로), M(가로) 입력
    line = input().split()
    if not line:
        return
    n, m = map(int, line)

    # 2. 직사각형 숫자판 입력 (문자열로 들어오므로 하나씩 숫자로 변환)
    board = [list(map(int, list(input().strip()))) for _ in range(n)]

    print("board::", board)

    # 3. 2차원 누적합 배열 (S[i][j]는 (0,0)부터 (i-1, j-1)까지의 합)
    s = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + board[i - 1][j - 1]

    # 구역의 합을 구하는 헬퍼 함수 (코드 가독성을 위해)
    def get_sum(x1, y1, x2, y2):
        return s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1]

    ans = 0

    # 4. 6가지 케이스 탐색 (경계선 i, j를 나누는 지점으로 사용)

    # Case 1: 세로로 3등분 (Vertical lines)
    for i in range(1, m - 1):
        for j in range(i + 1, m):
            ans = max(
                ans,
                get_sum(1, 1, n, i) * get_sum(1, i + 1, n, j) * get_sum(1, j + 1, n, m),
            )

    # Case 2: 가로로 3등분 (Horizontal lines)
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            ans = max(
                ans,
                get_sum(1, 1, i, m) * get_sum(i + 1, 1, j, m) * get_sum(j + 1, 1, n, m),
            )

    # Case 3: 왼쪽 1개 | 오른쪽 위아래 2개
    for i in range(1, m):
        for j in range(1, n):
            ans = max(
                ans,
                get_sum(1, 1, n, i)
                * get_sum(1, i + 1, j, m)
                * get_sum(j + 1, i + 1, n, m),
            )

    # Case 4: 왼쪽 위아래 2개 | 오른쪽 1개
    for i in range(1, m):
        for j in range(1, n):
            ans = max(
                ans,
                get_sum(1, 1, j, i) * get_sum(j + 1, 1, n, i) * get_sum(1, i + 1, n, m),
            )

    # Case 5: 위쪽 1개 / 아래쪽 좌우 2개
    for i in range(1, n):
        for j in range(1, m):
            ans = max(
                ans,
                get_sum(1, 1, i, m)
                * get_sum(i + 1, 1, n, j)
                * get_sum(i + 1, j + 1, n, m),
            )

    # Case 6: 위쪽 좌우 2개 / 아래쪽 1개
    for i in range(1, n):
        for j in range(1, m):
            ans = max(
                ans,
                get_sum(1, 1, i, j) * get_sum(1, j + 1, i, m) * get_sum(i + 1, 1, n, m),
            )

    print(ans)


solve()
