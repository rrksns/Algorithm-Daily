# 백준 2357 - 최솟값과 최댓값
# 핵심 아이디어: 세그먼트 트리(Segment Tree)를 두 개 구성
#   - 하나는 구간 최솟값, 하나는 구간 최댓값을 관리
#   - 각 쿼리 [a, b]에 대해 O(log N) 시간에 최솟값, 최댓값 반환
#   - 트리 구성: 리프 노드에 원소를 저장, 내부 노드에는 자식들의 min/max

import sys
input = sys.stdin.readline

def build(arr, n):
    min_tree = [float('inf')] * (4 * n)
    max_tree = [float('-inf')] * (4 * n)
    
    def build_tree(node, start, end):
        if start == end:
            min_tree[node] = arr[start]
            max_tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            build_tree(2*node, start, mid)
            build_tree(2*node+1, mid+1, end)
            min_tree[node] = min(min_tree[2*node], min_tree[2*node+1])
            max_tree[node] = max(max_tree[2*node], max_tree[2*node+1])
    
    build_tree(1, 0, n-1)
    return min_tree, max_tree

def query(min_tree, max_tree, node, start, end, l, r):
    if r < start or end < l:
        return float('inf'), float('-inf')
    if l <= start and end <= r:
        return min_tree[node], max_tree[node]
    mid = (start + end) // 2
    lmin, lmax = query(min_tree, max_tree, 2*node, start, mid, l, r)
    rmin, rmax = query(min_tree, max_tree, 2*node+1, mid+1, end, l, r)
    return min(lmin, rmin), max(lmax, rmax)

def main():
    sys.setrecursionlimit(300000)
    n, m = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    min_tree, max_tree = build(arr, n)
    
    results = []
    for _ in range(m):
        a, b = map(int, input().split())
        mn, mx = query(min_tree, max_tree, 1, 0, n-1, a-1, b-1)
        results.append(f"{mn} {mx}")
    
    print('\n'.join(results))

main()
