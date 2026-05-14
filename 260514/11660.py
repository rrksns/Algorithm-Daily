# 구간 합 구하기 4 - 2차원 누적합(prefix sum) 활용
# prefix[i][j] = (1,1)부터 (i,j)까지의 직사각형 합
# 쿼리 (x1,y1)~(x2,y2) 합 = prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]
import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    prefix = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        row = list(map(int, input().split()))
        for j in range(1, N + 1):
            prefix[i][j] = row[j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]

    result = []
    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        ans = prefix[x2][y2] - prefix[x1 - 1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1]
        result.append(ans)

    print('\n'.join(map(str, result)))

main()
