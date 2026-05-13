# 블랙잭 - 브루트포스
# 핵심 아이디어:
# N장의 카드 중 3장을 골라 합이 M을 넘지 않는 최댓값을 찾는다.
# N이 최대 100이므로 3중 반복문 O(N^3) = 최대 100^3 = 1,000,000으로 충분히 풀 수 있다.
# itertools.combinations를 사용해 3장의 조합을 모두 탐색한다.

import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))

ans = 0
for combo in combinations(cards, 3):
    s = sum(combo)
    if s <= M:
        ans = max(ans, s)

print(ans)
