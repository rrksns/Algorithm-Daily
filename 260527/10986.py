# 나머지 합 (BOJ 10986) - PrefixSum
#
# 핵심 아이디어:
# 구간 합 sum(i..j) = prefix[j] - prefix[i-1]
# 이 값이 M으로 나누어 떨어지려면 prefix[j] % M == prefix[i-1] % M
# → 각 나머지 값의 빈도를 세어, 같은 나머지끼리 2개씩 뽑는 조합 수를 더한다
# 나머지가 0인 prefix sum도 그 자체로 M의 배수이므로 cnt[0]을 초기값 1로 시작

import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    cnt = [0] * M
    cnt[0] = 1  # 빈 prefix (합 0)
    prefix_mod = 0
    ans = 0

    for a in A:
        prefix_mod = (prefix_mod + a) % M
        ans += cnt[prefix_mod]
        cnt[prefix_mod] += 1

    print(ans)

solve()
