import sys
input = sys.stdin.readline

# 구간 합 구하기 - 누적 합(Prefix Sum)
# prefix[i] = arr[1] + arr[2] + ... + arr[i]
# 구간 [i, j] 합 = prefix[j] - prefix[i-1]

n, m = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i-1] + arr[i-1]

for _ in range(m):
    i, j = map(int, input().split())
    print(prefix[j] - prefix[i-1])
