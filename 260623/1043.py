# 백준 1043: 거짓말
# 진실을 아는 사람과 같은 파티에 참석하면 거짓말 불가
# Union-Find로 같은 파티의 사람들을 하나의 그룹으로 묶음
# 진실을 아는 사람이 포함된 그룹이면 해당 파티에서는 거짓말 불가
# 거짓말 가능한 파티 수 = 전체 파티 - 진실 그룹이 포함된 파티

import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a, b = find(parent, a), find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solve():
    n, m = map(int, input().split())
    parent = list(range(n + 1))

    know_cnt, *know = map(int, input().split())
    know_set = set(know)

    parties = []
    for _ in range(m):
        cnt, *people = map(int, input().split())
        parties.append(people)
        for i in range(1, len(people)):
            union(parent, people[0], people[i])

    result = 0
    for people in parties:
        # 파티 구성원 중 진실을 아는 사람이 있으면 거짓말 불가
        can_lie = all(find(parent, p) not in {find(parent, k) for k in know_set} for p in people)
        if can_lie:
            result += 1

    print(result)

solve()
