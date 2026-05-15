# 케빈 베이컨의 6단계 법칙 - BFS
# 각 노드에서 BFS를 실행해 모든 노드까지의 최단 거리 합(케빈 베이컨 수)을 구한다.
# 케빈 베이컨 수가 가장 작은 사람의 번호를 출력한다.
# N명 모두에 대해 BFS → O(N*(N+M))

import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, graph, N):
    dist = [-1] * (N + 1)
    dist[start] = 0
    q = deque([start])
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)
    return sum(d for d in dist[1:] if d != -1)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

min_bacon = float('inf')
answer = 1
for i in range(1, N + 1):
    bacon = bfs(i, graph, N)
    if bacon < min_bacon:
        min_bacon = bacon
        answer = i

print(answer)
