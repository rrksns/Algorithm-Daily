# [Greedy] 로프
# 핵심 아이디어:
# k개의 로프를 병렬로 사용할 때, 들 수 있는 최대 하중 = (k개 중 가장 약한 로프의 최대 중량) × k
# 로프를 내림차순 정렬 후, i번째 로프까지 사용할 때의 최댓값을 순회하며 최댓값 갱신
# 정렬된 로프[i]가 i+1개 중 가장 약하므로 loads[i] * (i+1)이 해당 경우의 최대 중량

import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    loads = [int(input()) for _ in range(N)]
    loads.sort(reverse=True)
    
    ans = 0
    for i, w in enumerate(loads):
        ans = max(ans, w * (i + 1))
    
    print(ans)

solve()
