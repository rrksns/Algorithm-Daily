# 벨만-포드 알고리즘으로 음수 사이클 탐지
# 웜홀(음수 간선)이 있는 그래프에서 과거로 돌아갈 수 있는지 판단
# N번 relaxation 시 여전히 거리가 줄면 음수 사이클 존재

import sys
input = sys.stdin.readline

def bellman_ford(n, edges):
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[1] = 0
    for i in range(n):
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if i == n - 1:
                    return True  # 음수 사이클
    return False

def solve():
    TC = int(input())
    for _ in range(TC):
        N, M, W = map(int, input().split())
        edges = []
        for _ in range(M):
            S, E, T = map(int, input().split())
            edges.append((S, E, T))
            edges.append((E, S, T))
        for _ in range(W):
            S, E, T = map(int, input().split())
            edges.append((S, E, -T))
        # 모든 노드에서 시작 가능하도록 가상 노드 0 추가
        for i in range(1, N + 1):
            edges.append((0, i, 0))
        if bellman_ford(N, edges):
            print("YES")
        else:
            print("NO")

solve()
