# 가장 긴 바이토닉 부분 수열
# 아이디어: 각 위치 i에서 왼쪽 LIS + 오른쪽 LIS(역방향) - 1이 바이토닉 길이
# lis[i]: i에서 끝나는 증가 부분수열 최대 길이
# lds[i]: i에서 시작하는 감소 부분수열 최대 길이 = 배열 뒤집은 후의 LIS

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

# LIS ending at i
lis = [1] * n
for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:
            lis[i] = max(lis[i], lis[j] + 1)

# LDS starting at i (= LIS from right)
lds = [1] * n
for i in range(n-2, -1, -1):
    for j in range(i+1, n):
        if a[j] < a[i]:
            lds[i] = max(lds[i], lds[j] + 1)

print(max(lis[i] + lds[i] - 1 for i in range(n)))
