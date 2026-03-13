import sys
input = sys.stdin.readline

# 레벨 L 햄버거 구조:
# 빵 + 레벨(L-1)버거 + 패티 + 레벨(L-1)버거 + 빵
# 레벨 0: 패티 1개 (층 1개, 패티 1개)

MAX_L = 51

layers = [0] * MAX_L
patties = [0] * MAX_L

layers[0] = 1
patties[0] = 1

for i in range(1, MAX_L):
    layers[i] = 2 * layers[i-1] + 3
    patties[i] = 2 * patties[i-1] + 1


def eat(L, N):
    """레벨 L 햄버거에서 위에서 N층 먹을 때 패티 수"""
    if N == 0:
        return 0
    if L == 0:
        return 1

    if N >= layers[L]:
        return patties[L]

    # 구조: 빵(1) + 레벨(L-1)버거 + 패티(1) + 레벨(L-1)버거 + 빵(1)
    N -= 1  # 위 빵
    if N <= 0:
        return 0

    if N <= layers[L-1]:
        return eat(L-1, N)
    N -= layers[L-1]
    result = patties[L-1]

    N -= 1  # 가운데 패티
    if N <= 0:
        return result + 1
    result += 1

    if N <= layers[L-1]:
        return result + eat(L-1, N)

    return patties[L]


L, N = map(int, input().split())
print(eat(L, N))