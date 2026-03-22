# N!의 뒤에서부터 연속된 0의 개수 구하기
# 핵심: 끝자리 0 = 2와 5의 쌍 → N!에서 2가 항상 더 많으므로 5의 개수만 세면 됨

n = int(input())

count = 0
# 5, 25, 125, 625... 각 5의 거듭제곱이 기여하는 5의 인수 개수를 합산
power_of_5 = 5
while power_of_5 <= n:
    count += n // power_of_5
    power_of_5 *= 5

print(count)