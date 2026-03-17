import sys

input = sys.stdin.readline

N = int(input())

for i in range(1, N + 1):
    if i == N:  # 최하위 라인일때
        print("*" * (2 * i - 1))
    if i == 1:  # 최초 라인일때
        print(" " * (N - i), "*", sep="")
    else:  # 나머지 라인 일때
        print(" " * (N - i), "*", " " * (2 * i - 3), "*", sep="")
