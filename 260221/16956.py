import sys
input = sys.stdin.readline

R, C = map(int, input().split())
grid = []
for _ in range(R):
    grid.append(list(input().strip()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 늑대와 양이 이미 인접해 있으면 울타리 설치 불가
possible = True
for i in range(R):
    for j in range(C):
        if grid[i][j] == 'W':
            for k in range(4):
                ni, nj = i + dx[k], j + dy[k]
                if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] == 'S':
                    possible = False

if not possible:
    print(0)
else:
    # 모든 빈 칸에 울타리 설치
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '.':
                grid[i][j] = 'D'
    print(1)
    for row in grid:
        print(''.join(row))