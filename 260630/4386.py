# MST: 별자리 만들기
# 모든 별을 연결하는 최소 스패닝 트리
# 완전 그래프(별들 간 유클리드 거리)에서 Kruskal 알고리즘 적용
import sys
import math
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, a, b):
    a, b = find(parent, a), find(parent, b)
    if a == b:
        return False
    if rank[a] < rank[b]:
        a, b = b, a
    parent[b] = a
    if rank[a] == rank[b]:
        rank[a] += 1
    return True

def main():
    N = int(input())
    stars = [tuple(map(float, input().split())) for _ in range(N)]

    # 모든 간선 생성
    edges = []
    for i in range(N):
        for j in range(i + 1, N):
            dist = math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2)
            edges.append((dist, i, j))
    edges.sort()

    parent = list(range(N))
    rank = [0] * N
    total = 0.0
    count = 0

    for dist, u, v in edges:
        if union(parent, rank, u, v):
            total += dist
            count += 1
            if count == N - 1:
                break

    print(f"{total:.2f}")

main()
