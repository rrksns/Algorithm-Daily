# 트리의 부모 찾기 - BFS
# 아이디어: 루트(1번)에서 BFS 탐색하며 각 노드의 부모 기록
# 방문 처리로 역방향 탐색 방지
import sys
from collections import deque
input = sys.stdin.readline

def solve():
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    parent = [0] * (N + 1)
    visited = [False] * (N + 1)
    queue = deque([1])
    visited[1] = True

    while queue:
        node = queue.popleft()
        for nei in graph[node]:
            if not visited[nei]:
                visited[nei] = True
                parent[nei] = node
                queue.append(nei)

    for i in range(2, N + 1):
        print(parent[i])

solve()
