# 분해합 - 브루트 포스
# 어떤 수 N의 분해합 D(N) = N + N의 각 자릿수 합
# M이 주어질 때 D(N) = M인 가장 작은 N(생성자)를 구함
# 생성자 후보 범위: M - (자릿수 * 9) ~ M-1
# 최대 6자리이므로 M-54 ~ M-1 구간에서 완전탐색

import sys
input = sys.stdin.readline

M = int(input())

ans = 0
for n in range(max(1, M - 54), M):
    digit_sum = sum(int(d) for d in str(n))
    if n + digit_sum == M:
        ans = n
        break

print(ans)
