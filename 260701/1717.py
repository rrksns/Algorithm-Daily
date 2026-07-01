# 1717 집합의 표현 (Union-Find)
# 아이디어: 유니온 파인드(서로소 집합) 자료구조를 사용.
# path compression(경로 압축) + union by rank로 시간복잡도를 거의 O(1)에 가깝게 만든다.
# 연산 0 a b: a와 b가 속한 집합을 합침
# 연산 1 a b: a와 b가 같은 집합인지 확인(YES/NO)
import sys
input = sys.stdin.readline


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return
    if rank[a] < rank[b]:
        a, b = b, a
    parent[b] = a
    if rank[a] == rank[b]:
        rank[a] += 1


n, m = map(int, input().split())
parent = list(range(n + 1))
rank = [0] * (n + 1)
out = []
for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b)
    else:
        out.append("YES" if find(a) == find(b) else "NO")

print('\n'.join(out))
