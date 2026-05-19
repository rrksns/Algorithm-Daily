# 네트워크 연결 - 최소 스패닝 트리 (Kruskal 알고리즘)
# 모든 컴퓨터를 연결하는 최소 비용을 구한다.
# 간선을 비용 오름차순으로 정렬 후, Union-Find로 사이클 없이 연결.
import sys
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

def solve():
    N = int(input())
    M = int(input())
    edges = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))
    edges.sort()

    parent = list(range(N + 1))
    rank = [0] * (N + 1)
    total = 0
    count = 0
    for cost, a, b in edges:
        if union(parent, rank, a, b):
            total += cost
            count += 1
            if count == N - 1:
                break

    print(total)

solve()
