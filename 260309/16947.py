import sys
from collections import deque

input = sys.stdin.readline

def solve():
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    degree = [0] * (N + 1)

    for _ in range(N):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        degree[a] += 1
        degree[b] += 1

    # Step 1: 리프 노드를 반복 제거해 사이클 노드 찾기
    # degree == 1인 노드는 지선(트리 가지)이므로 제거
    removed = [False] * (N + 1)
    queue = deque()
    for i in range(1, N + 1):
        if degree[i] == 1:
            queue.append(i)

    while queue:
        node = queue.popleft()
        removed[node] = True
        for nxt in graph[node]:
            if not removed[nxt]:
                degree[nxt] -= 1
                if degree[nxt] == 1:
                    queue.append(nxt)

    # 제거되지 않은 노드 = 순환선 노드
    is_cycle = [not removed[i] for i in range(N + 1)]

    # Step 2: 순환선 노드들을 시작점으로 BFS → 각 역까지 최단 거리
    dist = [-1] * (N + 1)
    bfs_queue = deque()
    for i in range(1, N + 1):
        if is_cycle[i]:
            dist[i] = 0
            bfs_queue.append(i)

    while bfs_queue:
        node = bfs_queue.popleft()
        for nxt in graph[node]:
            if dist[nxt] == -1:
                dist[nxt] = dist[node] + 1
                bfs_queue.append(nxt)

    print(*dist[1:N + 1])

solve()