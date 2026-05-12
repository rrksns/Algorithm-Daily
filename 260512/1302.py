# [해시맵] 베스트셀러
# 핵심 아이디어:
# Counter로 각 책의 판매 횟수를 집계한 뒤
# 최대 판매 횟수를 가진 책들 중 사전 순(lexicographic order) 가장 앞선 책을 출력한다.
# 파이썬 Counter + sorted 조합으로 간결하게 해결.

import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
books = [input().strip() for _ in range(n)]
counter = Counter(books)
max_count = max(counter.values())
candidates = sorted(b for b, cnt in counter.items() if cnt == max_count)
print(candidates[0])
