# 절댓값 힙 - Heap
# 아이디어: (절댓값, 원래값) 튜플을 최소 힙에 저장
# Python heapq는 최소 힙 → (|x|, x)로 저장하면 절댓값 기준 정렬 자동
import sys
import heapq
input = sys.stdin.readline

def solve():
    n = int(input())
    heap = []
    for _ in range(n):
        x = int(input())
        if x != 0:
            heapq.heappush(heap, (abs(x), x))
        else:
            if heap:
                print(heapq.heappop(heap)[1])
            else:
                print(0)

solve()
