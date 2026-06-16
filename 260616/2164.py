# BOJ 2164 - 카드2 (Queue)
# 핵심 아이디어:
# deque를 이용해 카드 더미를 시뮬레이션한다.
# 1) 맨 위 카드를 버린다 (popleft)
# 2) 맨 위 카드를 맨 아래로 이동 (popleft 후 append)
# 마지막 남은 카드가 정답.
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
dq = deque(range(1, N + 1))

while len(dq) > 1:
    dq.popleft()          # 버린다
    dq.append(dq.popleft())  # 맨 아래로

print(dq[0])
