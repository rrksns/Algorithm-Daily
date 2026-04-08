"""
문제 요약
N×M 크기의 방에서 로봇 청소기가 작동하는 영역의 수를 구하는 시뮬레이션 문제.
입력

N, M (방 크기, 3 ≤ N, M ≤ 50)
로봇 초기 위치 (r, c)와 방향 d (0=북, 1=동, 2=남, 3=서)
N×M 격자 (0=빈칸, 1=벽)

출력: 청소한 칸의 개수

   동작 정리
1. 현재 위치를 청소 (청소 안 된 경우)
2. 현재 방향 기준 왼쪽부터 4방향 순서로 탐색:
   a. 왼쪽에 청소 안 된 빈 칸 → 그 방향으로 회전 후 전진 → step 1로
   b. 왼쪽에 청소할 공간 없음 → 회전만 하고 step 2로
3. 4방향 모두 청소됐거나 벽:
   - 뒤로 한 칸 이동 (방향 유지)
   - 뒤가 벽이면 → 종료


   방향 처리
방향 배열 (0=북, 1=동, 2=남, 3=서):
  dr = [-1, 0, 1, 0]
  dc = [0, 1, 0, -1]

왼쪽 회전: d = (d + 3) % 4
후진 방향: back_d = (d + 2) % 4



"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 방향: 0=북, 1=동, 2=남, 3=서
# 북쪽이 행 감소 방향
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

count = 0

while True:
    # 1. 현재 칸 청소
    if grid[r][c] == 0:
        grid[r][c] = 2  # 청소됨
        count += 1

    # 2. 왼쪽부터 4방향 탐색
    moved = False
    for _ in range(4):
        d = (d + 3) % 4  # 왼쪽으로 회전
        nr, nc = r + dr[d], c + dc[d]
        if grid[nr][nc] == 0:  # 청소 안 된 빈 칸
            r, c = nr, nc
            moved = True
            break

    if moved:
        continue

    # 3. 4방향 모두 청소됐거나 벽: 뒤로 이동 시도
    back_d = (d + 2) % 4
    nr, nc = r + dr[back_d], c + dc[back_d]
    if grid[nr][nc] == 1:  # 뒤가 벽이면 종료
        break
    r, c = nr, nc  # 방향은 유지한 채 후진

print(count)
