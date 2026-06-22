# N과 M (3) - DFS 백트래킹 (중복 순열)
# 1~N 중 M개를 고르되 중복 허용, 오름차순 아닌 순서도 가능
# => visited 없이, 매 단계마다 1~N 전체에서 선택
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = []

def dfs():
    if len(result) == M:
        print(*result)
        return
    for i in range(1, N + 1):
        result.append(i)
        dfs()
        result.pop()

dfs()
