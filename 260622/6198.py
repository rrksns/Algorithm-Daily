# 옥상 정원 꾸미기 - 단조 감소 스택
# 핵심 아이디어: 스택에 아직 오른쪽 시야가 열린 빌딩을 유지.
# 빌딩 j를 처리할 때, 스택에 있는 모든 빌딩은 j를 볼 수 있음(스택 감소 성질).
# h[j]보다 낮거나 같은 빌딩은 j에 의해 시야 차단 → 팝.

import sys
input = sys.stdin.readline

N = int(input())
heights = [int(input()) for _ in range(N)]

ans = 0
stack = []  # 단조 감소 스택 (높이 저장)

for h in heights:
    # 현재 빌딩 h를 볼 수 있는 빌딩 수 = 스택 크기
    ans += len(stack)
    # h보다 낮거나 같은 빌딩은 h 이후 시야 차단 → 팝
    while stack and stack[-1] <= h:
        stack.pop()
    stack.append(h)

print(ans)
