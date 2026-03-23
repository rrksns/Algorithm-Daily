import sys
from collections import deque

sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M, V = map(int, input().split())

# 인접 리스트로 그래프 구성
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 번호가 작은 정점부터 방문하기 위해 정렬
for i in range(1, N + 1):
    graph[i].sort()


def dfs(v, visited):
    visited[v] = True
    print(v, end=' ')
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v, visited)


def bfs(start):
    visited = [False] * (N + 1)
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)


# DFS 수행
visited_dfs = [False] * (N + 1)
dfs(V, visited_dfs)
print()

# BFS 수행
bfs(V)