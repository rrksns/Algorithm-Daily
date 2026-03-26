import sys
input = sys.stdin.readline

def solution():
    N, M, K = map(int, input().split())

    # 간선 입력 (가중치 = 입력 순서 1~M)
    edges = []
    for i in range(1, M + 1):
        x, y = map(int, input().split())
        edges.append((i, x, y))  # (가중치, u, v)

    removed = set()  # 제거된 간선 가중치 집합
    results = []

    for turn in range(K):
        # Union-Find 초기화
        parent = list(range(N + 1))
        rank_ = [0] * (N + 1)

        def find(x):
            # 경로 압축 (반복문)
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if rank_[px] < rank_[py]:
                px, py = py, px
            parent[py] = px
            if rank_[px] == rank_[py]:
                rank_[px] += 1
            return True

        # 크루스칼 알고리즘 (이미 가중치 오름차순 정렬됨)
        mst_cost = 0
        mst_edges = []
        edge_count = 0

        for w, u, v in edges:
            if w in removed:
                continue
            if union(u, v):
                mst_cost += w
                mst_edges.append(w)
                edge_count += 1
                if edge_count == N - 1:
                    break

        if edge_count < N - 1:
            # MST 불가능 → 나머지 모두 0
            results.extend([0] * (K - turn))
            break
        else:
            results.append(mst_cost)
            # 현재 MST에서 가중치 최솟값 간선 제거
            removed.add(min(mst_edges))

    print(*results)

solution()