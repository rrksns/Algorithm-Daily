# 포도주 시식 - DP
# 포도주가 n잔 있고, 연속 3잔은 마실 수 없음. 마실 수 있는 포도주 양의 최댓값 구하기
# dp[i] = i번째 포도주까지 고려했을 때 마실 수 있는 최대 양
# 3가지 경우:
#   1) i번 포도주를 마시지 않음: dp[i-1]
#   2) i번 포도주만 마심 (i-1은 안 마심): dp[i-2] + wine[i]
#   3) i-1, i번 연속 마심: dp[i-3] + wine[i-1] + wine[i]

import sys
input = sys.stdin.readline

def main():
    n = int(input())
    wine = [0] + [int(input()) for _ in range(n)]
    
    if n == 1:
        print(wine[1])
        return
    if n == 2:
        print(wine[1] + wine[2])
        return
    
    dp = [0] * (n + 1)
    dp[1] = wine[1]
    dp[2] = wine[1] + wine[2]
    
    for i in range(3, n + 1):
        dp[i] = max(
            dp[i-1],                          # i번 안 마심
            dp[i-2] + wine[i],                # i-1번 안 마시고 i번 마심
            dp[i-3] + wine[i-1] + wine[i]    # i-1, i번 연속 마심
        )
    
    print(dp[n])

main()
