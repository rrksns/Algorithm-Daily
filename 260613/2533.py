# 사회망 서비스 (SNS) - Tree DP (최소 정점 커버)
# 아이디어: 트리에서 모든 간선이 얼리어답터로 커버되는 최솟값
# dp[v][0] = v가 얼리어답터 아닐 때 → 모든 자식은 반드시 얼리어답터
# dp[v][1] = v가 얼리어답터일 때 → 자식은 선택 자유 (min 선택)

import sys
from sys import setrecursionlimit
input = sys.stdin.readline
setrecursionlimit(1000000)

def solve():
    n = int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    dp = [[0, 1] for _ in range(n+1)]  # dp[v][0]=비선택, dp[v][1]=선택

    # 반복적 DFS (재귀 깊이 제한 우회)
    visited = [False] * (n+1)
    stack = [(1, 0, False)]
    parent = [0] * (n+1)
    order = []

    while stack:
        v, p, processed = stack.pop()
        if processed:
            order.append(v)
            continue
        if visited[v]:
            continue
        visited[v] = True
        parent[v] = p
        stack.append((v, p, True))
        for u in graph[v]:
            if not visited[u]:
                stack.append((u, v, False))

    for v in order:
        for u in graph[v]:
            if u == parent[v]:
                continue
            dp[v][0] += dp[u][1]          # v 비선택 → u는 반드시 선택
            dp[v][1] += min(dp[u][0], dp[u][1])  # v 선택 → u는 최솟값

    print(min(dp[1][0], dp[1][1]))

solve()
