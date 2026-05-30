# 여행 가자 (Union-Find)
# 핵심 아이디어: 연결된 도시들을 유니온-파인드로 같은 그룹으로 묶은 뒤,
# 여행 계획의 모든 도시가 같은 그룹인지 확인

import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a, b = find(parent, a), find(parent, b)
    if a != b:
        parent[b] = a

def solve():
    N = int(input())
    M = int(input())
    parent = list(range(N + 1))
    
    for i in range(1, N + 1):
        row = list(map(int, input().split()))
        for j in range(N):
            if row[j] == 1:
                union(parent, i, j + 1)
    
    plan = list(map(int, input().split()))
    root = find(parent, plan[0])
    
    if all(find(parent, city) == root for city in plan):
        print("YES")
    else:
        print("NO")

solve()
