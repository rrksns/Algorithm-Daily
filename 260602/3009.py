# 3009 네 번째 점 - Math
# 직사각형의 세 꼭짓점이 주어질 때 네 번째 꼭짓점 찾기
# x좌표, y좌표 각각 독립적으로 처리: 홀수 번 등장하는 좌표값이 답

import sys
input = sys.stdin.readline

xs, ys = [], []
for _ in range(3):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

# 홀수 번 등장하는 값 = 짝이 없는 꼭짓점의 좌표
from collections import Counter
cx = Counter(xs)
cy = Counter(ys)
rx = [k for k, v in cx.items() if v % 2 == 1][0]
ry = [k for k, v in cy.items() if v % 2 == 1][0]
print(rx, ry)
