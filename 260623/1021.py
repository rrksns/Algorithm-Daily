# 백준 1021: 회전하는 큐
# 덱(deque)을 사용하여 원하는 원소를 꺼낼 때 필요한 최소 이동 횟수 계산
# 각 원소마다 왼쪽 회전 또는 오른쪽 회전 중 더 적은 횟수를 선택
# 인덱스 idx에 대해 min(idx, len(dq)-idx)가 최소 이동 횟수

import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    targets = list(map(int, input().split()))
    dq = deque(range(1, n + 1))
    result = 0

    for t in targets:
        idx = dq.index(t)
        left_moves = idx
        right_moves = len(dq) - idx
        if left_moves <= right_moves:
            result += left_moves
            for _ in range(left_moves):
                dq.append(dq.popleft())
        else:
            result += right_moves
            for _ in range(right_moves):
                dq.appendleft(dq.pop())
        dq.popleft()

    print(result)

solve()
