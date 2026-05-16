# 회의실 배정 - Greedy
# 가장 많은 회의를 배정하려면 끝나는 시간이 빠른 회의를 우선 선택한다.
# 끝나는 시간 기준 오름차순 정렬 → 끝나는 시간이 같으면 시작 시간 기준 오름차순
# 이전 회의 종료 시간 <= 다음 회의 시작 시간이면 선택

import sys
input = sys.stdin.readline

N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]
# 끝나는 시간 기준 정렬, 같으면 시작 시간 기준
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0
for start, end in meetings:
    if start >= end_time:
        count += 1
        end_time = end

print(count)
