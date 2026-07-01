# 2504 괄호의 값 (Stack)
# 아이디어: 스택에 여는 괄호를 쌓으며 현재까지의 곱셈값(num)을 관리한다.
# '(' 를 만나면 num *= 2, '[' 를 만나면 num *= 3.
# 닫는 괄호를 만났을 때 바로 직전 문자가 짝이 되는 여는 괄호라면(즉 "()"나 "[]"처럼 바로 닫히는 경우)
# 그 시점의 num 값을 answer에 더한다. 짝이 맞지 않거나 스택이 비어있으면 잘못된 식(0).
import sys

s = sys.stdin.readline().strip()

stack = []
num = 1
answer = 0
valid = True

for i, ch in enumerate(s):
    if ch == '(':
        num *= 2
        stack.append(ch)
    elif ch == '[':
        num *= 3
        stack.append(ch)
    elif ch == ')':
        if not stack or stack[-1] != '(':
            valid = False
            break
        if s[i - 1] == '(':
            answer += num
        stack.pop()
        num //= 2
    elif ch == ']':
        if not stack or stack[-1] != '[':
            valid = False
            break
        if s[i - 1] == '[':
            answer += num
        stack.pop()
        num //= 3

if stack:
    valid = False

print(answer if valid else 0)
