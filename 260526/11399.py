# 백준 11399 - ATM
# 핵심 아이디어:
# 각 사람의 대기 시간 = 자신 포함 앞 사람들의 인출 시간 합계
# 전체 대기 시간 합을 최소화하려면 인출 시간이 짧은 사람부터 세워야 한다 (그리디)
# 정렬 후 누적합 계산: sum(prefix_sums)
# 시간복잡도: O(N log N)

import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
p.sort()

total = 0
prefix = 0
for t in p:
    prefix += t
    total += prefix

print(total)
