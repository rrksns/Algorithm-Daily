import sys

input = sys.stdin.readline

N = int(input())
alist = []

for i in range(N):
    age, name = map(str, input().split())
    alist.append((int(age), name))

alist.sort(key=lambda x: x[0])

for age, name in alist:
    print(age, name, sep=" ")
