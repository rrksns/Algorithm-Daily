import sys

input = sys.stdin.readline

N = int(input())

way = [1, 3]

for i in range(2, N):
    way.append(way[i - 1] + 2 * way[i - 2])

print(way[N - 1] % 10007)
