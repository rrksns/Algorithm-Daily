import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize


def dik(start, graph, n):
    dist = [INF] * (n + 1)
    dist[start] = 0
    heap = [[0, start]]

    while heap:
        ew, ev = heapq.heappop(heap)
        if dist[ev] < ew:
            continue
        for nw, nv in graph[ev]:
            new_cost = nw + ew
            if new_cost < dist[nv]:
                dist[nv] = new_cost
                heapq.heappush(heap, [new_cost, nv])
    return dist


N, M, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
rev_graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append([w, v])
    rev_graph[v].append([w, u])

dist_to_x = dik(X, graph, N)
dist_from_x = dik(X, rev_graph, N)

ans = max(dist_to_x[i] + dist_from_x[i] for i in range(1, N + 1))
print(ans)
