import sys

input = sys.stdin.readline

s, e, m = map(int, input().split())
year = 0

while True:
    year += 1

    # (현재 연도 - 목표값)이 주기로 나누어 떨어지는지 확인
    if (year - s) % 15 == 0 and (year - e) % 28 == 0 and (year - m) % 19 == 0:
        break

print(year)
