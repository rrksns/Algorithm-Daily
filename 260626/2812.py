# 백준 2812: 크게 만들기
# N자리 수에서 k개 숫자를 제거하여 가장 큰 수 만들기
# 단조 감소 스택(monotone decreasing stack) 사용
# 스택 top보다 현재 숫자가 크면 top을 제거(k 감소), 현재 숫자 push
# 남은 k개는 뒤에서 제거

import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    num = input().strip()

    stack = []
    for d in num:
        while k > 0 and stack and stack[-1] < d:
            stack.pop()
            k -= 1
        stack.append(d)

    # k가 남아있으면 뒤에서 제거
    if k > 0:
        stack = stack[:-k]

    print(''.join(stack))

solve()
