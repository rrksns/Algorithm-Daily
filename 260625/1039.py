# 교환 - BFS
# N의 두 자리를 서로 교환하는 연산을 K번 수행해 만들 수 있는 최대값
# 핵심 아이디어:
# BFS로 (현재 숫자 문자열, 남은 교환 횟수) 상태를 탐색
# 각 상태에서 모든 위치 쌍(i,j)를 교환해보고, 앞자리가 0이 되는 경우 제외
# 같은 (숫자, 남은횟수) 상태 재방문 방지
# 남은 횟수가 0일 때 최대값 갱신
# 가능한 순열 수는 최대 8! = 40320이므로 BFS가 효율적

import sys
from collections import deque
input = sys.stdin.readline

def solve():
    N, K = map(int, input().split())
    s = str(N)
    n = len(s)
    
    # (number_str, swaps_remaining)
    visited = set()
    queue = deque()
    queue.append((s, K))
    visited.add((s, K))
    
    ans = -1
    
    while queue:
        cur, k = queue.popleft()
        
        if k == 0:
            ans = max(ans, int(cur))
            continue
        
        # 모든 두 위치 쌍 교환 시도
        cur_list = list(cur)
        for i in range(n - 1):
            for j in range(i + 1, n):
                cur_list[i], cur_list[j] = cur_list[j], cur_list[i]
                # 앞자리가 0이면 스킵
                if cur_list[0] != '0':
                    nxt = ''.join(cur_list)
                    state = (nxt, k - 1)
                    if state not in visited:
                        visited.add(state)
                        queue.append((nxt, k - 1))
                cur_list[i], cur_list[j] = cur_list[j], cur_list[i]
    
    print(ans)

solve()
