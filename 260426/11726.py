import sys

input = sys.stdin.readline

N = int(input())
way = [0] * (N + 1)
way[1] = 1
way[2] = 2
for i in range(3, N + 1):
    way[i] = way[i - 2] + way[i - 1]

print(way[N])
