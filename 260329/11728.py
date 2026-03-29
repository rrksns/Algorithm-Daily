import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = []
    a, b = 0, 0

    # 투 포인터: 두 배열을 동시에 순회하며 작은 값부터 결과에 추가
    while a < n and b < m:
        if A[a] <= B[b]:
            result.append(A[a])
            a += 1
        else:
            result.append(B[b])
            b += 1

    # 남은 원소 추가
    if a < n:
        result.extend(A[a:])
    if b < m:
        result.extend(B[b:])

    sys.stdout.write(' '.join(map(str, result)) + '\n')

main()