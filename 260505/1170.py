import sys

input = sys.stdin.readline

n = input()
m = int(input())
buttons = [input() for _ in range(m)]
now = 100
pick = []

while True:

    cnt = 0
    for t in n:
        if t not in buttons:
            cnt += 1
            pick.append(t)
        else:
            # -1일씩해봄
            # +1씩 해본
            # 둘중 최소를 픽함
            pick.append(t)
