# 듣보잡 - 정렬 + 집합 (Sorting)
# 아이디어: 못 듣는 사람 집합에서 못 보는 사람을 탐색 후 정렬 출력

import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    deaf = set(input().rstrip() for _ in range(N))
    blind = [input().rstrip() for _ in range(M)]

    result = sorted(name for name in blind if name in deaf)
    print(len(result))
    print('\n'.join(result))

solve()
