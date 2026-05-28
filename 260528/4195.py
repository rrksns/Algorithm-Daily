# 친구 네트워크 - Union-Find (유니온 파인드)
# 두 사람을 친구로 연결할 때마다, 해당 네트워크에 속한 친구 수를 출력
# Union-Find에서 각 그룹의 크기를 size 배열로 관리
# 이름을 숫자로 매핑하기 위해 딕셔너리 사용

import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return size[ra]
    # rank 기반 union
    if rank[ra] < rank[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
    if rank[ra] == rank[rb]:
        rank[ra] += 1
    return size[ra]

T = int(input())
for _ in range(T):
    F = int(input())
    parent = {}
    rank = {}
    size = {}
    
    def get_node(name):
        if name not in parent:
            parent[name] = name
            rank[name] = 0
            size[name] = 1
        return name
    
    for _ in range(F):
        a, b = input().split()
        get_node(a)
        get_node(b)
        print(union(a, b))
