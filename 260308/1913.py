import sys
input = sys.stdin.readline

n = int(input())
target = int(input())

# N×N 그리드 초기화
grid = [[0] * n for _ in range(n)]

# 시작점: 정중앙
r, c = n // 2, n // 2
grid[r][c] = 1

# 방향: 위 → 오른쪽 → 아래 → 왼쪽
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

num = 2          # 다음에 채울 숫자
dir_idx = 0      # 현재 방향 인덱스
step = 1         # 현재 방향으로 이동할 칸 수

# 방향 전환 패턴: 1,1,2,2,3,3,4,4,...
# 각 step 크기를 2번 사용한 후 step 증가
while num <= n * n:
    for _ in range(2):  # 같은 step 크기로 두 방향 이동
        for _ in range(step):
            r += dr[dir_idx]
            c += dc[dir_idx]
            grid[r][c] = num
            num += 1
            if num > n * n:
                break
        dir_idx = (dir_idx + 1) % 4
        if num > n * n:
            break
    step += 1

# 그리드 출력 & target 좌표 탐색
tr, tc = 0, 0
result = []
for i in range(n):
    row_vals = []
    for j in range(n):
        row_vals.append(str(grid[i][j]))
        if grid[i][j] == target:
            tr, tc = i + 1, j + 1  # 1-based 좌표
    result.append(' '.join(row_vals))

print('\n'.join(result))
print(tr, tc)