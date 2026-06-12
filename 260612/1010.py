# 다리 놓기: 서쪽 N개 사이트를 동쪽 M개 사이트에 연결
# 다리는 교차 불가 → 동쪽에서 N개를 순서대로 선택 = 조합 C(M, N)
import sys
input = sys.stdin.readline
from math import comb

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(comb(M, N))
