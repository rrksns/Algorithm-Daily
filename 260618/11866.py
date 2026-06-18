# BOJ 11866 - 요세푸스 문제 0 (Queue)
# 핵심 아이디어:
# 1~N을 deque에 넣고, K번째마다 제거하는 시뮬레이션.
# K-1번 앞에서 뺀 뒤 맨 뒤로 넣고(rotate), K번째는 제거.
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
dq = deque(range(1, N + 1))
result = []

while dq:
    dq.rotate(-(K - 1))   # K-1번 앞으로 당기기
    result.append(dq.popleft())

print('<' + ', '.join(map(str, result)) + '>')
