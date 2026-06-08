# 등수 매기기 - Sorting
# 핵심 아이디어: 예상 등수를 정렬하고 실제 등수(1~N)와 순서대로 매칭하면
# 재배열 부등식에 의해 |실제 등수 - 예상 등수| 합이 최소가 된다.
import sys
input = sys.stdin.readline

N = int(input())
expected = [int(input()) for _ in range(N)]
expected.sort()

ans = sum(abs(actual - expected[i]) for i, actual in enumerate(range(1, N+1)))
print(ans)
