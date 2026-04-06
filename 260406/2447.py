import sys

input = sys.stdin.readline


def is_star(r, c):
    # 좌표를 3으로 계속 나눌 때 양쪽 나머지가 모두 1이면 공백
    while r > 0 or c > 0:
        if r % 3 == 1 and c % 3 == 1:
            return False
        r //= 3
        c //= 3
    return True


n = int(input())

result = []
for r in range(n):
    row = []
    for c in range(n):
        row.append("*" if is_star(r, c) else " ")
    result.append("".join(row))

print("\n".join(result))



