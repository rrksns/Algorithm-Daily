# 가운데를 말해요 - Heap (최대힙 + 최소힙)
# 아이디어:
#   - 하한 최대힙(max_heap): 중앙값 이하의 수들, 루트가 중앙값
#   - 상한 최소힙(min_heap): 중앙값 초과의 수들
#   - 항상 max_heap 크기 >= min_heap 크기 (차이 최대 1)
#   - 새 수 추가 후 두 힙의 균형 유지
#   - 중앙값 = max_heap의 루트

import sys
import heapq
input = sys.stdin.readline

def main():
    n = int(input())
    max_heap = []  # 최대힙 (음수로 저장)
    min_heap = []  # 최소힙
    
    result = []
    for _ in range(n):
        x = int(input())
        
        # max_heap이 비어있거나 x가 max_heap 루트보다 작으면 max_heap에 삽입
        if not max_heap or x <= -max_heap[0]:
            heapq.heappush(max_heap, -x)
        else:
            heapq.heappush(min_heap, x)
        
        # 균형 맞추기: max_heap 크기가 min_heap보다 2 이상 크면
        if len(max_heap) > len(min_heap) + 1:
            val = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, val)
        # min_heap 크기가 max_heap보다 크면
        elif len(min_heap) > len(max_heap):
            val = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -val)
        
        result.append(-max_heap[0])
    
    print('\n'.join(map(str, result)))

main()
