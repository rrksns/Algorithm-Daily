import sys
input = sys.stdin.readline

# 입력 받기
N, S, M = map(int, input().split())
V = list(map(int, input().split()))

# 현재 가능한 볼륨의 집합
possible = {S}

# 각 곡마다 볼륨 변경
for v in V:
    next_possible = set()
    for p in possible:
        if p + v <= M:
            next_possible.add(p + v)
        if p - v >= 0:
            next_possible.add(p - v)
    possible = next_possible
    if not possible:
        break

# 결과 출력: 가능한 볼륨이 없으면 -1, 있으면 최댓값
print(max(possible) if possible else -1)