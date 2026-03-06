import sys
input = sys.stdin.readline

# 재료 수 N, 갑옷 번호 M 입력
N = int(input())
M = int(input())
materials = list(map(int, input().split()))

# 정렬 후 투 포인터
materials.sort()
left, right = 0, N - 1
count = 0

while left < right:
    total = materials[left] + materials[right]
    if total == M:
        count += 1
        left += 1
        right -= 1
    elif total < M:
        left += 1
    else:
        right -= 1

print(count)