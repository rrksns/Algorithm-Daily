"""
1.아이디어
 최소 금액을 구하는 그래프 -> 다익스트라
2.시간복잡도
O(E * logV)

3.변수
최소 거리

"""

import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize


def dik(tc, sy, sx):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    start_cost = graph[0][0]
    dist = [[INF] * n for _ in range(n)]
    dist[sy][sx] = start_cost

    heap = []
    heapq.heappush(heap, (start_cost, 0, 0))

    while heap:
        cost, cy, cx = heapq.heappop(heap)
        if cx == n - 1 and cy == n - 1:
            print(f"Problem {tc} : {dist[cy][cx]}")
            break

        if dist[cy][cx] < cost:
            continue

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                new_cost = cost + graph[ny][nx]
                if new_cost < dist[ny][nx]:
                    dist[ny][nx] = new_cost
                    heapq.heappush(heap, (new_cost, ny, nx))


tc = 0
while True:
    n = int(input())
    if n != 0:
        tc += 1
        graph = [list(map(int, input().split())) for _ in range(n)]
        dik(tc, 0, 0)
    else:
        break
