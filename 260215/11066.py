import sys
input = sys.stdin.readline

def solve():
    K = int(input())
    files = list(map(int, input().split()))

    # 누적합 (prefix sum) 계산
    prefix = [0] * (K + 1)
    for i in range(K):
        prefix[i + 1] = prefix[i] + files[i]

    # dp[i][j] = i번째부터 j번째 파일까지 합치는 최소 비용
    # 초기값: dp[i][i] = 0 (파일 하나는 합칠 필요 없음)
    INF = float('inf')
    dp = [[0] * K for _ in range(K)]

    # 구간 길이(gap)를 1부터 K-1까지 늘려가며 계산
    for gap in range(1, K):
        for i in range(K - gap):
            j = i + gap
            dp[i][j] = INF
            # 구간 [i, j]의 파일 크기 합
            total = prefix[j + 1] - prefix[i]
            # 분할점 k: [i..k] + [k+1..j]
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + total
                if cost < dp[i][j]:
                    dp[i][j] = cost

    print(dp[0][K - 1])

T = int(input())
for _ in range(T):
    solve()