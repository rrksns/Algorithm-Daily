# 크로아티아 알파벳 - String
# 크로아티아 알파벳에는 특수 표현이 있음 (c=, c-, dz=, d-, lj, nj, s=, z=)
# 핵심 아이디어: 특수 알파벳 문자열을 순서대로 치환 후 길이를 세면 됨
# 단, dz=은 d-보다 먼저 처리해야 함

import sys
input = sys.stdin.readline

s = input().strip()

# dz= 먼저 처리 (d-와 혼동 방지)
croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for ch in croatian:
    s = s.replace(ch, '*')

print(len(s))
