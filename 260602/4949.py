# 4949 균형잡힌 세상 - Stack
# 괄호 문자열의 균형 여부 확인: (, [ 는 스택에 push, ), ] 는 pop 후 짝 확인
# 빈 줄(.)이 나오면 종료

import sys
input = sys.stdin.readline

while True:
    line = input().rstrip('\n')
    if line == '.':
        break
    stack = []
    balanced = True
    for ch in line:
        if ch in ('(', '['):
            stack.append(ch)
        elif ch == ')':
            if not stack or stack[-1] != '(':
                balanced = False
                break
            stack.pop()
        elif ch == ']':
            if not stack or stack[-1] != '[':
                balanced = False
                break
            stack.pop()
    if balanced and not stack:
        print('yes')
    else:
        print('no')
