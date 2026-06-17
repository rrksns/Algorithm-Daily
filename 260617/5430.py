# BOJ 5430 - AC (Deque)
# 핵심 아이디어:
# R(뒤집기)을 실제로 수행하면 O(n)이 매번 들어 TLE.
# 대신 "뒤집힌 상태"를 bool 플래그로 관리하고,
# D(삭제)는 플래그에 따라 앞(popleft) 또는 뒤(pop)에서 제거.
# 최종 출력 시 플래그에 따라 순서 결정.
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input().strip()
    n = int(input())
    arr = input().strip()
    
    # 배열 파싱: "[1,2,3]" → deque([1,2,3]), "[]" → deque([])
    if arr == "[]":
        dq = deque()
    else:
        dq = deque(arr[1:-1].split(','))
    
    reversed_ = False
    error = False
    
    for cmd in p:
        if cmd == 'R':
            reversed_ = not reversed_
        else:  # D
            if not dq:
                error = True
                break
            if reversed_:
                dq.pop()
            else:
                dq.popleft()
    
    if error:
        print("error")
    else:
        if reversed_:
            dq = reversed(dq)
        print('[' + ','.join(dq) + ']')
