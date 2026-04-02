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
        # if dist[ev] != ew:
        #     continue
        if ew > dist[ev]:
            continue
        for nw, nv in graph[ev]:
            new_cost = ew + nw
            if new_cost < dist[nv]:
                dist[nv] = new_cost
                heapq.heappush(heap, [new_cost, nv])

    return dist


V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([w, v])

dist = dik(K, graph, V)

for i in range(1, V + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
