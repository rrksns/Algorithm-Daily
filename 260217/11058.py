import sys
input = sys.stdin.readline

N = int(input())

# dp[i] = i번 눌렀을 때 화면에 출력할 수 있는 A의 최대 개수
dp = [0] * (N + 1)

for i in range(1, N + 1):
    # 1) 그냥 A를 한 번 누르는 경우
    dp[i] = dp[i - 1] + 1

    # 2) j번째까지 입력 후, Ctrl-A, Ctrl-C, 그리고 (i-j-2)번 Ctrl-V
    #    → dp[j] * (i - j - 1) (복사 후 붙여넣기 횟수 = i-j-2, 원본 포함하면 i-j-1배)
    for j in range(1, i - 2):
        dp[i] = max(dp[i], dp[j] * (i - j - 1))

print(dp[N])