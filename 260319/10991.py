import sys

input = sys.stdin.readline

N = int(input())

for i in range(1, N + 1):
    if i == 1:
        print(" " * (N - i), "*", sep="")
    else:
        print(" " * (N - i), "* " * i, sep="")
