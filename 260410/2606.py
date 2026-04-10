import sys

input = sys.stdin.readline

n = int(input())
e = int(input())

cnt = 0
visited = [False] * (n + 1)  # visited 형식에 유의
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort()


def dfs(sv):
    global cnt
    visited[sv] = True

    for i in graph[sv]:
        if visited[i] == False:
            cnt += 1  # 시작점을 빼고 합산한다.
            dfs(i)


dfs(1)
print(cnt)
