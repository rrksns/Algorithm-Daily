import sys
input = sys.stdin.readline

MOD = 1_000_000_007

def solve():
    P, N, K = map(int, input().split())

    # dp[i][j] = 길이 i인 플레이리스트에서 j가지 서로 다른 노래를 사용한 경우의 수
    # 점화식:
    # 새 노래를 추가하는 경우: dp[i-1][j-1] * (N - (j-1))
    # 이미 나온 노래를 추가하는 경우: dp[i-1][j] * max(0, j - K)

    dp = [[0] * (N + 1) for _ in range(P + 1)]
    dp[0][0] = 1

    for i in range(1, P + 1):
        for j in range(1, N + 1):
            # 새 노래 추가
            dp[i][j] = dp[i-1][j-1] * (N - (j - 1)) % MOD
            # 이미 나온 노래 반복 (단 K개 이상 다른 노래 재생됐어야 함)
            if j > K:
                dp[i][j] = (dp[i][j] + dp[i-1][j] * (j - K)) % MOD

    print(dp[P][N])

solve()