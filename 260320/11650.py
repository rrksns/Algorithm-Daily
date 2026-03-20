import sys

input = sys.stdin.readline

N = int(input())
loc = []

for i in range(N):
    x, y = map(int, input().split())
    loc.append((x, y))

loc.sort()

for p in loc:
    print(p[0], p[1], sep=" ")


# import sys

# # 입력 속도를 위해 sys.stdin.read 사용
# input = sys.stdin.read
# data = input().split()
# print(data)

# n = int(data[0])
# points = []

# for i in range(n):
#     x = int(data[2 * i + 1])
#     y = int(data[2 * i + 2])
#     points.append((x, y))

# # x좌표 -> y좌표 순으로 오름차순 정렬
# points.sort()

# for p in points:
#     print(p[0], p[1])
