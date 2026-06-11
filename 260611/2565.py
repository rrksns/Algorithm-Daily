# 전깃줄 (백준 2565)
# 핵심 아이디어: 전깃줄이 교차하지 않으려면, A 전봇대 번호 순으로 정렬했을 때
# B 전봇대 번호가 증가하는 순서(LIS)여야 한다.
# 전체 전깃줄 수 - LIS 길이 = 제거해야 할 최소 전깃줄 수
import sys
input = sys.stdin.readline

def lis_length(arr):
    dp = []
    for x in arr:
        lo, hi = 0, len(dp)
        while lo < hi:
            mid = (lo + hi) // 2
            if dp[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        if lo == len(dp):
            dp.append(x)
        else:
            dp[lo] = x
    return len(dp)

n = int(input())
wires = []
for _ in range(n):
    a, b = map(int, input().split())
    wires.append((a, b))

wires.sort()
b_values = [b for a, b in wires]
print(n - lis_length(b_values))
