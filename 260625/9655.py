# 돌 게임 - 게임 이론 / DP
# 돌을 1개 또는 3개 가져갈 수 있고 마지막 돌을 가져가는 사람이 승리
# 핵심 아이디어:
# dp[i] = i개 돌 남았을 때 현재 차례인 사람이 이기면 True
# dp[1]=True(1개 가져가서 승), dp[2]=False(1개만 가능→상대가 1개 가져가 승),
# dp[3]=True(3개 가져가서 승), dp[4]=False(어떻게 해도 상대가 이김)
# → N이 홀수면 SK 승, 짝수면 CY 승

import sys
input = sys.stdin.readline

N = int(input())
print("SK" if N % 2 == 1 else "CY")
