import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(start, graph, V):
    dist = [INF] * (V + 1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        ew, ev = heapq.heappop(heap)
        if dist[ev] != ew:
            continue
        for nw, nv in graph[ev]:
            if dist[nv] > nw + ew:
                dist[nv] = nw + ew
                heapq.heappush(heap, (dist[nv], nv))

    return dist  # ✅ dist 배열 반환


N, M, X = map(int, input().split())  # ✅ X = 목적지

graph = [[] for _ in range(N + 1)]  # 원래 방향
rev_graph = [[] for _ in range(N + 1)]  # ✅ 역방향 그래프

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    rev_graph[v].append((w, u))  # ✅ 역방향 간선 추가

# X → 각 학생 (원래 그래프, 파티 끝나고 돌아오는 경로)
dist_from_X = dijkstra(X, graph, N)

# 각 학생 → X (역방향 그래프에서 X 출발 = 원래 방향에서 X 도착)
dist_to_X = dijkstra(X, rev_graph, N)

# ✅ 각 학생의 왕복 시간 = 가는 거리 + 오는 거리
answer = max(dist_to_X[i] + dist_from_X[i] for i in range(1, N + 1))
print(answer)
