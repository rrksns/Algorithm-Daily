# **BFS + 인접 리스트 + 오름차순 정렬**

# 핵심 포인트:
# 1. 인접 리스트로 그래프를 표현 (인접 행렬은 N=100,000이면 O(N²) → 메모리/시간 초과)
# 2. 각 정점의 인접 리스트를 미리 오름차순 정렬
# 3. BFS 진행하며 방문 순서를 배열에 기록

# ---

# ## 시간/공간 복잡도

# | 항목 | 복잡도 |
# |------|--------|
# | 정렬 | O(M log M) |
# | BFS | O(N + M) |
# | 전체 | **O(M log M)** |

# - N ≤ 100,000 / M ≤ 200,000이므로 충분히 통과

# ---

# ## 풀이 과정

# ```
# 초기 상태 (R=1):
#   visited = [0, 0, 0, 0, 0, 0]  (인덱스 0 미사용)
#   graph[1] = [2, 4]  (정렬됨)
#   graph[2] = [1, 3, 4]
#   graph[3] = [2, 4]
#   graph[4] = [1, 2, 3]

# BFS 시작:
#   1 방문 → visited[1]=1, queue=[1]
#   dequeue(1) → 이웃 [2, 4] 처리
#     2 미방문 → visited[2]=2, queue=[2]
#     4 미방문 → visited[4]=3, queue=[2, 4]
#   dequeue(2) → 이웃 [1, 3, 4] 처리
#     1 이미 방문
#     3 미방문 → visited[3]=4, queue=[4, 3]
#     4 이미 방문
#   dequeue(4) → 이웃 [1, 2, 3] 처리
#     모두 방문됨
#   dequeue(3) → 이웃 [2, 4] 처리
#     모두 방문됨
#   queue 비어있음 → 종료

# 결과: [1, 2, 4, 3, 0]
# ```

# ---

# ## 코드 설명

# ```python
import sys
from collections import deque

input = sys.stdin.readline  # 빠른 입력 (N,M이 크므로 필수)


def bfs(graph, start, n):
    visited = [0] * (n + 1)
    order = 1

    visited[start] = order  # 시작 정점 1번째 방문
    queue = deque([start])

    while queue:
        u = queue.popleft()
        for v in graph[u]:  # 오름차순 정렬된 인접 리스트 순회
            if visited[v] == 0:
                order += 1
                visited[v] = order
                queue.append(v)

    return visited


N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # 무방향 그래프

for i in range(1, N + 1):
    graph[i].sort()  # 오름차순 정렬 (핵심!)

visited = bfs(graph, R, N)
print("\n".join(map(str, visited[1:])))
