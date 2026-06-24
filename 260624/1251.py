# 백준 1251: 단어 나누기
# 단어를 세 부분으로 나눠 각각 뒤집은 뒤 이어붙인 결과 중 사전순 최솟값 출력
# 브루트포스: 두 분할 지점 i, j (1 <= i < j <= n-1)를 모두 탐색

import sys
input = sys.stdin.readline

def solve():
    word = input().strip()
    n = len(word)
    result = None

    for i in range(1, n - 1):
        for j in range(i + 1, n):
            part = word[:i][::-1] + word[i:j][::-1] + word[j:][::-1]
            if result is None or part < result:
                result = part

    print(result)

solve()
