import sys
from itertools import combinations

input = sys.stdin.readline

def solve():
    N, K = map(int, input().split())
    words = [input().strip() for _ in range(N)]

    # 모든 단어가 "anta...tica" 형태 → a, n, t, i, c 5글자는 필수
    MUST = set('antic')

    # K < 5이면 어떤 단어도 읽을 수 없음
    if K < 5:
        print(0)
        return

    # 각 단어를 비트마스크로 변환 (알파벳 a=0, b=1, ..., z=25)
    word_masks = []
    for word in words:
        mask = 0
        for ch in word:
            mask |= (1 << (ord(ch) - ord('a')))
        word_masks.append(mask)

    # 필수 5글자 비트마스크
    must_mask = 0
    for ch in MUST:
        must_mask |= (1 << (ord(ch) - ord('a')))

    # K == 26이면 모든 단어 읽기 가능
    if K == 26:
        print(N)
        return

    # 필수 5글자를 제외한 나머지 21개 알파벳 인덱스
    remaining = [i for i in range(26) if not (must_mask >> i & 1)]

    # 나머지 알파벳 중 K-5개를 선택하는 모든 조합 탐색
    ans = 0
    for chosen in combinations(remaining, K - 5):
        # 선택된 알파벳 + 필수 5글자 비트마스크
        learned = must_mask
        for idx in chosen:
            learned |= (1 << idx)

        # 읽을 수 있는 단어 수: 단어 마스크가 learned의 부분집합이면 읽을 수 있음
        count = sum(1 for wm in word_masks if (wm & learned) == wm)
        ans = max(ans, count)

    print(ans)

solve()