# 잃어버린 괄호 - Greedy
# 핵심 아이디어:
# '-' 이후에 나오는 모든 숫자를 괄호로 묶으면 최소값을 얻을 수 있다.
# 예: A - B + C + D = A - (B + C + D)
# 즉, '-'를 기준으로 분리한 뒤, 첫 번째 그룹은 더하고 나머지 그룹은 모두 뺀다.

import sys
input = sys.stdin.readline

expr = input().strip()
# '-'로 분리
parts = expr.split('-')

result = sum(map(int, parts[0].split('+')))
for part in parts[1:]:
    result -= sum(map(int, part.split('+')))

print(result)
