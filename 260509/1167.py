import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

# 트리의 지름 - BFS/DFS 두 번
# 1) 임의 노드(1)에서 가장 먼 노드 u를 찾는다
# 2) u에서 가장 먼 노드 v를 찾는다
# 3) u~v 거리가 트리의 지름

from collections import deque

def bfs(start, graph, n):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])
    far_node, max_dist = start, 0
    while q:
        node = q.popleft()
        for nxt, w in graph[node]:
            if dist[nxt] == -1:
                dist[nxt] = dist[node] + w
                if dist[nxt] > max_dist:
                    max_dist = dist[nxt]
                    far_node = nxt
                q.append(nxt)
    return far_node, max_dist

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n):
    data = list(map(int, input().split()))
    u = data[0]
    i = 1
    while data[i] != -1:
        v, w = data[i], data[i+1]
        graph[u].append((v, w))
        graph[v].append((u, w))
        i += 2

u, _ = bfs(1, graph, n)
_, diameter = bfs(u, graph, n)
print(diameter)
