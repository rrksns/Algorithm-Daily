"""
1. 핵심아이디어
    N<= 8 최대경우의수: 8! = 40320
    모든 순열 열거해 값을 계산 최대값 출력
"""

# 내부 순열 생성 라이브러리 이용

from itertools import permutations

# 입력
n = int(input())
a = list(map(int, input().split()))

# 모든 순열을 시도하여 |A[0]-A[1]| + ... + |A[N-2]-A[N-1]| 최댓값 구하기
max_val = 0
for perm in permutations(a):
    total = 0
    for i in range(n - 1):
        total += abs(perm[i] - perm[i + 1])
        max_val = max(max_val, total)

print(max_val)

# 직접구현(백트레킹)
# import sys
# input = sys.stdin.readline

# n = int(input())
# a = list(map(int, input().split()))

# max_val = 0
# visited = [False] * n
# perm = []

# def backtrack():
#     global max_val
#     # 순열이 완성되면 식의 값을 계산
#     if len(perm) == n:
#         total = sum(abs(perm[i] - perm[i+1]) for i in range(n-1))
#         max_val = max(max_val, total)
#         return
#     # 아직 사용하지 않은 원소를 하나씩 골라 추가
#     for i in range(n):
#         if not visited[i]:
#             visited[i] = True
#             perm.append(a[i])
#             backtrack()
#             perm.pop()        # 되돌리기 (backtrack)
#             visited[i] = False

# backtrack()
# print(max_val)
