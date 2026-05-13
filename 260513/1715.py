# 카드 정렬하기 - 힙 (우선순위 큐)
# 핵심 아이디어:
# N묶음의 카드를 두 묶음씩 합쳐 1묶음으로 만들 때 비교 횟수의 최솟값을 구한다.
# 합칠 때마다 비교 횟수 = 두 묶음 카드 수의 합이 추가된다.
# 항상 가장 작은 두 묶음을 먼저 합치면 전체 비용이 최소가 된다 (그리디).
# 최소 힙(heapq)을 사용해 매 단계에서 O(log N) 으로 최솟값 2개를 꺼내 합산 후 다시 삽입한다.

import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    heapq.heappush(heap, int(input()))

total = 0
while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    merged = a + b
    total += merged
    heapq.heappush(heap, merged)

print(total)
