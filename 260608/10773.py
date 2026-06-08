# 제로 - Stack
# 핵심 아이디어: 스택을 사용하여 숫자를 저장하고
# 0이 입력되면 마지막 숫자를 제거, 최종 합산
import sys
input = sys.stdin.readline

K = int(input())
stack = []
for _ in range(K):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))
