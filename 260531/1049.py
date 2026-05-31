# 기타줄 - Greedy
# 6개 묶음 최저가(pack)와 낱개 최저가(single)를 구한 후
# 가능한 구매 방식: 묶음 k개(k=0..ceil(N/6)) + 나머지 낱개
# 낱개가 묶음보다 비싸면 낱개 대신 묶음으로 구매하는 것도 고려

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pack = float('inf')
single = float('inf')
for _ in range(M):
    p, s = map(int, input().split())
    pack = min(pack, p)
    single = min(single, s)

ans = float('inf')
for k in range((N // 6) + 2):
    cost = k * pack
    remain = N - k * 6
    if remain > 0:
        cost += remain * single
    ans = min(ans, cost)

print(ans)
