# 그룹 단어 체커 - String
# 그룹 단어: 각 문자가 연속된 구간에만 나타나는 단어
# 이전에 나왔다가 사라진 문자가 다시 나오면 그룹 단어가 아님
import sys
input = sys.stdin.readline

n = int(input())
count = 0

for _ in range(n):
    word = input().strip()
    seen = set()
    prev = ''
    is_group = True
    for c in word:
        if c != prev:
            if c in seen:
                is_group = False
                break
            seen.add(prev)
            prev = c
    if is_group:
        count += 1

print(count)
