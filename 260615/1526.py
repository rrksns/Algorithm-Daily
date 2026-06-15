# 금민수: 4와 7로만 이루어진 수 (lucky number)
# 4를 0, 7을 1로 보고, K번째 수를 이진수처럼 생성
# 1자리: 4,7 (2개), 2자리: 44,47,74,77 (4개), d자리: 2^d개
import sys
input = sys.stdin.readline

def solve():
    K = int(input())
    # d자리 금민수를 순서대로 생성하다가 K번째 수 반환
    nums = []
    d = 1
    while len(nums) < K:
        for i in range(2 ** d):
            binary = format(i, f'0{d}b')
            num = int(binary.replace('0', '4').replace('1', '7'))
            nums.append(num)
        d += 1
    print(nums[K - 1])

solve()
