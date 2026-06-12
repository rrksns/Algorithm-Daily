# 줄 세우기: 일부 학생 간 앞뒤 관계가 주어졌을 때 전체 줄 세우기
# 위상 정렬 (Kahn's algorithm) - 진입차수 0인 노드부터 BFS
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque([i for i in range(1, N+1) if indegree[i] == 0])
result = []
while q:
    node = q.popleft()
    result.append(node)
    for nxt in graph[node]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

print(*result)
