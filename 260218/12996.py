import sys
input = sys.stdin.readline

def solve():
    S, a, b, c = map(int, input().split())
    MOD = 1_000_000_007

    # dp[j][k][l]: 지금까지 멤버1이 j곡, 멤버2가 k곡, 멤버3가 l곡 참여한 경우의 수
    # 각 곡을 배정할 때 (x, y, z) ∈ {0,1}^3 \ {(0,0,0)} 7가지 중 선택
    dp = [[[0] * (c + 1) for _ in range(b + 1)] for _ in range(a + 1)]
    dp[0][0][0] = 1

    for _ in range(S):
        ndp = [[[0] * (c + 1) for _ in range(b + 1)] for _ in range(a + 1)]
        for j in range(a + 1):
            for k in range(b + 1):
                for l in range(c + 1):
                    if dp[j][k][l] == 0:
                        continue
                    val = dp[j][k][l]
                    # 이번 곡에 각 멤버가 참여(1) / 불참(0)
                    for x in range(2):
                        for y in range(2):
                            for z in range(2):
                                if x == 0 and y == 0 and z == 0:
                                    continue  # 최소 1명은 참여해야 함
                                nj, nk, nl = j + x, k + y, l + z
                                if nj <= a and nk <= b and nl <= c:
                                    ndp[nj][nk][nl] = (ndp[nj][nk][nl] + val) % MOD
        dp = ndp

    print(dp[a][b][c])

solve()