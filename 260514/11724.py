# 연결 요소의 개수 - BFS/DFS로 그래프의 연결 요소 개수 찾기
# 방문하지 않은 노드에서 BFS를 시작할 때마다 연결 요소 +1
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (N + 1)
    count = 0
    for node in range(1, N + 1):
        if not visited[node]:
            bfs(node, graph, visited)
            count += 1

    print(count)

main()
