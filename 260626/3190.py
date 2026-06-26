# 백준 3190: 뱀
# 덱으로 뱀의 몸통 위치 관리 (head=appendleft, tail=pop)
# 사과 있으면 꼬리 유지, 없으면 꼬리 제거
# 벽 또는 자기 몸과 충돌 시 종료

import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n = int(input())
    k = int(input())
    apples = set()
    for _ in range(k):
        r, c = map(int, input().split())
        apples.add((r, c))

    l = int(input())
    commands = {}
    for _ in range(l):
        t, d = input().split()
        commands[int(t)] = d

    # 방향: 0=우, 1=하, 2=좌, 3=상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    snake = deque()
    snake.appendleft((1, 1))
    visited = {(1, 1)}
    direction = 0
    time = 0

    while True:
        time += 1
        hr, hc = snake[0]
        nr, nc = hr + dr[direction], hc + dc[direction]

        # 벽 또는 자기 몸 충돌
        if not (1 <= nr <= n and 1 <= nc <= n) or (nr, nc) in visited:
            break

        snake.appendleft((nr, nc))
        visited.add((nr, nc))

        if (nr, nc) in apples:
            apples.remove((nr, nc))
        else:
            tail = snake.pop()
            visited.remove(tail)

        if time in commands:
            if commands[time] == 'L':
                direction = (direction - 1) % 4
            else:
                direction = (direction + 1) % 4

    print(time)

solve()
