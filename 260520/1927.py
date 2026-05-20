# 최소 힙 (Min Heap)
# 핵심 아이디어: Python의 heapq 모듈을 활용한 최소 힙 구현
# - 연산 x > 0: 힙에 x를 삽입
# - 연산 x = 0: 힙에서 최솟값 출력 후 제거 (힙이 비어있으면 0 출력)
import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
result = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if heap:
            result.append(heapq.heappop(heap))
        else:
            result.append(0)
    else:
        heapq.heappush(heap, x)

print('\n'.join(map(str, result)))
