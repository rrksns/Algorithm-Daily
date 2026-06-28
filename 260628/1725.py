# 히스토그램 - 스택 (Stack)
# 아이디어: 단조 증가 스택을 유지하며 가장 큰 직사각형 넓이 계산
# - 현재 막대가 스택 top보다 낮으면 top을 꺼내며 넓이 계산
# - 꺼낸 막대의 높이 * (현재 인덱스 - 새 top 인덱스 - 1)

import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    heights = [int(input()) for _ in range(N)]
    heights.append(0)  # 마지막에 0 추가해 스택 전부 비우기

    stack = []
    ans = 0

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            ans = max(ans, height * width)
        stack.append(i)

    print(ans)

solve()
