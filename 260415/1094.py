import sys

input = sys.stdin.readline

X = int(input())

sticks = [64]  # 현재 보유한 막대 목록

while sum(sticks) != X:
    shortest = min(sticks)
    sticks.remove(shortest)
    half = shortest // 2
    sticks.append(half)  # 한 쪽은 항상 유지
    if sum(sticks) <= X:
        sticks.append(half)  # 합이 X 이하면 나머지도 유지

print(len(sticks))
