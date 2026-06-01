# 이분 그래프 - Graph / BFS
# 그래프를 두 집합으로 나눌 수 있는지 확인
# BFS로 2-coloring: 인접 노드에 다른 색을 칠하다가 같은 색 충돌 시 NO
# 비연결 그래프 대비 모든 컴포넌트를 탐색

import sys
from collections import deque

input = sys.stdin.readline

def is_bipartite(graph, n):
    color = [-1] * (n + 1)
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        queue = deque([start])
        color[start] = 0
        while queue:
            v = queue.popleft()
            for u in graph[v]:
                if color[u] == -1:
                    color[u] = 1 - color[v]
                    queue.append(u)
                elif color[u] == color[v]:
                    return False
    return True

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    print("YES" if is_bipartite(graph, V) else "NO")
