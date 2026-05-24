# 수 정렬하기 3 - Counting Sort
# N개의 수(1 ≤ Ai ≤ 10,000)를 정렬. N이 최대 1000만이라 메모리 제한이 있음
# 계수 정렬(Counting Sort): 1~10000 범위의 카운트 배열을 만들어 O(N+K)로 해결
# sys.stdout.write로 출력 속도를 최대화

import sys
input = sys.stdin.readline

def main():
    n = int(input())
    count = [0] * 10001
    for _ in range(n):
        count[int(input())] += 1
    
    result = []
    for num in range(1, 10001):
        if count[num] > 0:
            result.append((str(num) + '\n') * count[num])
    
    sys.stdout.write(''.join(result))

main()
