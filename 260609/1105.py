# [L, R] 범위에서 8이 가장 적게 포함된 수의 8 개수 구하기
# 핵심 아이디어:
# - L과 R의 자릿수가 다르면, 8이 없는 수(예: 10, 100)가 반드시 존재 → 답 0
# - 자릿수가 같으면: L과 R의 공통 접두사에서 8의 개수를 세면 된다
#   (접두사 이후 자리는 8이 아닌 숫자로 자유롭게 선택 가능)
import sys
input = sys.stdin.readline

L, R = input().split()
if len(L) != len(R):
    print(0)
else:
    count = 0
    for a, b in zip(L, R):
        if a != b:
            break
        if a == '8':
            count += 1
    print(count)
