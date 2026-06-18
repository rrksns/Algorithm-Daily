# BOJ 11055 - 가장 큰 증가하는 부분 수열 (DP)
# 핵심 아이디어:
# dp[i] = A[i]로 끝나는 증가 부분 수열의 원소 합 최댓값.
# dp[i] = max(dp[j] + A[i]) for all j < i where A[j] < A[i]
# 초기값: dp[i] = A[i] (자기 자신만 포함)
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = A[:]  # dp[i] 초기값 = A[i]

for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + A[i])

print(max(dp))
