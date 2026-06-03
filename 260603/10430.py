# 나머지 연산의 분배 법칙 검증
# (A+B) % C == ((A%C) + (B%C)) % C
# (A×B) % C == ((A%C) × (B%C)) % C
# 단순히 공식대로 계산하여 출력

import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)
