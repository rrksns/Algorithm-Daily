# 대회 or 인턴: 남학생 N명, 여학생 M명, 인턴 최소 K명 확보
# 팀 = 남2 + 여1, 팀 수 T 최대화
# 조건: N-2T >= 0, M-T >= 0, (N-2T)+(M-T) >= K
# => T <= N//2, T <= M, T <= (N+M-K)//3
import sys
input = sys.stdin.readline

def solve():
    N, M, K = map(int, input().split())
    ans = min(N // 2, M, (N + M - K) // 3)
    print(max(0, ans))

solve()
