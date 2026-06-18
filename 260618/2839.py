# 설탕 배달 - Greedy/Math
# N킬로그램을 3kg, 5kg 봉지로 정확히 나눌 때 최소 봉지 수
# 핵심 아이디어: 5kg 봉지를 최대한 많이 사용하되,
#   나머지가 3의 배수이면 성공. 5kg 봉지를 줄여가며 탐색.

import sys
input = sys.stdin.readline

N = int(input())

ans = -1
for five in range(N // 5, -1, -1):
    remain = N - five * 5
    if remain % 3 == 0:
        ans = five + remain // 3
        break

print(ans)
