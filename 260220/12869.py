from itertools import permutations
from collections import deque

def solve():
    n = int(input())
    hp = list(map(int, input().split()))

    # SCV가 3개 미만이면 0으로 채워 항상 3개로 맞춤
    while len(hp) < 3:
        hp.append(0)

    a, b, c = hp[0], hp[1], hp[2]

    # dp[a][b][c] = 이 상태에서 모든 SCV를 처치하는 최소 공격 횟수
    INF = float('inf')
    dp = [[[INF] * 61 for _ in range(61)] for _ in range(61)]
    dp[a][b][c] = 0

    # BFS로 탐색
    queue = deque()
    queue.append((a, b, c))

    # 9, 3, 1의 모든 순열 (6가지)
    attacks = list(permutations([9, 3, 1]))

    while queue:
        x, y, z = queue.popleft()

        for d1, d2, d3 in attacks:
            # 공격 후 체력 계산 (0 미만은 0으로)
            nx = max(0, x - d1)
            ny = max(0, y - d2)
            nz = max(0, z - d3)

            if dp[nx][ny][nz] == INF:
                dp[nx][ny][nz] = dp[x][y][z] + 1
                if nx == 0 and ny == 0 and nz == 0:
                    print(dp[0][0][0])
                    return
                queue.append((nx, ny, nz))

    print(dp[0][0][0])

solve()