import math

def is_prime(n):
    # 1 이하는 소수 아님
    if n < 2:
        return False
    # 2부터 √n까지 나누어 떨어지면 소수 아님
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 입력
N = int(input())
numbers = list(map(int, input().split()))

# 소수 개수 카운트
count = sum(1 for x in numbers if is_prime(x))

print(count)