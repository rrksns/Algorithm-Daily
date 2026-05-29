# 덩치 - BruteForce
# 모든 쌍을 비교하여, 자신보다 몸무게와 키 모두 큰 사람의 수 + 1이 등수
import sys
input = sys.stdin.readline

n = int(input())
people = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(n):
    rank = 1
    for j in range(n):
        if i == j:
            continue
        # j가 i보다 몸무게와 키 모두 크면 i의 등수가 밀림
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            rank += 1
    print(rank, end=' ')
print()
