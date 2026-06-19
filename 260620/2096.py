# 내려가기 - DP (슬라이딩 윈도우)
# 아이디어: N줄, 각 줄 3개 숫자. 위→아래 이동 시 같은 열 or 인접 열만 가능
# max/min DP를 동시에 유지. 메모리 절약 위해 직전 행만 저장
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    row = list(map(int, input().split()))
    dp_max = row[:]
    dp_min = row[:]

    for _ in range(N - 1):
        row = list(map(int, input().split()))
        new_max = [0, 0, 0]
        new_min = [0, 0, 0]
        new_max[0] = row[0] + max(dp_max[0], dp_max[1])
        new_max[1] = row[1] + max(dp_max[0], dp_max[1], dp_max[2])
        new_max[2] = row[2] + max(dp_max[1], dp_max[2])
        new_min[0] = row[0] + min(dp_min[0], dp_min[1])
        new_min[1] = row[1] + min(dp_min[0], dp_min[1], dp_min[2])
        new_min[2] = row[2] + min(dp_min[1], dp_min[2])
        dp_max = new_max
        dp_min = new_min

    print(max(dp_max), min(dp_min))

solve()
