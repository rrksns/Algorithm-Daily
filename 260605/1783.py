# [Greedy] 병든 나이팅게일 - BOJ 1783
# 이동 종류 4가지: (±2, +1), (±1, +2) → 열은 항상 증가
# 이동 횟수 >= 4이면 4가지를 모두 최소 1번씩 사용해야 함
#
# 분석:
# - N=1: 행 이동 불가 → 방문 칸 1개
# - N=2: (±2, +1) 사용 불가 (범위 초과) → 2열씩 이동만 가능
#         최대 3번 이동 가능 (4번이면 4종 필수인데 2종뿐이라 불가)
#         이동당 2열 소모: max_moves = min((M-1)//2, 3)
# - N>=3: 4종 모두 사용 가능
#         4종 최소 열 소모: 1+1+2+2 = 6열 (4번 이동)
#         M <= 4: M칸 방문 (이동 M-1번, 4종 제한 없음)
#         M <= 6: 4칸 방문 (4종 제한 못 채우므로 최대 3번 이동)
#         M >= 7: M-2칸 방문 (4번+나머지 1열씩)

import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    
    if N == 1:
        print(1)
    elif N == 2:
        moves = min((M - 1) // 2, 3)
        print(moves + 1)
    else:  # N >= 3
        if M <= 4:
            print(M)
        elif M <= 6:
            print(4)
        else:
            print(M - 2)

solve()
