import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    logs = list(map(int, input().split()))
    logs.sort()  # 정렬

    # 양 끝 쌍 (1칸 차이 인접)
    ans = max(logs[1] - logs[0], logs[-1] - logs[-2])

    # 나머지 쌍 (2칸 차이 인접)
    for i in range(2, N):
        ans = max(ans, logs[i] - logs[i - 2])

    print(ans)
