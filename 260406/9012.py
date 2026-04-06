"""
1.아이디어
 괄호는 한쌍이어야 VPS가됨
 "("가 반듯이 먼저나와야함
2.시간복잡도
 O(T*N(stirng길이))
3.변수
 문자 저장 변수
"""

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    s = input().strip()
    stack = 0
    valid = True

    for c in s:
        if c == "(":
            stack += 1
        else:  # c == ')'
            stack -= 1
            if stack < 0:  # 닫는 괄호가 열린 괄호보다 많으면 즉시 NO
                valid = False
                break

    print("YES" if valid and stack == 0 else "NO")
