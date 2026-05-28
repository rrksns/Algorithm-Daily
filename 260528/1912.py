# 연속합 - DP (카데인 알고리즘, Kadane's Algorithm)
# 연속된 부분 배열의 합 중 최댓값을 구하는 문제
# dp[i] = i번째 원소를 반드시 포함하는 연속 부분 배열의 최대합
# dp[i] = max(dp[i-1] + a[i], a[i])
# 이전까지의 합이 음수면 버리고 현재 원소부터 새로 시작

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

cur = a[0]
ans = a[0]
for i in range(1, n):
    cur = max(cur + a[i], a[i])
    ans = max(ans, cur)

print(ans)
