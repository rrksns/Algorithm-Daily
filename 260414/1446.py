import sys, heapq

n, d = map(int, sys.stdin.readline().split())
inf = float("inf")

graph = [[] for _ in range(d + 1)]
dist = [inf] * (d + 1)

for i in range(d):
    graph[i].append((i + 1, 1))

for _ in range(n):
    start, dest, length = map(int, sys.stdin.readline().split())
    if dest <= d:
        graph[start].append((dest, length))

q = []
heapq.heappush(q, (0, 0))
dist[0] = 0

while q:
    w1, u = heapq.heappop(q)

    for v, w2 in graph[u]:
        cost = dist[u] + w2
        if dist[v] > cost:
            dist[v] = cost
            heapq.heappush(q, (cost, v))
print(dist[d])


# import sys
# input = sys.stdin.readline

# N, D = map(int, input().split())

# # 지름길 목록 읽기
# shortcuts = []
# for _ in range(N):
#     s, e, w = map(int, input().split())
#     # 실제로 이득이 있는 지름길만 사용 (길이가 구간보다 짧아야 함)
#     if w < e - s:
#         shortcuts.append((s, e, w))

# # dp[i] = 위치 i까지 오는 최소 거리
# dp = list(range(D + 1))  # 기본: dp[i] = i (1씩 이동)

# for i in range(1, D + 1):
#     # 일반 이동: 이전 위치에서 1 전진
#     dp[i] = min(dp[i], dp[i - 1] + 1)

#     # 지름길 적용: 도착점이 i인 지름길 확인
#     for s, e, w in shortcuts:
#         if e == i:
#             dp[i] = min(dp[i], dp[s] + w)

# print(dp[D])
