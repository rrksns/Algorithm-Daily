# a와 b 사이의 모든 정수의 합 (a, b 포함)

a, b = map(int, input().split())

# a > b인 경우 swap
if a > b:
    a, b = b, a

# 등차수열 합 공식: (개수) * (첫항 + 끝항) / 2
count = b - a + 1
result = count * (a + b) // 2

print(result)