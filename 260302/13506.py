import sys
input = sys.stdin.readline

def solve():
    S = input().strip()
    n = len(S)

    if n == 1:
        print(-1)
        return

    # KMP 실패 함수 계산
    fail = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and S[i] != S[j]:
            j = fail[j-1]
        if S[i] == S[j]:
            j += 1
        fail[i] = j

    # cnt[k]: fail 배열에서 k가 등장하는 횟수 (=접두사 길이 k인 부분문자열이
    # 접두사 위치 제외하고 등장하는 횟수, 단 중첩 포함)
    cnt = [0] * (n + 1)
    for v in fail:
        if v > 0:
            cnt[v] += 1

    # 전파: 길이 k인 prefix=suffix → 그보다 짧은 fail[k-1] 길이도 그 위치에서 등장
    for k in range(n, 0, -1):
        if k > 1 and cnt[k] > 0:
            cnt[fail[k-1]] += cnt[k]

    # fail[n-1] 체인을 따라가며 cnt[k] >= 2인 가장 큰 k 탐색
    # (접두사 1번 + 접미사 1번 + 내부 1번 이상 = 총 3번 → cnt[k]>=2)
    ans = -1
    k = fail[n-1]
    while k > 0:
        if cnt[k] >= 2:
            ans = k
            break
        k = fail[k-1]

    if ans == -1:
        print(-1)
    else:
        print(S[:ans])

solve()