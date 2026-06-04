# 플로이드-워셜 알고리즘으로 모든 쌍 최단경로 계산
# DP[i][j] = i에서 j로 가는 최소 비용
# 중간 노드 k를 거치는 경우를 모든 쌍에 대해 갱신

import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    m = int(input())
    INF = float('inf')
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dist[i][i] = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        dist[a][b] = min(dist[a][b], c)
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    for i in range(1, n + 1):
        print(*[0 if dist[i][j] == INF else dist[i][j] for j in range(1, n + 1)])

solve()
