import sys
input = sys.stdin.readline

# 입력
N, S, M = map(int, input().split())
V = list(map(int, input().split()))

# dp[j] = 현재 곡을 j 볼륨으로 연주할 수 있는지 여부
# 시작 전 볼륨 S에서 출발
dp = [False] * (M + 1)
dp[S] = True

for i in range(N):
    next_dp = [False] * (M + 1)
    for j in range(M + 1):
        if dp[j]:
            # 볼륨을 V[i]만큼 더하거나 빼기
            if j + V[i] <= M:
                next_dp[j + V[i]] = True
            if j - V[i] >= 0:
                next_dp[j - V[i]] = True
    dp = next_dp

# 마지막 곡의 최대 볼륨 (뒤에서부터 탐색)
result = -1
for j in range(M, -1, -1):
    if dp[j]:
        result = j
        break

print(result)