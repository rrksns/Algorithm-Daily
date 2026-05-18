# 최대 힙: 정수를 최대 힙에 넣고 최댓값을 꺼내는 자료구조
# 핵심 아이디어:
#   Python의 heapq는 최소 힙이므로, 값을 음수로 저장하면 최대 힙처럼 동작
#   - x > 0 이면: heappush(heap, -x)
#   - x == 0 이면: 힙이 비어있으면 0, 아니면 -heappop(heap) 출력

import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
result = []

for _ in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(heap, -x)
    else:
        if heap:
            result.append(-heapq.heappop(heap))
        else:
            result.append(0)

print('\n'.join(map(str, result)))
