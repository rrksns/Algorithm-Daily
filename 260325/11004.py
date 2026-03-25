import sys

input = sys.stdin.readline

n, k = map(int, input().split())

alist = list(map(int, input().split()))

alist.sort()

print(alist[k - 1])
