# 파도반 수열: P(n) = P(n-2) + P(n-3) 점화식으로 DP 계산
# P(1)=P(2)=P(3)=1, 이후 2칸 전 + 3칸 전 합산
import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    # 최대 100까지 미리 계산
    p = [0] * 101
    p[1] = p[2] = p[3] = 1
    for i in range(4, 101):
        p[i] = p[i-2] + p[i-3]
    
    for _ in range(T):
        N = int(input())
        print(p[N])

solve()
