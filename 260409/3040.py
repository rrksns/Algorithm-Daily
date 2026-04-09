import sys

input = sys.stdin.readline

# 9개의 모자 숫자 입력
hats = [int(input()) for _ in range(9)]

total = sum(hats)
diff = total - 100  # 빼야 할 두 가짜 난쟁이의 합

# 가짜 두 명 찾기 (이중 반복문)
found = False
for i in range(9):
    for j in range(i + 1, 9):
        if hats[i] + hats[j] == diff:
            # 가짜 두 명 제외하고 나머지 7명 출력
            result = [hats[k] for k in range(9) if k != i and k != j]
            result.sort()
            print("\n".join(map(str, result)))
            found = True
            break
    if found:
        break
