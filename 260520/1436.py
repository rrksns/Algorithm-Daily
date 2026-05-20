# 영화감독 숌 (BruteForce)
# 핵심 아이디어: 666을 포함하는 수를 순서대로 N번째까지 찾는 브루트포스
# - 666부터 시작하여 문자열로 변환 후 "666"이 포함되는지 확인
# - N이 최대 10000이므로 충분히 빠르게 동작
import sys
input = sys.stdin.readline

n = int(input())
count = 0
num = 665

while count < n:
    num += 1
    if '666' in str(num):
        count += 1

print(num)
