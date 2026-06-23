# 신입 사원 - 그리디
# 핵심 아이디어: 서류 순위로 정렬하면, 뒤에 오는 지원자는 서류에서 반드시 불리.
# 따라서 면접 순위가 지금까지 선발된 지원자 중 최솟값보다 작아야만 선발 가능.
# 서류 1등은 무조건 선발, 이후 면접 순위 최솟값 갱신하며 카운트.

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    applicants = [tuple(map(int, input().split())) for _ in range(N)]
    # 서류 순위 기준 정렬
    applicants.sort()
    
    count = 1
    min_interview = applicants[0][1]
    
    for i in range(1, N):
        if applicants[i][1] < min_interview:
            count += 1
            min_interview = applicants[i][1]
    
    print(count)
