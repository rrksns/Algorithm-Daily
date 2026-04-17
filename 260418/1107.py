import sys

input = sys.stdin.readline

target = int(input())
m = int(input())

if m > 0:
    broken = set(input().split())
else:
    broken = set()

min_count = abs(target - 100)

for num in range(1000001):
    num_str = str(num)

    for digit in num_str:
        if digit in broken:
            break
    else:
        min_count = min(min_count, len(num_str) + abs(num - target))

print(min_count)
