# 일곱 난쟁이
# 9명 중 키의 합이 100이 되는 7명을 찾기
# 9명 합에서 100을 뺀 값과 같은 두 난쟁이를 찾아 제거
import sys
input = sys.stdin.readline

heights = [int(input()) for _ in range(9)]
total = sum(heights)

found = False
for i in range(9):
    for j in range(i + 1, 9):
        if heights[i] + heights[j] == total - 100:
            result = sorted(h for k, h in enumerate(heights) if k != i and k != j)
            for h in result:
                print(h)
            found = True
            break
    if found:
        break
