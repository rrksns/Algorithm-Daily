# 특정한 최단 경로 - Dijkstra
# 반드시 두 꼭짓점 v1, v2를 거쳐 1 → N으로 가는 최단 경로
# 경로 후보: 1→v1→v2→N  또는  1→v2→v1→N
# 각 노드에서 Dijkstra 3번 실행 (1, v1, v2 출발)
# INF 초과 시 -1 출력

import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

def dijkstra(start, graph, N):
    dist = [INF] * (N + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

d1 = dijkstra(1, graph, N)
dv1 = dijkstra(v1, graph, N)
dv2 = dijkstra(v2, graph, N)

# 경우 1: 1 → v1 → v2 → N
route1 = d1[v1] + dv1[v2] + dv2[N]
# 경우 2: 1 → v2 → v1 → N
route2 = d1[v2] + dv2[v1] + dv1[N]

ans = min(route1, route2)
print(-1 if ans >= INF else ans)
