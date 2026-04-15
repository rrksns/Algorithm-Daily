import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    L, n = map(int, input().split())
    ants = [int(input()) for _ in range(n)]

    min_time = max(min(p, L - p) for p in ants)
    max_time = max(max(p, L - p) for p in ants)

    print(min_time, max_time)
