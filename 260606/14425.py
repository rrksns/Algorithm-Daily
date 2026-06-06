# [HashSet] 문자열 집합 - BOJ 14425
# N개의 문자열 집합 S에, M개의 문자열 중 S에 포함된 것의 개수 출력
# 핵심 아이디어:
# - set에 N개 저장 후 M개 각각 O(1) 조회

import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    S = {input().rstrip() for _ in range(N)}
    count = sum(1 for _ in range(M) if input().rstrip() in S)
    print(count)

solve()
