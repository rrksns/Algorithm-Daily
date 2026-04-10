from collections import deque
import sys

input = sys.stdin.readline

n, m, v = map(int, input().split())  # n,m,v입력

g = [
    [] for _ in range(n + 1)
]  # 정점은 n개이나, 인덱스 숫자번호를 맞추기 위해 0번을 만들어 1부터 시작하도록 만듦

# print("넣을 빈 리스트 : ", g)

for _ in range(m):
    a, b = map(int, input().split())  # 간선
    g[a].append(b)
    g[b].append(a)  # 간선이 양방향 이니까


for i in g:
    i.sort()  # 탐색 순서 정렬

# print("리스트 차례대로 정리 : ", g)


def dfs(v):  # dfs함수

    print(v, end=" ")
    visited[v] = True  # dfs에 들어온 정점은  방문처리
    for i in g[v]:  # 그 정점에 연결 된 간선들 확인
        if visited[i] == False:  # 방문 안 했던 정점이면 또 dfs해서 탐색
            dfs(i)


def bfs(v):
    que = deque()
    que.append(v)
    visited[v] = True  # ✅ 시작 노드는 넣을 때 바로 체크

    while que:
        v = que.popleft()
        print(v, end=" ")
        for i in g[v]:
            if not visited[i]:
                visited[i] = True  # ✅ 큐에 넣는 시점에 방문 체크
                que.append(i)


visited = [False] * (n + 1)  # 방문 확인 배열
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)
