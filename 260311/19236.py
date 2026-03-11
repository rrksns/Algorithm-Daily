import copy

# 방향: 1~8 (반시계 순서)
# 1:↑  2:↖  3:←  4:↙  5:↓  6:↘  7:→  8:↗
DR = [0, -1, -1, 0, 1, 1, 1, 0, -1]
DC = [0, 0, -1, -1, -1, 0, 1, 1, 1]

# board[r][c] = [물고기번호, 방향]  (0이면 빈칸, -1이면 상어)
# fish_pos[번호] = (r, c)  (None이면 먹힘)

def move_fishes(board, shark_r, shark_c):
    """물고기를 번호 순서대로 이동"""
    # 물고기 위치 맵 구성
    for num in range(1, 17):
        # 현재 board에서 num 위치 찾기
        fr, fc = -1, -1
        for r in range(4):
            for c in range(4):
                if board[r][c][0] == num:
                    fr, fc = r, c
                    break
            if fr != -1:
                break
        if fr == -1:
            continue  # 먹힌 물고기

        d = board[fr][fc][1]
        # 45도씩 반시계 회전하며 이동 가능한 방향 탐색
        for i in range(8):
            nd = (d - 1 + i) % 8 + 1  # 반시계 회전
            nr, nc = fr + DR[nd], fc + DC[nd]
            # 이동 불가: 경계 밖 or 상어 위치
            if not (0 <= nr < 4 and 0 <= nc < 4):
                continue
            if nr == shark_r and nc == shark_c:
                continue
            # 이동 가능: 방향 갱신 후 위치 교환
            board[fr][fc][1] = nd
            board[fr][fc], board[nr][nc] = board[nr][nc], board[fr][fc]
            break


def dfs(board, shark_r, shark_c, shark_d, score):
    global answer
    answer = max(answer, score)

    # 물고기 이동
    move_fishes(board, shark_r, shark_c)

    # 상어 이동: 방향으로 직선 이동, 물고기 있는 칸만 선택 가능
    nr, nc = shark_r + DR[shark_d], shark_c + DC[shark_d]
    while 0 <= nr < 4 and 0 <= nc < 4:
        if board[nr][nc][0] > 0:  # 물고기가 있는 칸
            # 해당 칸으로 이동하는 경우 탐색
            new_board = copy.deepcopy(board)
            eaten_num = new_board[nr][nc][0]
            new_d = new_board[nr][nc][1]
            new_board[nr][nc] = [0, 0]   # 빈칸으로
            dfs(new_board, nr, nc, new_d, score + eaten_num)
        nr += DR[shark_d]
        nc += DC[shark_d]


# 입력
board = []
for i in range(4):
    row_data = list(map(int, input().split()))
    row = []
    for j in range(4):
        num = row_data[j * 2]
        d = row_data[j * 2 + 1]
        row.append([num, d])
    board.append(row)

answer = 0

# 상어가 (0,0) 물고기 먹고 시작
start_num = board[0][0][0]
start_d = board[0][0][1]
board[0][0] = [0, 0]

dfs(board, 0, 0, start_d, start_num)

print(answer)