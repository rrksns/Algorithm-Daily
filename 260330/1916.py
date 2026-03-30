import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(start_v):
    dist[start_v] = 0

    heap = []

    heapq.heappush(heap, [0, start_v])

    while heap:
        now_dis, now_v = heapq.heappop(heap)

        # 가지치기
        if now_dis > dist[now_v]:
            continue

        for next_v in graph[now_v]:
            cost = next_v[0] + dist[now_v]
            if cost < dist[next_v[1]]:
                dist[next_v[1]] = next_v[0] + dist[now_v]
                heapq.heappush(heap, [cost, next_v[1]])


N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    v1, v2, c = map(int, input().split())
    graph[v1].append([c, v2])

start, end = map(int, input().split())

dist = [INF] * (N + 1)

dijkstra(start)
