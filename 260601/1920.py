# 수 찾기 - Binary Search
# N개의 정수 집합에서 M개의 수가 존재하는지 이진 탐색으로 확인
# sorted + bisect 모듈 활용 → O((N+M) log N)

import sys
from bisect import bisect_left

input = sys.stdin.readline

def exists(arr, x):
    i = bisect_left(arr, x)
    return i < len(arr) and arr[i] == x

N = int(input())
A = sorted(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

result = []
for x in B:
    result.append('1' if exists(A, x) else '0')

print('\n'.join(result))
