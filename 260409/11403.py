import sys

input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

# 플로이드-워셜: graph[i][j] = i에서 j로 가는 경로 존재 여부
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for row in graph:
    print(*row)
